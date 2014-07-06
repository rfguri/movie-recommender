from math import sqrt
import os

# Returns a distance-based similarity score for person1 and person2
def sim_distance(prefs,person1,person2):
    # Get the list shared_items
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1

    # If they have no ratings in common,return 0
    if len(si)==0: return 0

    # Add up the squares of all the differences
    sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2) for item in si])

    return 1/(1+sqrt(sum_of_squares))

# Returns the Pearson correlation coefficient for person1 and person2
def sim_pearson(prefs,person1,person2):
    # Get the list of mutually rated items
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]: si[item]=1

    # Find the number of elements
    n=len(si)

    # If they have no ratings in common,return 0
    if n==0: return 0

    # Add up all the preferences
    sum1=sum([prefs[person1][item] for item in si])
    sum2=sum([prefs[person2][item] for item in si])

    # Sum up the squares
    sum1_of_squares=sum([pow(prefs[person1][item],2) for item in si])
    sum2_of_squares=sum([pow(prefs[person2][item],2) for item in si])

    # Sum up the products
    product_sum=sum([prefs[person1][item]*prefs[person2][item] for item in si])

    # Calculate Pearson score
    num=product_sum-(sum1*sum2/n)
    den=sqrt((sum1_of_squares-pow(sum1,2)/n)*(sum2_of_squares-pow(sum2,2)/n))
    if den==0: return 0

    r=num/den

    return r

# Returns the best matches for person from the data dictionary
# Number of results and similarity functon ara optional parameters
def top_matches(prefs,person,n=5,similarity=sim_pearson):
    scores=[(similarity(prefs,person,other),other) for other in prefs if other!=person]

    # Sort the list so the highest scores appear at the top
    scores.sort()
    scores.reverse()

    return scores[0:n]

# Gets recomendations for a person by using a weighted average
# of every other user's rnkings
def get_recommendations(prefs,person,similarity=sim_pearson):
    totals={}
    sim_sums={}
    for other in prefs:
        # Don't compare me to myself
        if other==person: continue
        sim=similarity(prefs,person,other)

        # Ignore scores of zero or lower
        if sim<=0: continue
        for item in prefs[other]:
            # Only score movies I haven't seen yet
            if item not in prefs[person] or prefs[person][item]==0:
                # Similarity * Score
                totals.setdefault(item,0)
                totals[item]+=prefs[other][item]*sim
                # Sum of similarities
                sim_sums.setdefault(item,0)
                sim_sums[item]+=sim

    # Create the normalized list
    rankings=[(total/sim_sums[item],item) for item,total in totals.items()]

    # Sort the list so the highest rankins appear at the top
    rankings.sort()
    rankings.reverse()

    return rankings

# Returns flipped item and person values
def transform_prefs(prefs):
    result={}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item,{})

            # Flip item and person
            result[item][person]=prefs[person][item]

    return result

# Builds a complete dataset of similar items
def calculate_similar_items(prefs,n=10):
    # Create a dictionary of items showeing which other itmes they
    # are most similar to
    result={}

    # Invert the preference matrix to be item-centric
    item_prefs=transform_prefs(prefs)
    c=0
    for item in item_prefs:
        # Status updates for large datasets
        c+=1
        if c%100==0: print "%d / %d" % (c,len(item_prefs))
        # Find the most similar items to this one
        scores=top_matches(item_prefs,item,n=n,similarity=sim_distance)
        result[item]=scores
    return result

# Returns recommendations using the item similarity dictionary without going through the whole dataset
def get_recommended_items(prefs,item_match,user):
    user_ratings=prefs[user]
    scores={}
    total_sim={}

    # Loop over items rated by this user
    for (item,rating) in user_ratings.items():
        # Loop over items similar to this one
        for (similarity,item2) in item_match[item]:
            # Ignore if this user has already rated this item
            if item2 in user_ratings: continue
            # Weighted sum of rating times similarity
            scores.setdefault(item2,0)
            scores[item2]+=similarity*rating

            # Sum of all the similarities
            total_sim.setdefault(item2,0)
            total_sim[item2]+=similarity
    # Divide each total score by total weighting to get an average
    rankings=[(score/total_sim[item],item) for item,score in scores.items()]

    # Return the rankings from highest to lowest
    rankings.sort()
    rankings.reverse()
    return rankings

# Load Movie Lens dataset
def load_movie_lens(path='/data'):
    curr_path=os.path.dirname(os.path.abspath(__file__))
    path=curr_path+path

    # Get movie titles
    movies = {}
    for line in open(path+'/u.item'):
        (id,title)=line.split('|')[0:2]
        movies[id]=title

    # Load data
    prefs={}
    for line in open(path+'/u.data'):
        (user,movieid,rating,ts)=line.split('\t')
        prefs.setdefault(user,{})
        prefs[user][movies[movieid]]=float(rating)
    return prefs

