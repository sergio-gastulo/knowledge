# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 20:14:01 2023

@author: sgast
"""

import numpy as np 
from sklearn.cluster import DBSCAN 
from sklearn.datasets import make_blobs 
from sklearn.preprocessing import StandardScaler 
import matplotlib.pyplot as plt 

#%%

def createDataPoints(centroidLocation, numSamples, clusterDeviation):
    # Create random data and store in feature matrix X and response vector y.
    X, y = make_blobs(n_samples=numSamples, centers=centroidLocation, 
                                cluster_std=clusterDeviation)
    
    # Standardize features by removing the mean and scaling to unit variance
    X = StandardScaler().fit_transform(X)
    return X, y

#%%

X, y = createDataPoints(
    centroidLocation = [[4,3], [2,-1], [-1,4]] , 
    numSamples = 1500, 
    clusterDeviation=0.5)


#%%