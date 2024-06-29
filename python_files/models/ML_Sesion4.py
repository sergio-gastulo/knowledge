# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 09:36:53 2023

@author: sgast
"""

import os 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

df = pd.read_csv("https://raw.githubusercontent.com/robintux/Datasets4StackOverFlowQuestions/master/HousePrices.csv")

ListaVarNumericas = []
ListaVarCualitativas = []

for col in df.columns:
    if df[col].dtype in ["int64","float64"]:
        ListaVarNumericas.append(col)
    else:
        ListaVarCualitativas.append(col)

df[ListaVarNumericas].isnull().sum().sort_values(ascending = False)
df[ListaVarNumericas] = df[ListaVarNumericas].fillna(df[ListaVarNumericas].mean())

y = df[ListaVarNumericas].SalePrice
x = df[ListaVarNumericas[:-2]]

X_train, X_test, Y_train, Y_test = train_test_split(x,y,train_size = 0.85)

ModelHousePrice1 = LinearRegression()
ModelHousePrice1.fit(X_train, Y_train)

y_pronostico = ModelHousePrice1.predict(X_test)
ModelHousePrice1_MAPE = metrics.mean_absolute_percentage_error(Y_test, y_pronostico)

#%%

Xc = df[ListaVarCualitativas]

#"Valores faltantes:"
list_to_remove = list(Xc.isnull().sum().sort_values(ascending = False).head().index)
Xc = Xc.drop(labels = list_to_remove,axis = "columns")
#Eliminaremos las siguientes 5 columnas
#PoolQC           1453
#MiscFeature      1406
#Alley            1369
#Fence            1179
#MasVnrType        872
#FireplaceQu       690

#%%

Lista_var_cualitativas_final = Xc.columns
for col in Lista_var_cualitativas_final:
    Xc[col] = Xc[col].fillna(Xc[col].mode()[0])

Xc = pd.get_dummies(Xc)














