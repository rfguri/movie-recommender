# Lib imports
import recommendations, time

# Function's execution
t1 = time.time()
prefs=recommendations.load_movie_lens()
t2 = time.time()
print "Recomendations: {}".format(recommendations.get_recommendations(prefs,'87')[0:30])
t3 = time.time()
itemsim=recommendations.calculate_similar_items(prefs,50)
t4 = time.time()
print "Recommended items: {}".format(recommendations.get_recommended_items(prefs,itemsim,'87')[0:30])
t5 = time.time()
print "\nExecution times"
print "-----------------"
print "Load dataset: {} seconds".format(t2-t1)
print "User based filtering: {} seconds".format(t3-t2)
print "Calculate similar item: {} seconds".format(t4-t3)
print "Item based filtering: {} seconds".format(t5-t4)
