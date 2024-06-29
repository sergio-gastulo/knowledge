# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 16:24:27 2023

@author: sgast
"""

import sys
import numpy as np 
import pandas as pd
from sklearn.tree import DecisionTreeClassifier as DTC
import sklearn.tree as tree

my_data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/drug200.csv', delimiter=",")
my_data.head()
a = list(my_data.columns)
a.remove('Drug')
X = my_data[a].values

#%%

from sklearn import preprocessing

label_encoder_sex = preprocessing.LabelEncoder()
label_encoder_sex.fit(['F','M'])
X[:,1] = label_encoder_sex.transform(X[:,1])

label_encoder_BP = preprocessing.LabelEncoder()
label_encoder_BP.fit(my_data.BP.unique())
X[:,2] = label_encoder_BP.transform(X[:,2])

label_encoder_Cholesterol = preprocessing.LabelEncoder()
label_encoder_Cholesterol.fit(my_data.Cholesterol.unique())
X[:,3] = label_encoder_Cholesterol.transform(X[:,3])

y = my_data.Drug.values

#%%

from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state=3)

#%%
drug_Tree = DTC(criterion = 'entropy', max_depth=4)

#%%

drug_Tree.fit(X_train,y_train)
pred_Tree = drug_Tree.predict(X_test)
from sklearn import metrics

print("DecisionTrees's Accuracy: ", 
      metrics.accuracy_score(y_test, pred_Tree))

#%%

import matplotlib.pyplot as plt
tree.plot_tree(drug_Tree)
plt.show()





