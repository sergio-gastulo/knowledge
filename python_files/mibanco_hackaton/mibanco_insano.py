#%% LOAD
#-*- coding: utf-8 -*-
"""
Created on Fri Nov 17 15:35:34 2023
This is the last version of the python script I made for a machine learning competition on Kaggle a couple of months ago
Default probability: the idea was to predict if a certain customer, with some properties, could pay a loan
"""

import numpy as np
import pandas as pd
import statistics as st
import matplotlib.pyplot as plt

"""
    the paths of the csv files provided by mibanco on the kaggle dathaton
"""

filepaths = [r'C:\Users\sgast\Downloads\datathon-mibanco\test.csv', 
             r'C:\Users\sgast\Downloads\datathon-mibanco\train.csv',
             r'C:\Users\sgast\Downloads\datathon-mibanco\customers.csv',
             r'C:\Users\sgast\Downloads\datathon-mibanco\balances.csv']

# Reading the files with filepath, not optimal tbh

df_balances = pd.read_csv(filepaths[3])
df_customers = pd.read_csv(filepaths[2])
df_train = pd.read_csv(filepaths[1])
df_test = pd.read_csv(filepaths[0])

#%%SCALER DEF

"""
    Here, i wanted chose the columns with numerical values: cuanti
    so a standar scalling would be appropiate
"""

def SCALER(df:pd.DataFrame):
    cuanti = []
    for i in df.columns:
        if df[i].dtype in ['float64','int64']:
            cuanti.append(i)

    from sklearn.preprocessing import StandardScaler
    _scaler_ = StandardScaler()
    #scalling the columns with numerical values
    df[cuanti] = _scaler_.fit_transform(df[cuanti])

#%% CLEANING CUSTOMERS

"""
    cleaning customers: 
    customers where their location is unknown where deleted
"""
df_customers['BOOL_VIVIENDA'] = ((
    df_customers.NO_DEPARTAMENTO.notnull()
    ) & (
        df_customers.NO_PROVINCIA.notnull()
        )
        )

"""
    More cleaning, though i dont know exactly why i was dropping the rows i previously filtered
"""

df_customers.drop(columns= ['NO_DEPARTAMENTO','NO_PROVINCIA', 'DE_CIIU'],
                  axis = 1,
                  inplace = True)

"""
    More cleaning, filling the rows with mean on age, it is not a good practice.
"""

df_customers.EDAD.fillna(
    df_customers.EDAD.mean(), inplace=True)

"""
    Getting dummies on the sex of the client
"""

df_customers = pd.get_dummies(
    data = df_customers,
    columns = ['CO_TIPO_SEXO'])
     
""" 
    *********** CUSTOMERS CLEANED *********** 
"""

#%% AGRUPANDO SALDOS NO CORRER

"""
    This is a cell made for data exploring, as it says above, do not run this cell
"""

saldos_dola = []

saldos = []

for i in df_balances.columns:
    if i.find('SALDO')!=-1:
        if i.find('DOLA')!=-1:
            saldos_dola.append(i)
        else:
            saldos.append(i)
df_balances['BOOL_SALDO'] = (
    df_balances[saldos].sum(axis = 1) 
    + 4*df_balances[saldos_dola].sum(axis=1)
    >= 10_000
    )

df_balances.drop(
    columns = saldos_dola + saldos, 
    axis = 1, 
    inplace = True)

#%% X CREATION

"""
    Creation of the final matrix made for logistic regression
"""

#Dropping period columns
df_balances.drop(columns = ['PERIODO'], 
      axis = 1,
      inplace=True)
        
#Adding those values to the X matrix
X=(
    df_balances
    .groupby('ID')
    .agg([
        np.min,np.max,np.mean,np.std
        ])
    .reset_index()
)

#renamming columns
X.columns=range(len(X.columns))
X.rename(columns={0:'ID'},inplace=True)

#merging df_customers to X
X = X.merge(
    df_customers,
    on = 'ID',how='inner')
X.columns = X.columns.astype(str)

#%%
#scalling the X values
SCALER(df = X)


#%% ADDING TRAINING TO X

X=pd.merge(
    X,
    df_train,
    on='ID',
    how='left'
    )

X.columns = X.columns.astype(str)

#%%TRAINING WITH LOGISTIC

"""
    The final part of the code, where the logistic regression is modeled
"""

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)

model.fit(X[
    X.
    TARGET.
    notnull()]
    .drop(['ID','TARGET'], axis=1), 
    X[
    X.
    TARGET.
    notnull()]
    .TARGET)

X.loc[
    X.TARGET.isnull(),
    'TARGET'] = model.predict(
        X[
            X.
            TARGET.
            isnull()].
        drop(['ID','TARGET'],axis=1))

(X[
    X
    .ID
    .isin(
        df_test.ID)]
    [['ID','TARGET']]
    .to_csv('test.csv',index=False)
)

"""
    Not my best code, there are some steps lost on the time which i wont understand since the csv files where deleted on the kaggle competition, and it's impossible to recover them
    Anyways, my first machine learnign algorithim for a kaggle competition
"""
