movie-recommender
=================

Movie recommender using data from MovieLens Dataset to find similar movies and recommend the ones they haven't seen before

## Instructions
To run the program issue the following command:
```bash
python main.py
````

## Result
This is an example result when executing the main program (note: execution's times may vary depending on your machine):
```
Recomendations: [(5.0, 'They Made Me a Criminal (1939)'), (5.0, 'Star Kid (1997)'), (5.0, 'Santa with Muscles (1996)'), (5.0, 'Saint of Fort Washington, The (1993)'), (5.0, 'Marlene Dietrich: Shadow and Light (1996) '), (5.0, 'Great Day in Harlem, A (1994)'), (5.0, 'Entertaining Angels: The Dorothy Day Story (1996)'), (5.0, 'Boys, Les (1997)'), (4.89884443128923, 'Legal Deceit (1997)'), (4.815019082242709, 'Letter From Death Row, A (1998)'), (4.7321082983941425, 'Hearts and Minds (1996)'), (4.696244466490867, 'Pather Panchali (1955)'), (4.652397061026758, 'Lamerica (1994)'), (4.538723693474813, 'Leading Man, The (1996)'), (4.535081339106103, 'Mrs. Dalloway (1997)'), (4.532337612572981, 'Innocents, The (1961)'), (4.527998574747079, 'Casablanca (1942)'), (4.510270149719864, 'Everest (1998)'), (4.493967755428439, 'Dangerous Beauty (1998)'), (4.485151301801342, 'Wallace & Gromit: The Best of Aardman Animation (1996)'), (4.463287461290222, 'Wrong Trousers, The (1993)'), (4.450979436941035, 'Kaspar Hauser (1993)'), (4.431079071179518, 'Usual Suspects, The (1995)'), (4.427520682864959, 'Maya Lin: A Strong Clear Vision (1994)'), (4.414870784592075, 'Wedding Gift, The (1994)'), (4.377445252656464, 'Affair to Remember, An (1957)'), (4.376071110447771, 'Good Will Hunting (1997)'), (4.376011099001396, 'As Good As It Gets (1997)'), (4.374146179500976, 'Anna (1996)'), (4.367437266504598, 'Close Shave, A (1995)')]

Building item dataset:
100 / 1664
200 / 1664
300 / 1664
400 / 1664
500 / 1664
600 / 1664
700 / 1664
800 / 1664
900 / 1664
1000 / 1664
1100 / 1664
1200 / 1664
1300 / 1664
1400 / 1664
1500 / 1664
1600 / 1664

Recommended items: [(5.0, "What's Eating Gilbert Grape (1993)"), (5.0, 'Vertigo (1958)'), (5.0, 'Usual Suspects, The (1995)'), (5.0, 'Toy Story (1995)'), (5.0, 'Titanic (1997)'), (5.0, 'Sword in the Stone, The (1963)'), (5.0, 'Stand by Me (1986)'), (5.0, 'Sling Blade (1996)'), (5.0, 'Silence of the Lambs, The (1991)'), (5.0, 'Shining, The (1980)'), (5.0, 'Shine (1996)'), (5.0, 'Sense and Sensibility (1995)'), (5.0, 'Scream (1996)'), (5.0, 'Rumble in the Bronx (1995)'), (5.0, 'Rock, The (1996)'), (5.0, 'Robin Hood: Prince of Thieves (1991)'), (5.0, 'Reservoir Dogs (1992)'), (5.0, 'Police Story 4: Project S (Chao ji ji hua) (1993)'), (5.0, 'House of the Spirits, The (1993)'), (5.0, 'Fresh (1994)'), (5.0, 'Denise Calls Up (1995)'), (5.0, 'Day the Sun Turned Cold, The (Tianguo niezi) (1994)'), (5.0, 'Before the Rain (Pred dozhdot) (1994)'), (5.0, 'Assignment, The (1997)'), (5.0, '1-900 (1994)'), (4.875, "Ed's Next Move (1996)"), (4.833333333333333, 'Anna (1996)'), (4.8, 'Dark City (1998)'), (4.75, 'Flower of My Secret, The (Flor de mi secreto, La) (1995)'), (4.75, 'Broken English (1996)')]

Execution's times
-----------------
Load dataset: 0.162872076035 seconds
User based filtering: 0.126660108566 seconds
Calculate similar item: 34.2250339985 seconds
Item based filtering: 0.0105328559875 seconds
```
