# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 19:16:12 2024

@author: sgast
"""

import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt 
from numpy import divide as d
import requests
from bs4 import BeautifulSoup


def dolar_getter()->float:
    """
        This function queries the USD -> PEN exchange rate returning a float
    """

    #the page i'm taking the exchange rate
    URL = r"https://securex.pe"

    #requesting the url
    page = requests.get(URL)
    
    sopa = BeautifulSoup(page.content, "html.parser")
    
    #sopa.prettify() to webscrapp the page
    #finding the value i want
    results = sopa.find('div', class_ = 'col-md-5 col-xs-5 custom-col text-center')
    
    dollar_to_soles = float(results.find_all('span')[1].text)

    return dollar_to_soles


def personal_settings()->None:
    '''
        Dark mode on matplotlib
    '''
    plt.style.use('dark_background')
    plt.rcParams['font.family'] = 'monospace'  # Set font family
    plt.rcParams['font.size'] = 12  # Set font size


def dates_in_range(df:pd.DataFrame)->list:
    
    '''
        This function is responsible for creating a list of dates that are not found in the dataframe. 
    '''

    #first_date on the df    
    first_date = df.Date.min().date()
    #last_date on the df    
    last_date = df.Date.max().date()
    #day counting    
    days = (last_date - first_date).days
    #set of days from first date to last date
    full_list_of_days = {
        first_date + dt.timedelta(days = _) 
        for _ in range(days)}
    #days where there where monetary movements
    list_of_movements = set(df.Date.dt.date.unique())
    
    #returns the list of the days where there where no movements
    return list(full_list_of_days - list_of_movements)


def supreme_loading(path:str)->pd.DataFrame:
    '''
        This function is responsible for uploading the CSV into a dataframe, with pre-filled data, hence the importance of the previous function. 
        Additionally, it is responsible for obtaining the columns year, month, and day.
    '''
    #just loading the csv
    df = pd.read_csv(
        path,
        index_col= None)
    
    #converting Date into datetime format
    df.Date = pd.to_datetime(
        df.Date,
        dayfirst=True,
        format = '%d-%m-%Y')

    #Creating NULL values to append in the dataframe, just for analisys porpouses    
    value_dict = {
        'Date': dates_in_range(df),
        'Amount': 0,
        'Description': 'Null values',
        'Category': 'NULL'
        }
    
    #df_ghost stands for the null values
    df_ghost = pd.DataFrame.from_dict(value_dict)
    #concatenating them
    df = pd.concat([df,df_ghost], ignore_index=True)
    
    
    #It seems i was uploading datetime types twice instead of just uploading them after the merge
    df.Date = pd.to_datetime(
        df.Date,
        format = "%d-%m-%Y")
    
    df.Category = df.Category.str.upper()

    #Getting the needed columns for grouping
    df['Month'] = df.Date.dt.strftime("%b")
    df['Year'] = df.Date.dt.year
    df['Day'] = df.Date.dt.day
    
    def dolar_converter_pandas(df_pandas:pd.DataFrame)->None:
        dol_value = dolar_getter()
        df_pandas.loc[df_pandas['Category'] == 'USD_INC', 'Amount'] *= dol_value
        df_pandas.loc[df_pandas['Category'] == 'USD_INC', 'Category'] = 'INGRESO'
    
    dolar_converter_pandas(df)

    return df


def col_periodo(df:pd.DataFrame)->pd.DataFrame:
    '''
        What do we want to do?
        What my Excel used to do, extracting summaries by categories and plotting them. I think I could create a histogram by categories, a comparison between total expenses and total income, especially income per month versus expenses per month.

        To achieve this, we will create a function that groups my data by period, almost artificially.
    '''
    
    #grouping by period
    df_per = (df
         #Dropping description cause is unnecessary to analysis porpouses
         .drop(['Description','Date'], axis=1) 
         #Grouping by
         .groupby(['Year', 'Month','Category'])
         .sum()
         .reset_index()
    )
    
    #PERIOD = MONTH-YEAR
    df_per['Periodo'] = (
        df_per.Month.astype(str) 
        +'-' + 
        df_per.Year.astype(str))

    #We only want period, is unnecessary the other columns once we are done with PERIOD column    
    df_per.drop(['Year','Month','Day'], inplace = True, axis = 1)
    
    return df_per


def ploteo_de_barras_vs_periodo(
        df_per:pd.DataFrame,
        periodo_to_analyze:list)->None:
    '''
        This function generates a plot of expenses per period grouped by category.
    '''

    #iterating over each period to analyze requested by the user
    for i in periodo_to_analyze:
        filtered = (df_per[
            (df_per.Periodo == i)
            &
            #We dont want to analyze the values on Category that are INCOMES
            (df_per.Category != 'INGRESO')
            &
            #We dont want to analyze the values on Category that are NULL
            (df_per.Category != 'NULL')
            ])
        
        #BLIND def: Money I receive from people to offset my expenses.
        #As it is received, it has to be negative to be added to my expenses.
        filtered.loc[filtered.Category=='BLIND','Amount'] *=-1

        #Getting the sum of all INCOMES from the same requested PERIOD
        #I guess this is not optimal, ill check it later
        ingreso = (df_per[
            (df_per.Periodo == i) 
            &
            (df_per.Category == 'INGRESO')
            ]
            .Amount.sum())
        
        #All the EXPENSES made on the iterated PERIOD
        gasto = filtered.Amount.sum()
        
        #Plotting the barplot, category vs amount
        #Questions answered: which are the CATEGORIES where we expend money the most 
        filtered.plot(
            x = 'Category',
            y = 'Amount',
            kind = 'bar',
            color = (0.49, 0.31, 1),
            legend = False
            )
        
        #Decorator: it writes over each bar the amount per each category
        #iterates over the filtered amounts on the bar
        for j, value in enumerate(filtered.Amount):
            plt.text(
                #x value = order of the category on the plot
                j,
                #y value = the value of the summed money
                value, 
                #the actual text: the actual value of the amounts summed by category properly formated
                f'S/{value:.2f}', 
                #how to be shown:
                ha='center', 
                va='bottom'
                )

        #Another decorator:
        #It shows the EXPENSES (Gastos)
        #It shows the INCOMES (Ingresos)
        #And it shows their difference (Diferencia)

        plt.text(
            #x value of the text: we want it on the left
            0,
            #y value of the text :we want it on the top
            filtered.Amount.max(),
            #the value of the actual text
            f' Ingresos: S/{ingreso:.2f} \n Gastos: S/{gasto:.2f} \n Diferencia: S/{ingreso-gasto:.2f}',
            #where, wrt the pre established x,y values
            ha = 'left',
            va = 'top',
            #color of the block printed on the plot
            bbox=dict(
                facecolor='black', 
                edgecolor=(0.49, 0.31, 1),
                linewidth=2)
            )
        
        #names for the plot
        plt.title(f'Periodo {i}')
        plt.xticks(rotation=45)
        plt.show()


def bar_plot_grouped_days(df:pd.DataFrame)->None:
    """
        This funciton generates a barplot of the expenses per day, it does not show any interesting result, but it works
    """
    
    #Defining the dataframe to plot groped per day, but only by its num_day, and only taking into consideration the values which are less than 250.
    #The main idea was to track a pattern on which days im wasting money the most, but it did not work as expected
    df_to_plot_daily = (df
     [
      (df.Category!='INGRESO')
      &
      (df.Category != 'BLIND')
      &
      (df.Amount<=150)
     ]
     .groupby('Day')['Amount']
     .sum()
     .reset_index())
    
    #creating the plot
    plt.figure()
    plt.bar(
        df_to_plot_daily.Day.astype(str),
        df_to_plot_daily.Amount,
        color = (0.49, 0.31, 1)
        )
    
    #Addind the decorators to the plot
    for j, value in enumerate(
            df_to_plot_daily.Amount
            ):
        plt.text(
            j, 
            value, 
            f'{value:.0f}', 
            ha='center', 
            va='bottom'
            )
        
    #More decorators
    plt.title('''
    Gastos no exageradamente grandes (menores a 150), agrupados por Day
              ''')
    plt.xlabel('Dia')
    plt.ylabel('Cantidad')
    plt.show()


def sort_month_year(month_year:str)-> tuple:
    """
        This function does the following
        PERIOD (MONTH-YEAR) -> YEAR(int), number of month
        For sorting purposes, clearly 
    """
    #spliting the str
    month, year = month_year.split('-')
    #creating the order of the dictionary
    month_order = {
        'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 
        'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 
        'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
    }
    month_num = month_order[month]
    return (int(year), month_num)


def acumulados_por_periodos(df_per:pd.DataFrame)->None:
    '''
        Now we want to know how much we are spending per month. 
        We want to see accumulated income per month and accumulated expenses per month. 
        I think I'll use `df_per` because it's already accumulated by periods.

        This function does exactly the requested work: plots expenses per MONTH-YEAR=:PERIOD.
    '''
    
    #coping the dataframe so its not modify, since df_per will be used in the ongoing
    df_local = df_per.copy()

    #expenses (neither ingresos nor blinds) should be always negative:
    df_local.loc[
            (df_local.Category!='INGRESO') & (df_local.Category!='BLIND'),'Amount']*=-1
    
    #dataframe of expenses
    df_gastos = {
    
        'sin_ingreso':(df_local[
            (df_local.Category!='INGRESO') & (df_local.Category != 'BLIND')
            ])
            .groupby(['Periodo'])['Amount'].sum()
            .sort_index(key= lambda x: x.map(sort_month_year)),
        
        'con_ingreso': df_local.groupby(['Periodo'])['Amount'].sum().sort_index(key= lambda x: x.map(sort_month_year)),

        'solo_ingreso': (df_local[
            (df_local.Category=='INGRESO') | (df_local.Category == 'BLIND')]
            .groupby(['Periodo'])['Amount'].sum()
            .sort_index(key= lambda x: x.map(sort_month_year)))
        }
    
    #Creating the figure and axis where our plot will be created, is necessary to plot both graphs on the same plot to visualize their difference
    fig, ax = plt.subplots()
    
    #without incomes, with incomes and incomes only
    cat_values = ['sin_ingreso','con_ingreso','solo_ingreso']

    #colors to match the plot
    colors = [(0.573, 0.573, 1),(0.259, 0.91, 0.525),(0.573, 0.573, 1)]
    
    #the plot itself:
    for i, cat_val in enumerate(cat_values):
        ax.plot(df_gastos[cat_val],
                linewidth = 2.5,
                marker = 'o',
                label = f'gastos {cat_val}',
                color = colors[i])
        
        #some markers:
        for j, value in enumerate(df_gastos[cat_val].values):
            plt.text(j, value, 
                f'{value:.1f}', 
                ha='center', va='bottom'
                )
    ax.set_xlabel('Periodo')
    ax.set_ylabel('Montos')
    ax.set_title('Movimiento de los gastos agrupados por periodo a través del tiempo')
    plt.legend()
    plt.show()


def evolucion_de_gastos_vs_tiempo(df:pd.DataFrame)->None:
    '''
        This function plots the evolution of expenses over time. 
        Obviously, INCOME is excluded from the account.
    '''

    #BLINDS as always are negative
    df.loc[df.Category == 'BLIND','Amount'] *= -1 
    
    filtered_data = (df[
        #INCOME excluded
        (df.Category!='INGRESO') 
        #in case we want to omit HOUSE, just uncomment the following lines
        # & 
        # (df.Category!= 'CASA')
        ]
        .groupby('Date')['Amount']
        .sum()
        .reset_index())
    
    #usual plot
    plt.figure()
    plt.plot(
        filtered_data.Date,
        filtered_data.Amount,
        color = (0.545, 0.392, 0.929),
        linewidth = 1,
        marker = 'o',
        markersize = 2
             )
    
    '''
        The following decorator is especial and deserves to be highlighted.
        
        First, it filters the top 10 values of the plot.
        Then, it shows their position on the x and y axis using gridlines.
        Also, it plots their value on each point, on a suitable location.
    '''

    #Sorting the first then values
    #(not optimal though, sorting, heading and getting values from the query twice could take too much time than expected, ill check it later)
    #And getting its x and y value
    for j, value in zip(
            (filtered_data
             .sort_values(
                 by = 'Amount',
                 ascending = False)
             .head(10)
             .values[:,0])
            ,
            filtered_data
            .sort_values(
                by = 'Amount',
                ascending = False)
            .head(10)
            .values[:,1]):
        #Adding the value of each dot on the plot
        plt.text(
            j, 
            value, 
            f'{value:.1f}', 
            ha='center', 
            va='bottom'
            )
        #the requested highlighting on the x and y axis
        plt.vlines(j, 0, value, 
                   linestyle=':', 
                   color='white',
                   linewidth=0.75)
        plt.hlines(value, filtered_data.Date.min(), j, 
                    linestyle=':', 
                    color='white',
                    linewidth=0.75)
    
    #Decorators for the plot
    plt.title('Evolucion de SOLO GASTOS con el tiempo')
    plt.xlabel('Fechas')
    plt.xlabel('Gastos puntuales')
    plt.show()


def acumulados_por_periodos_y_categoria(df_per:pd.DataFrame)->None:
    """
    This function does exactly what the above funciton does. The main difference is it plots only expenses on logaritmic scale
    and per Category
    """
    df_local = df_per.copy().sort_values(by = 'Periodo', key= lambda x: x.map(sort_month_year))
    #only expenses:
    df_local = df_local[(df_local.Category!='INGRESO') & (df_local.Category!='BLIND') & (df_local.Category!='NULL')]
    
    #list of categories present on df_per
    category_list = df_local.Category.unique().tolist()
    
    #colors from green to blue, asked chatgpt for this, btw it does not go to blue lol
    colors_2 = [
        '#00FF00',  # Green
        '#1AFF33', '#33FF66', '#4DFF99', '#66FFCC', '#80FFFF', '#99FFFF', '#B3FFFF', '#CCFFFF', '#E6FFFF', '#FFFFFF',
        '#0000FF'   # Blue
    ]

    #creating the plot
    fig, ax = plt.subplots()

    #iterating over the value of the categories.
    #Also, using enumerate to iterate at pair with category list
    for i,cat in enumerate(category_list):
        ax.plot(
            df_local[df_local.Category==cat].Periodo,
            df_local[df_local.Category==cat].Amount,
            label = f'Gastos asociados a {cat}',
            linewidth = 2.5,
            marker = 'o',
            c = colors_2[i]
        )

    #scaling to log because some expenses overflow the other ones 
    ax.set_yscale('log')
    ax.set_xlabel('Periodo')
    ax.set_ylabel('Cantidad')
    ax.set_title('Movimiento de los gastos agrupados por periodo a través del tiempo')
    plt.legend()
    plt.show()


#######################  DISCLAIMER  ###############################
#######################  DISCLAIMER  ###############################
#######################  DISCLAIMER  ###############################
#######################  DISCLAIMER  ###############################
#######################  DISCLAIMER  ###############################


"""

This thoughts are part of the analysis, so I considered they were necessary to understand the behaviour of the following function.
I did my best to not delete it from here and also translating it because these comments where in Spanish. 

    --If we evenly distribute all income across the days that have passed, we can see how much we save on average per day.

So the idea in the previous line was: if i dont spend money on a day, im saving money actually, so its worth to consider the dates where expenses are not made, in order to see how much i have been saving lately 
    
    --TASK:
        --Find out properly how the heck we add an income average to expenses. 
        --View a detailed cumulative table. 
        --Wonder if the average should be considered with spending days or all days, if the latter is the answer, make sure to add entire rows for dates that don't record income, fill with zeros, and create a new category called NULL.

    --DISCLAIMER:
        --It's too memory-intensive; find a better method to register dates with empty values.

Indeed, it is a lot of memory, especially if we had more data. However, it was the only method I came up with, that's why you can see its already implemented in the first lines of the code

    --DISCLAIMER 2:
        --I'd also like to know how many days I haven't spent anything.
        --Id like to know how many times I've "stayed home peacefully, saving."

There is where the idea of analyzing the days where I spent time at home poped up.

First of all, we needed to see whether our hypotesis was correct and indeed it was.
    
    --Here it's tested that there are days with only income. 
    --Hence, there are days with ridiculously large figures in the previous graphs.
"""


def checker(df:pd.DataFrame)->None:
    
    """
        This function will help us to compare the days where there were no EXPENSES but also no INCOMES.
    """

    #Grouping per Date but without INCOMES
    df_alterada_con_promedio = (
        df[
           (df.Category != 'INGRESO')
           ]
        .groupby('Date')['Amount']
        .sum()
        .reset_index()
        )
    
    #set of dates to test
    conjunto_prueba = (
        #set of days present in the dataframe
        set(df.Date.dt.date) 
        - 
        #set of dates where INCOMES was not the only CATEGORY present, this works to delete the days with incomes ONLY  
        set(df_alterada_con_promedio.Date.dt.date)
        )

    #I dont remember what this did, i will debug it later.
    for fecha in list(conjunto_prueba):
        print(
            df[
                (df.Month == fecha.strftime("%b"))
                &
                (df.Day == fecha.strftime("%d") )
                ])
        print('\n\n ****************** \n\n')


'''
    --It seems conjunto_prueba is the indicated to do the job of shadow dataframe with values to append:
    
        value_dict = {
            'Date': list(conjunto_prueba),
            'Amount': 0,
            'Description': 'Null values',
            'Category': 'NULL'
            }

        df_ghost = pd.DataFrame.from_dict(value_dict)

        print(df_ghost.head)


    --No, the test set is not adequate because it doesn't contain dates without any transactions. Updating the test set.
    
    --We will create a function that collects the list of dates from the first date that appears in the dataframe until the last.
    
    --COMMENT: DONE, when loading the data, we added ghost rows to see the data.
    
    --We only need to plot. 

Thats why at the begining of the script youll se a pdshadow, now you know why it was necesssary.
'''


#######################  DISCLAIMER  ###############################
#######################  DISCLAIMER  ###############################
#######################  DISCLAIMER  ###############################
#######################  DISCLAIMER  ###############################
#######################  DISCLAIMER  ###############################


def accumulative_earnings(df:pd.DataFrame)->None:
    """
        This, as it name says, is a function which will plot the requested values:
        To see how the money changes taking into consideration the amount gained per day with a saving percentage
        It also helps to dimensionate the impact of the expenses made per day
    """

    #Saving percentage
    # porcentaje_ahorro = 0.15
    
    #No percentage:
    porcentaje_ahorro = 0.0
    #almacenating the difference of the days to divide 
    diferencia_dias = len(set(df.Date.dt.date))
    
    #mean of incomes per day: (1-%saving)incomes/days 
    promedio_ingresos_dia = d(
        df[
           df.Category == 'INGRESO'
           ]['Amount']
        .sum()*(1-porcentaje_ahorro), 
        diferencia_dias)
    
    #creation of the dataframe which will almacenate the days with income per day
    df_alterada_con_promedio = (
        df[
           (df.Category != 'INGRESO')
           ]
        .groupby('Date')['Amount']
        .sum()
        .reset_index()
        )
    
    #as every aspect of the dataframe are just expenses, we multiply the column by -1 to track a NEGATIVE behaviour
    df_alterada_con_promedio.loc[:,'Amount'] *= -1
    #also, we add the mean of incomes per day
    df_alterada_con_promedio.loc[:,'Amount'] += promedio_ingresos_dia 
    #a cumsum, which will show how the days with income behaves
    df_alterada_con_promedio['Cumsum'] = df_alterada_con_promedio.Amount.cumsum()
    
    #without INCOMES and HOUSE expenses, so we can track their behaviour under the main graph, youll check it later
    filtered_data = (df[
        (df.Category!='INGRESO') 
        # & 
        # (df.Category!= 'CASA')
        ]
        .groupby('Date')['Amount']
        .sum()
        .reset_index())
    
    #plt creation
    fig, ax = plt.subplots()
    
    #main plot
    ax.plot(
        df_alterada_con_promedio.Date,
        df_alterada_con_promedio.Cumsum,
        color = (0.545, 0.392, 0.929),
        linewidth = 1.5,
        label = 'Cumulative sums of GASTOS'
        )
    
    #under plot
    ax.plot(
        filtered_data.Date,
        filtered_data.Amount,
        color = (0.298, 0.831, 0.769),
        linewidth = 1.5,
        #including HOUSE should not be there... ill check it later 
        label = 'GASTOS, including CASA'
             )
    
    '''
        Labelling top 20 gastos
    '''
    
    #selecting the top 20 expenses
    values_to_grid = 20
    pseudo = filtered_data.sort_values(
        by = 'Amount',
        ascending = False
        #selecting the top 20 expenses
        ).head(values_to_grid)
    
    #x,y values of the main dots in the plot
    for j, value in zip(pseudo.values[:,0],pseudo.values[:,1]):
        
        #lines decorator:
        #goes from the day to the top of the plot at the bottom to the bottom of the top plot
        #it creates a type of duality which is really worth to see
        plt.vlines(j, value, df_alterada_con_promedio[
            df_alterada_con_promedio.Date==j
            ].Cumsum.sum(), 
                    linestyle=':', 
                    color='white',
                    linewidth=0.75)
        
        #value decorator
        plt.text(
            j, 
            df_alterada_con_promedio[
                df_alterada_con_promedio.Date==j
                ].Cumsum.sum(), 
            f'{value:.1f}', 
            ha='center', 
            va='bottom',
            fontsize = 10
            )
    banco_de_la_nacion_6_3_2024 = 24_191.51
    ahorro = df_alterada_con_promedio.Cumsum.iloc[-1] + banco_de_la_nacion_6_3_2024
    ahorro_text = f'S/.{ahorro:.2f}'
    #decorators for plotting 
    ax.set_title(f'Ingresos acumulados y gastos. Ahorro: {ahorro_text}')
    ax.set_xlabel('Fechas')
    ax.set_ylabel('Ingresos divididos - gastos')
    ax.legend()
    plt.show()


if __name__ == '__main__':
    
    #path of the csv
    path = r'c:\Users\sgast\Documents_personal\excel\cuentas.csv'
    
    #personal settings to mpl
    personal_settings()

    #loading the dataframe
    df = supreme_loading(path)
    
    #grouped per periods
    df_per = col_periodo(df)
    
    #which periods would be worth to analyze
    periodo_to_analyze = ['Apr-2024','May-2024','Jun-2024']
    
    #plotting
    #not worth it, it works though
    # ploteo_de_barras_vs_periodo(df_per, periodo_to_analyze)
    
    # as this plot was not worh, we are not doing showing it, but the function works so...
    # bar_plot_grouped_days(df)

    #plotting
    acumulados_por_periodos(df_per)
    acumulados_por_periodos_y_categoria(df_per)
    
    #plotting 
    evolucion_de_gastos_vs_tiempo(df)
    
    #plotting
    accumulative_earnings(df)

    dolar = dolar_getter()
    print("Dolar value: ", dolar)

    print("Perdido por tio: ",3000-dolar*800)


