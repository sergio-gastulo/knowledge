# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 11:50:07 2023

@author: sgast
"""

import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn import linear_model as lin_mod
from sklearn.model_selection import train_test_split

datos = pd.read_csv("https://raw.githubusercontent.com/robintux/Datasets4StackOverFlowQuestions/master/Consumo_cerveza_SP.csv")
datos.info()

#%%
datos.rename(columns = {
    'Temperatura Media (C)': "Temperatura_Media",
    'Temperatura Minima (C)': "Temperatura_Minima",
    'Temperatura Maxima (C)': "Temperatura_Maxima",
    'Precipitacao (mm)': 'Precipitacion',
    'Final de Semana': 'Fin_de_semana',
    'Consumo de cerveja (litros)': 'Consumo_litros'
}, inplace = True)
datos.head(15)
#%%
datos.Temperatura_Minima = datos.Temperatura_Minima.str.replace(',','.').astype(float)
datos.Temperatura_Media = datos.Temperatura_Media.str.replace(',','.').astype(float)
datos.Temperatura_Maxima = datos.Temperatura_Maxima.str.replace(',','.').astype(float)
datos.Precipitacion = datos.Precipitacion.str.replace(',','.').astype(float)
datos = datos.dropna()
datos.isnull().sum()
datos.head()
#%%
datos.Data = pd.to_datetime(datos.Data)
datos.info()
#%%
#variables a utilizar:
y = datos.Consumo_litros
x = datos[["Fin_de_semana","Temperatura_Maxima","Precipitacion"]]

#Particionando los datos:
#Train: sirve para calcular los parametros del modelo
#Test: sirve para calcular los indicadores de calidad del modelo
#Indicador de calidad: MAPE "<=20 es bueno"
x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=0.9)

#Instanciamos la clase a modelar:
model2 = lin_mod.LinearRegression()

#Ajustar el modelo con los métodos de entrenamiento
model2.fit(x_train,y_train)
#%%
ScoreTrain = model2.score(x_train,y_train)
ScoreTest = model2.score(x_test,y_test)
print(f'''
  R^2 train : {100*ScoreTrain}%
  R^2 test : {100*ScoreTest}%
      ''')

#%%
def Model1():
  X_train, X_test, y_train, y_test = train_test_split(datos[["Temperatura_Media", "Temperatura_Minima",
            "Temperatura_Maxima", "Precipitacion",
            "Fin_de_semana"]], datos.Consumo_litros,
                                                    train_size = 0.85)
  # Instanciamos el modelo
  modelo = lin_mod.LinearRegression()
  # Ajustamos el modelo
  modelo.fit(X_train[["Temperatura_Maxima", "Precipitacion"]], y_train)
  # La funcion debe devolver algunos requerimientos
  return {"MAPE" : 100*metrics.mean_absolute_percentage_error(y_test, modelo.predict(X_test[["Temperatura_Maxima", "Precipitacion"]])),
            "Scores": [modelo.score(X_train[["Temperatura_Maxima", "Precipitacion"]], y_train), modelo.score(X_test[["Temperatura_Maxima", "Precipitacion"]], y_test)],
            "Parametros" : [modelo.coef_, modelo.intercept_]}

#%%
MAPE = 0
for i in range(100):
  MAPE+=Model1()["MAPE"]
  # print(model1())
print(np.var(MAPE))







