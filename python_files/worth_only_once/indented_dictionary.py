# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 19:57:11 2024

@author: sgast
"""

"""
    Este programa nos ayudará a copiar pegar los valores y apendizarlos a un 
    diccionario. 
    Toma la primera fila como cabeza del diccionario, y al resto de entradas 
    las almacena como valores pivoteados por la columna del diciconario
"""

if __name__ == '__main__':
    
    my_dict = {}
    cond = True
    while cond:
        lista = input()
        lista = lista.replace('\t','')
        lista = lista.replace('    ','')
        lista = lista.split('\n')
        
        my_dict[lista[0]] = lista[2:]
        
        if lista == 0:
            cond = False

#%%

import json 

filename = r'C:\Users\sgast\tania\category_excel_dict.txt'

with open(filename,'w') as f:
    json.dump(my_dict,f)

#%%
    
with open(filename, 'r') as f:
    loaded_dict = json.load(f)

print("Loaded dictionary:", loaded_dict)    
    
    
    
    
    
    