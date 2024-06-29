# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 11:17:38 2023

@author: sgast
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#%%

"""
    we'll deal with a multilinear problem. the idea is to understand 
    how it works 
"""

df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv")
df.head()
#%%
"""
    Choosing float and int data
"""

cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
cdf.head()

#%%

"""
    testing:
"""
msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]

#%%

"""
    contructing our model 
"""

from sklearn import linear_model
regr = linear_model.LinearRegression()
x = np.asanyarray(train[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']])
y = np.asanyarray(train[['CO2EMISSIONS']])
regr.fit (x, y)
# The coefficients
print ('Coefficients: ', regr.coef_)

#%%

"""
    metrics of prediction
"""

y_hat= regr.predict(test[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']])
x = np.asanyarray(test[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']])
y = np.asanyarray(test[['CO2EMISSIONS']])
print("Mean Squared Error (MSE) : %.2f"
      % np.mean((y_hat - y) ** 2))

# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(x, y))


#%%

"""
    I thought i could be a good idea to take only 
    the columns of the df which are highly correlated
    to the TARGET columns.
    However, according to CHATGPT, this can lead to 
    an overfitted model, so it's not a good choice
    to keep the top correlated ones.
    We'll leave this function as a map which multilinearly 
    regresses the column to predict. 
    We cannot develop a programm like linear_reg_ since
    taking into consideration each of the N columns and
    playing with them, regressively could lead to high
    computer perfomance... which is not good (trying 2^N
    columns is insane)
"""

#import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score
#from colour import Color

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
            'float8'] and col_name != c_pred:
            col_list_to_test.append(col_name)
    
    for i in range(100):
        
        msk = np.random.rand(len(df)) < t_size 
        train = df[msk]
        test = df[~msk]
        
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









