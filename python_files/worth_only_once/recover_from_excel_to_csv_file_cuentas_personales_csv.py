
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 19:35:06 2024

@author: sgast
"""

import pandas as pd 
df = pd.read_csv(r'C:\Users\sgast\excel\Cuentas_de_Sergio.csv')

#%%

#Dropeando columnas innecesarias

for i in range(4,11):
    df.drop(['Unnamed: '+str(i)], axis = 1, inplace = True)
del(i)
    
df.drop(df.index[:2],inplace = True)

#%%

#limpiando los nombres de columna
df = df.rename(columns = df.iloc[0]).drop(df.index[0])
df.columns = df.columns.str.replace(' ','')

'''
    Limpiando la columna Monto
'''

df['Monto'] = df.Monto.str.replace('PEN ', '')
df['Monto'] = df.Monto.str.replace(' ', '')
df['Monto'] = df.Monto.str.replace(',', '')
df['Monto'] = df.Monto.astype('float64')
df.reset_index(inplace = True)
df.drop('index',inplace=True,axis = 1)

#%%

from datetime import datetime as dt

def datetime_function(date_string):
    parsed_date = dt.strptime(date_string, "%d-%b")
    
    if parsed_date.month >= 8:
        parsed_date = parsed_date.replace(year = 2023)
    else:
        parsed_date = parsed_date.replace(year = 2024)
    
    return parsed_date.strftime("%d-%m-%Y")

df.Fecha = df.Fecha.apply(datetime_function)
#%%

df.to_csv('cuentas.csv', index = False)

#%%










