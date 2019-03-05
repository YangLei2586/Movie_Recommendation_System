# Movie_Recommendation_System
A Movie Recommendation System using Lightfm library 

(1) Problem Framing 

Our options to learn or to buy or to experience or to create are limitless on the web and in life. All of this abundance presents a problem “the paradox of choice”. We could spend way too much time trying to pick one because we have so many choices. We could end up with not picking anything at all or worse picking something and then get FOMO (fear of missing out). If there was a way to have an abundance of options and have certainty in our decisions that would be ideal. That’s how recommendation systems help us. 

(2) Problem Solving 

Amazon recommends products we’d like. Google recommends search results we’d like. Facebook recommends friends we’d like. Pretty much a lot of services do that now. There are two main types of recommender systems:
(a) Collaborative system
Collaborative systems predict what you like based on what other similar users have liked in the past.
(b) Content based system
Content based system predict what you like based on what you’ve liked in the past.

However, some times these two method will be combined for the consideration of better production results. For example Netflix combine both approaches to be even more accurate. In our scripts we will combine two of this approaches to produce a hybrid model.

(3) Libaries 

(a) numpy for scientic computing
(b) lightfm for datasets and modeling 

(4) Dataset

We will use the defealt dataset coming from the libary of lightfm called movielens, which is a big CSV file that contains 100K movies ratings from 1K users on 1700 movies. Each user has rated at least 20 moives on a scale of 1 to 5.

The fetch movie lens method takes in an optional parameter called min rating, which stands for the minimum rating we want to include in our data, will set to 4.0 meaning we're only clollecting the movies with a rating of 4 or higher. This method will create an interaction matrix from our CSV file and store in our data varible as a dictionary.
