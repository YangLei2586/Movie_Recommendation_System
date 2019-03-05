#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import libaries
import numpy as np
from lightfm.datasets import fetch_movielens # movielens is big csv file containing 100K movies ratings from 1K users on 1700 movies
from lightfm import lightFM

# Fetch and format data
data = fetch_movielens(min_rating = 4.0)     # creat a variable called "data" to store data set in; min_rating equals 4.0 means we only include the movies with a rating of 4 or higher

# print training and testing data
print(repr(data['train']))
print(repr(data['test']))

# creat and initialize model
model = LightFM(loss = 'warp')               # choosing a Weighted Approximate-Rank Pairwise loss function called warp, which will help us creat recommendations for each users by looking at the existing users rating pairs and predicting rankings for each. It uses the gradient descent algorithm to iteratively find the weights that improve our prediction over time. This model takes into account book the user's past rating history content and similar users ratings collaborative
# train the model
model.fit(data['train'],epochs=30,num_threads=2)

# define a sample recommendation function
def sampel_recommendation(model,data,user_ids):
    
    n_users, n_items = data['train'].shape                                            # number of users and movies in training data
    
    for user_id in user_ids:
        
        known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices] # movies they already like
        
        scores = model.predict(user_id,np.arange(n_items))                            # movies our model predicts they will like
        
        top_items = data['item_labels'][np.argsort(-scores)]                          # rank them in order of most liked to least
        
        print("User %s" % user_id)
        print("   known positives:")                                                  # print out the results
        
        for x in known_positives[:3]:
            print("      %s" % x)
        
        print("     Recommended:")
        
        for x in top_items[:3]:
            print("      %s" % x)


# In[ ]:




