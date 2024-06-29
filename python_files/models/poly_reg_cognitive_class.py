# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 18:42:36 2023

@author: sgast
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score

df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv")
df.head()

#%%

from sklearn.preprocessing import PolynomialFeatures

def testing_all_columns(df, t_size, c_pred, best=False):
    col_list_to_test = []
    dic = {}
    for col_name in df.columns:
        if df[col_name].dtype in [
            'int64', 
            'float64', 
            'int16', 
            'float16', 
            'int32', 
            'float32', 
            'int8', 
            'float8'] and col_name != c_pred and df[col_name].std()!=0:
            col_list_to_test.append(col_name)
    
    poly = PolynomialFeatures(
        degree=3, 
        interaction_only=True)
    X = df[col_list_to_test]
    Y = df[c_pred]
    for i in range(100):
        
        msk = np.random.rand(len(df)) < t_size 
        train = poly.fit_transform(df[msk])
        test = poly.fit_transform(df[~msk])
        
        regr = linear_model.LinearRegression()
        x = np.asanyarray(train[col_list_to_test])
        y = np.asanyarray(train[c_pred])
        regr.fit(x,y)
        y_hat= regr.predict(test[col_list_to_test])
        z = r2_score(test[c_pred] , y_hat)
        dic[i] = [regr.coef_, z]

    
    dic = pd.DataFrame(dic).T
    dic.columns = ['m_vect', 'r2']
    dic = dic.sort_values(
        by = 'r2', 
        axis = 0, 
        ascending = False)
    
    if best:
        return dic
    else:
        return dic.iloc[0,0]