import random
import pandas as pd
import pickle
import numpy as np
from utils import movies


movies_list = movies.title.tolist()

with open('data/nmf_modelproj.pkl','rb') as file:
    model = pickle.load(file)


def get_recommendations_random():
    random.shuffle(movies_list)
    return movies_list[:3]

def get_recommendations_NMF(query, k=10):
    """
    Filters and recommends the top k movies for any given input query based on a trained NMF model. 
    Returns a list of k movie ids.
    """
    
    recommendations = []
    # 1. candidate generation
    # construct new_user-item dataframe given the query
    new_query = pd.DataFrame(query, columns=movies_list, index=['new_user'])
    new_query_imputed = new_query.fillna(value=0)
   
    # 2. scoring
    # calculate the score with the NMF model
    Q_matrix = model.components_
    P_new_query_matrix = model.transform(new_query_imputed)
    R_hat_new_query_matrix = np.dot(P_new_query_matrix, Q_matrix)
    R_hat_new_query = pd.DataFrame(data=R_hat_new_query_matrix,
                                   columns=model.feature_names_in_,
                                   index=['new_user'])
    
    # 3. ranking
    query_ranking = R_hat_new_query.transpose().sort_values(by='new_user',
                                                            ascending=False).index.to_list()
    # filter out movies already seen by the user
    query_rated = list(query.keys())
    query_filtered = [mov for mov in query_ranking if mov not in query_rated]
    # return the top-k highest rated movie ids or titles
    recommendations = query_filtered[0:k]
    return recommendations


def recommend_neighborhood(query, model, k=3):
    """
    Filters and recommends the top k movies for any given input query based on a trained nearest neighbors model. 
    Returns a list of k movie ids.
    """   
    pass