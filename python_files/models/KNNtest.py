# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 12:42:31 2023

@author: sgast
"""

from sklearn import preprocessing
import pandas as pd
import numpy as np
"""
    Inserte el link del dataframe a trabajar:
"""

df = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/teleCust1000t.csv')

"""
    Inserte la columna del dato a KNN analizar
"""

columna = 'custcat'


#%%

"""
    Preparando la data a analizar
"""

from sklearn.model_selection import train_test_split 

list_to_analize  = list(df.columns)
list_to_analize.remove(columna)
X = df[list_to_analize]
y = df[columna]
X = preprocessing.StandardScaler().fit(X).transform(X.astype(float))

#%%

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.20, random_state = 4)

#%%

"""
    Trabajaremos desde 1 a 10 KNN para poder escoger el mejor "k"
"""
import sklearn
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier as KNC

limit = 10
mean_acc = np.zeros(limit-1)
std_acc = np.zeros(limit-1)

for n in range(1,limit):
    nn = KNC(n_neighbors = n).fit(X_train,y_train)
    yhat = nn.predict(X_test)
    mean_acc[n-1] = metrics.accuracy_score(y_test, yhat)
    std_acc[n-1] = np.std(yhat==y_test)/np.sqrt(yhat.shape[0])


#%%
import matplotlib.pyplot as plt

plt.plot(range(1,limit),mean_acc,'g')
plt.fill_between(range(1,limit),mean_acc - 1 * std_acc,mean_acc + 1 * std_acc, alpha=0.10)
plt.fill_between(range(1,limit),mean_acc - 3 * std_acc,mean_acc + 3 * std_acc, alpha=0.10,color="green")
plt.legend(('Accuracy ', '+/- 1xstd','+/- 3xstd'))
plt.ylabel('Accuracy ')
plt.xlabel('Number of Neighbors (K)')
plt.tight_layout()
plt.show()

#%%

print( "The best accuracy was with", mean_acc.max(), "with k=", mean_acc.argmax()+1) 


