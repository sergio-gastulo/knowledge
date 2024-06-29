# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 21:36:48 2024

@author: sgast
"""

import pandas as pd
import numpy as np
import sklearn

train_path = r'C:\Users\sgast\Downloads\train.csv' 
test_path  = r'C:\Users\sgast\Downloads\test (2).csv'

df_train = pd.read_csv(train_path)
df_test = pd.read_csv(test_path)

target = 'SalePrice'

final_list = list(df_train.columns)
final_list.remove(target)
lista_float = []
lista_str = []

for i in final_list:
    if df_train[i].dtype in ['float64','int64']:
        lista_float.append(i)
    else:
        lista_str.append(i)

del(i)

#%%

X = df_train[final_list].values
y = df_train[target].values

from sklearn.ensemble import RandomForestRegressor as RFR
from sklearn.metrics import mean_absolute_error as MAE
from sklearn.model_selection import train_test_split

xx_index = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
xx = df_train[xx_index]
yy = y.copy()

train_xx, test_xx, train_yy, test_yy = train_test_split(xx,yy, random_state=1)

rf_model = RFR(random_state = 1)
rf_model.fit(train_xx,train_yy)
rf_predictions = rf_model.predict(test_xx)
rf_mae = MAE(rf_predictions, test_yy)

print(f"Validation MAE for Random Forest Model: {rf_mae}")


#%% MI TURNO OMEGALUL

"""
    Dropping rows with nan values.
"""
#Cheking nans values:
df_train[lista_float].isnull().sum().sort_values(ascending = False).head()

#%%
#dropping first three:
lista_float.remove('LotFrontage')
lista_float.remove('GarageYrBlt')
lista_float.remove('MasVnrArea')

#%%

from sklearn.ensemble import RandomForestRegressor as RFR
from sklearn.metrics import mean_absolute_error as MAE
from sklearn.model_selection import train_test_split

X = df_train[lista_float]
y = df_train[target]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y, 
    test_size = 0.15, 
    random_state = 420)

rfr = RFR(random_state=420)
rfr.fit(X_train,y_train)
y_predicted = rfr.predict(X_test)
rfr_mae = MAE(y_test,y_predicted)

print(f"Validation MAE for Random Forest Model: {rfr_mae}")

test_data = df_test[lista_float]

#%% RUN WHEN READY

y_test_predicted = rfr.predict(test_data)

output = pd.DataFrame({'Id': test_data.Id,
                       'SalePrice': y_test_predicted})
output.to_csv('test_2.csv', index=False)

#%%
