"""
    This code will generate a random csv simulating my accounting information.
    Of course, I cannot provide my accounting information because it is private, thats why a random csv has to be made
"""


import numpy as np
import numpy.random as rand
import os
import pandas as pd
from datetime import datetime as dt
from datetime import timedelta


def random_dates(first_day:str, last_day:str, size:int)->list:
    """
        This funciton generates a random array of dates
    """
    #first and last day must be in the following format
    #DAY-MONTH-YEAR
    l_day = dt.strptime(last_day,"%d-%m-%Y")
    f_day = dt.strptime(first_day,"%d-%m-%Y")

    delt = (l_day - f_day).days

    rd_dates = [
        (f_day + 
        timedelta(days = rand.randint(delt)))
        .strftime("%d-%m-%Y") 
        for _ in range(size)]

    return rd_dates


def random_accounting(first_day:str,last_day:str, size:int)->None:
    
    #header of the csv
    """
        Date: day of the expense or income
        Amount: amount of the expense or income
        Description: a small description to the transaction to register what it was exactly
        Category: the category it corresponds
    """
    list_of_headers = ['Date', 'Amount', 'Description', 'Category']


    #list of values of category
    list_of_category = [
        'BLIND',    # Money I recieve from people to offset my expenses
        'CASA',     # Money I spend at home, paying services 
        'CELULAR',  # Phone expenses
        'COM_VAR',  # Food i buy when hanging out or just a craving 
        'INGRESO',  # money i gain from work or effort
        'MENU',     # menu necessarily spend on my day to day
        'PASAJE',   # money to move on the country
        'PERSONAL', # money i spend on me
        'RECIBO',   # money i spend on me, monthly like spotify or netflix
        'VARIOS',   # expenses which idk how to label them
        ]
    
    #not my produest matrix, im really considering to avoid Description but the script resumen_cuentas works with it, so i cannot delete it
    #i will probably change the code using try except KeyError to check if the df has Decription on it or not
    #in case it does, eveything might remain the same
    #in coes it doesnt, then decription will have to be dropped from resumen_cuentas 
    data = np.transpose([
        random_dates(first_day=first_day, last_day=last_day, size = size),  #random dates generator
        rand.randint(100, size = size),                                     #random int for accounting track
        [None]*size,                                                        #the part idk how to deal with, ill figure it out later
        rand.choice(a = list_of_category, size = size)                      #choice of categories randomly
    ])

    # name of the file
    path = os.getcwd()
    filename = r'\accounting.csv'
    
    file_path = path+filename
    
    # #saving col names
    # with open(filename, 'w') as f:
    #     f.write(','.join(list_of_headers)+'\n')
    
    # #saving data into a csv as expected
    # with open(filename, 'a') as f:
    #     np.savetxt(f, data, delimiter = ',')

    #So, it seems numpy cannot handle nonnumerical matrices, we are forced to conver the data into a dataframe and exportit using tocsv
    pd.DataFrame(
        data, 
        columns=list_of_headers).to_csv(
            file_path, 
            index=False)

    os.system(f'notepad {file_path}')


if __name__ == '__main__':

    print("Prompt the dates in the following format: DD-MM-YYYY")
    first_day = input("Prompt the firstday to work with: ")
    last_day = input("Prompt the lastday to work with: ")
    size = int(input("size of the csv to deal with: "))

    random_accounting(first_day=first_day,last_day=last_day,size=size)

