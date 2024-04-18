#!/bin/python3

import math
import os
import random
import re
import sys

"""
    Solution to https://www.hackerrank.com/challenges/matrix-script/problem?isFullScreen=false
"""
#Preprompted loading script
first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
#Preprompted loading script

"""
    My problem solving contribution
"""

#Transforming matrix into an actual matrix 
array_lista = list(map(lambda x: list(x), matrix))

#"Transposing" the matrix
text = ''
for i in range(m):
    text += ''.join([row[i] for row in array_lista])

#As ifs where not allowed, i needed to use the AttributeError when the re.search method fails
#As the only case where they fail is the only case when the string has no alphanumerical text
#I had to manipulate the indexes them to get an empty re.sub: not modifying the string at all
try:
    val1 = re.search(r'\w', text).start()  
except AttributeError:
    val1 = 0 
try:
    val2 = -re.search(r'\w',''.join(list(reversed(text)))).start()-1  
except AttributeError:
    val2 = 0 

#The final string
print(text[:val1]+re.sub(r'[^a-zA-Z0-9]+',' ',text[val1:val2])+text[val2:])