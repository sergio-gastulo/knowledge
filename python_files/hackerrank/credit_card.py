# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 19:21:56 2024

@author: sgast

Solution tho the hackerrank problem
https://www.hackerrank.com/challenges/validating-credit-card-number/problem
"""

#%%

def grouped_in(s)->bool:
    s = s.split('-')
    boo = list(map(len,s))
    
    if boo == [4 for _ in range(4)] or len(s) == 1:
        return True

    else: 
        return False
    
#%%

def from0to9andhypen(s) -> bool:
    lista = [f'{_}' for _ in range(10)] + ['-']
    return all(list(map(lambda x: x in lista, list(s))))
    
#%%

def consecutive(s) -> bool:
    s = s.replace('-','')
    n = 16
    boolean = []
    for i in range(n-5):
        pivot = s[i:i+4]
        boolean.append(all(list(map( lambda x: x==pivot[0], pivot))))
    
    return(any(boolean))
    
#%%


def card_number_detector(card_number):
    
    #checks if first number is 4 5 or 6
    first_is456 = card_number[0] in ['4','5','6']
    
    #check if card number, regardless of its hypens, is of lenght 16
    is_16_long = len(card_number.replace("-","")) == 16
    
    #checks if only contains of digits from 0 to 9 and '-'
    #also cheks if there is another element different from the previous ones
    contains_weird_chars = from0to9andhypen(card_number)
    
    #checks if its grouped on group of 4x4 or 1
    is_grouped4x4 = grouped_in(card_number)

    #checks if the credit card has more than 4 consecutives
    four_consecutives = consecutive(card_number)

    boolean = [
        first_is456,
        is_16_long,
        is_grouped4x4,
        contains_weird_chars,
        not four_consecutives]
    
    if all(boolean):
        return "Valid"
    
    else:
        return "Invalid"
        
    
#%%
if __name__ == '__main__':
    
    for _ in range(int(input())):
        card_number = input()
        card_number_detector(card_number)
