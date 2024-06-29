    # -*- coding: utf-8 -*-

"""
Created on Wed Jan  3 14:03:27 2024

@author: sgast
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FC
from matplotlib.figure import Figure

fig = Figure()
z = FC(fig)
x = np.random.randn(10_000)
ax = fig.add_subplot(111)
ax.hist(x,100) #100 bins actually
ax.set_title('Normal distribution')
fig.savefig('hola')

#%%

x = np.random.randn(10_000)
plt.hist(x,100)
plt.title(r'HOLA $\mu = 0$')
plt.show()

#%%

plt.plot(5,5,'o')
plt.show()

#%%

import pandas as pd

URL = r'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx'
df_can = pd.read_excel(
    URL,
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)
print('Data downloaded and read into a dataframe!')

#%%
df_can.drop(
    ['AREA','REG','DEV','Type','Coverage'], 
    axis=1, 
    inplace=True)

df_can.rename(
    columns={
        'OdName':'Country', 
        'AreaName':'Continent', 
        'RegName':'Region'}, 
    inplace=True)
df_can.columns

#%%

df_can.set_index('Country', inplace=True)
df_can.columns = list(map(str, df_can.columns))

#%%

import matplotlib as mpl
print(mpl.__version__)

#%%

print(plt.style.available)
mpl.style.use(['ggplot']) 
# optional: for ggplot-like style

#%%
years = np.array(range(1980,2013)).astype(str)
haiti = df_can.loc['Haiti', years]
haiti.plot()


#%%

haiti.index = haiti.index.map(int) # let's change the index values of Haiti to type integer for plotting
haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

plt.show() # need this line to show the updates made to the figure

#%%

haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

# annotate the 2010 Earthquake. 
# syntax: plt.text(x, y, label)
plt.text(2000, 6000, '2010 Earthquake') # see note below

plt.show() 

#%%
years = list(map(str, range(1980, 2014)))

df_CI = df_can.loc[['China','India'],years]
df_CI = df_CI.transpose()
#%%
df_CI.index = df_CI.index.map(int)
df_CI.plot(kind = 'line')
plt.title('ZZ')
plt.ylabel('ASD')
plt.xlabel('x')
plt.show()


#%%

df_can['Total'] = df_can[years].sum(axis = 1)
df_can.sort_values(
    ['Total'],
    ascending = False,
    axis =0,
    inplace = True)

#%%

df_top5 = df_can.head()
df_top5 = df_top5[years].transpose()

#%%

df_top5.plot(kind='area', 
             alpha = 0.45,  # 0 - 1, default value alpha = 0.5
             stacked=False,
             figsize=(20, 10))

plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.show()

#%%

df_2013 = df_can['2013'].transpose()

#%%

df_can['2013'].plot(kind = 'hist')

plt.title('Histogram of immigrators from 195 countries in 2013')
plt.ylabel('Number of countries')
plt.xlabel('Number of immigrants')

plt.show()

#%%

count, bin_edges = np.histogram(df_can['2013'])

df_can['2013'].plot(
    kind = 'hist',
    xticks = bin_edges)

plt.title('Histogram of immigrators from 195 countries in 2013')
plt.ylabel('Number of countries')
plt.xlabel('Number of immigrants')

plt.show()

#%%

df_iceland = df_can.loc['Iceland',years]

df_iceland.plot(kind='bar')

plt.title('Icelandic immigrants from 1980 to 2013')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

plt.show()

#%%

df_t = df_can.loc[['Denmark', 'Norway', 'Sweden'], years].transpose()

#%%

# let's get the x-tick values
count, bin_edges = np.histogram(df_t, 15)

# un-stacked histogram
df_t.plot(kind ='hist', 
          figsize=(10, 6),
          bins=15,
          alpha=1,
          xticks=bin_edges,
          color=[
              'red', 
              'black', 
              'mediumseagreen']
         )

plt.title('Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013')
plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants')

plt.show()

#%%

count, bin_edges = np.histogram(df_t, 15)
xmin = bin_edges[0] - 10   #  first bin value is 31.0, adding buffer of 10 for aesthetic purposes 
xmax = bin_edges[-1] + 10  #  last bin value is 308.0, adding buffer of 10 for aesthetic purposes

# stacked Histogram
df_t.plot(kind='hist',
          figsize=(10, 6), 
          bins=15,
          xticks=bin_edges,
          color=['coral', 'darkslateblue', 'mediumseagreen'],
          stacked=True,
          xlim=(xmin, xmax)
         )

plt.title('Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013')
plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants') 

plt.show()

#%%

df_iceland.plot(kind='bar', figsize=(10, 6), rot=90)  # rotate the xticks(labelled points on x-axis) by 90 degrees

plt.xlabel('Year')
plt.ylabel('Number of Immigrants')
plt.title('Icelandic Immigrants to Canada from 1980 to 2013')

# Annotate arrow
plt.annotate('',  # s: str. Will leave it blank for no text
             xy=(32, 70),  # place head of the arrow at point (year 2012 , pop 70)
             xytext=(28, 20),  # place base of the arrow at point (year 2008 , pop 20)
             xycoords='data',  # will use the coordinate system of the object being annotated
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='blue', lw=2)
             )

plt.show()

# Annotate Text
plt.annotate('2008 - 2011 Financial Crisis',  # text to display
             xy=(28, 30),  # start the text at at point (year 2008 , pop 30)
             rotation=72.5,  # based on trial and error to match the arrow
             va='bottom',  # want the text to be vertically 'bottom' aligned
             ha='left',  # want the text to be horizontally 'left' algned.
             )

plt.show()

#%%

df_continents = df_can.groupby(
    'Continent',
    axis = 0).sum()

#%%

# autopct create %, start angle represent starting point
df_continents['Total'].plot(kind='pie',
                            figsize=(5, 6),
                            autopct='%1.1f%%', # add in percentages
                            startangle=90,     # start angle 90° (Africa)
                            shadow=True,       # add shadow      
                            )

plt.title('Immigration to Canada by Continent [1980 - 2013]')
plt.axis('equal') # Sets the pie chart to look like a circle.

plt.show()

#%%

colors_list = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'pink']
explode_list = [0.1, 0, 0, 0, 0.1, 0.1] # ratio for each continent with which to offset each wedge.


df_continents['Total'].plot(kind='pie',
                            autopct='%1.1f%%', 
                            startangle=90,    
                            shadow=True,       
                            labels=None,         # turn off labels on pie chart
                            pctdistance=1.12,    # the ratio between the center of each pie slice and the start of the text generated by autopct 
                            colors=colors_list,  # add custom colors
                            explode=explode_list # 'explode' lowest 3 continents
                            )
plt.title('Immigration to Canada by Continent [1980 - 2013]', y=1.12) 
plt.axis('equal') 
plt.legend(labels=df_continents.index, loc='upper left') 
plt.show()
    


#%%

df_japan = df_can.loc[['Japan'], years].transpose()
df_japan.plot(kind='box', figsize=(8, 6))

plt.title('Box plot of Japanese Immigrants from 1980 - 2013')
plt.ylabel('Number of Immigrants')

plt.show()
#%%

df_CI.plot(
    kind='box',
    vert=False)
plt.title('China vs India version lmao')
plt.show()

#%%

fig = plt.figure()
ax0 = fig.add_subplot(1,2,1)
ax1 = fig.add_subplot(1,2,2)
df_CI.plot(kind='box',vert=False,ax = ax0)
ax0.set_title('First plot')
ax0.set_xlabel('Number of immigrants')
ax0.set_ylabel('Countries')

df_CI.plot(kind='line', ax=ax1) # add to subplot 2
ax1.set_title ('Line Plots of Immigrants from China and India (1980 - 2013)')
ax1.set_ylabel('Number of Immigrants')
ax1.set_xlabel('Years')

plt.show()

#%%

df_top15 = df_can.head(15)
matrix_decades = np.array(
    range(1980,2010))
matrix_decades = matrix_decades.reshape((3,10)).astype(str)

#%%

df_80s = df_top15.loc[:,matrix_decades[0]].sum(axis=1)
df_90s = df_top15.loc[:,matrix_decades[1]].sum(axis=1)
df_00s = df_top15.loc[:,matrix_decades[2]].sum(axis=1)

new_df =  pd.DataFrame({
    '1980s':df_80s,
    '1990s':df_90s,
    '2000s':df_00s,
    })

new_df.head()

#%%

new_df.plot(vert = False, kind='box')
plt.title('ASASDASDASS')
plt.show()

#%%

df_tot = pd.DataFrame(
    df_can[years].sum(axis = 0))

df_tot.index = map(int,df_tot.index)
df_tot.reset_index(inplace=True)
df_tot.columns = ['year','total']


#%%
df_tot.plot(
    kind='scatter',
    x = 'year',
    y ='total',
    color = 'darkblue')

plt.title('Total immigrant population to canada from 1980 to 2013')
plt.xlabel('zzzz')
plt.ylabel('zzzzz')

#%%

x = df_tot['year']
y = df_tot['total']

fit = np.polyfit(
    x,
    y,
    deg = 1)

df_tot.plot(
    kind='scatter', 
    x='year',
    figsize=(10, 6),
    y='total', 
    color='darkblue')

plt.title('Total Immigration to Canada from 1980 - 2013')
plt.xlabel('Year')
plt.ylabel('Number of Immigrants')

# plot line of best fit
plt.plot(x, fit[0] * x + fit[1], color='red') # recall that x is the Years
plt.annotate('y={0:.0f} x + {1:.0f}'.format(fit[0], fit[1]), xy=(2000, 150000))

plt.show()

# print out the line of best fit
'No. Immigrants = {0:.0f} * Year + {1:.0f}'.format(fit[0], fit[1]) 

#%%

df_countries = df_can.loc[['Denmark','Norway','Sweden'],years].transpose()
df_total = pd.DataFrame(
    df_countries.sum(axis = 1))
df_total.reset_index(inplace = True)
df_total.columns = ['year','total']
df_total.year = df_total.year.astype(int)

#%%

df_total.plot(
    kind='scatter',
    x = 'year',
    y = 'total',
    color = 'darkblue')

#%%


df_can_t = df_can[years].transpose()
df_can_t.index = map(int, df_can_t.index)
df_can_t.index.name = 'Year'
df_can_t.reset_index(inplace=True)

# normalize Brazil data
norm_brazil = (df_can_t['Brazil'] - df_can_t['Brazil'].min()) / (df_can_t['Brazil'].max() - df_can_t['Brazil'].min())

# normalize Argentina data
norm_argentina = (df_can_t['Argentina'] - df_can_t['Argentina'].min()) / (df_can_t['Argentina'].max() - df_can_t['Argentina'].min())

#%%
# Brazil
ax0 = df_can_t.plot(kind='scatter',
                    x='Year',
                    y='Brazil',
                    alpha=0.5,  # transparency
                    color='green',
                    s=norm_brazil * 500 + 100,  # pass in weights 
                    xlim=(1975, 2015)
                    )

# Argentina
ax1 = df_can_t.plot(kind='scatter',
                    x='Year',
                    y='Argentina',
                    alpha=0.5,
                    color="blue",
                    s=norm_argentina * 500 + 100,
                    ax=ax0
                    )

ax0.set_ylabel('Number of Immigrants')
ax0.set_title('Immigration from Brazil and Argentina from 1980 to 2013')
ax0.legend(['Brazil', 'Argentina'], loc='upper left', fontsize='x-large')

#%% WAFFLE FUNCION

df_dsn = df_can.loc[['Denmark', 'Norway', 'Sweden'], :]
# compute the proportion of each category with respect to the total
total_values = df_dsn['Total'].sum()
category_proportions = df_dsn['Total'] / total_values
width = 40 # width of chart
height = 10 # height of chart
total_num_tiles = width * height # total number of tiles
tiles_per_category = (category_proportions * total_num_tiles).round().astype(int)

#%%

waffle_chart = np.zeros((height,width),dtype = np.uint)

# define indices to loop through waffle chart
category_index = 0
tile_index = 0

# populate the waffle chart
for col in range(width):
    for row in range(height):
        tile_index += 1

        # if the number of tiles populated for the current category is equal to its corresponding allocated tiles...
        if tile_index > sum(tiles_per_category[0:category_index]):
            # ...proceed to the next category
            category_index += 1       
            
        # set the class value to an integer, which increases with class
        waffle_chart[row, col] = category_index

#%%

# instantiate a new figure object
fig = plt.figure()

# use matshow to display the waffle chart
colormap = plt.cm.coolwarm
plt.matshow(waffle_chart, cmap=colormap)
plt.colorbar()
plt.show()

#%%

# instantiate a new figure object
fig = plt.figure()

# use matshow to display the waffle chart
colormap = plt.cm.coolwarm
plt.matshow(waffle_chart, cmap=colormap)
plt.colorbar()

# get the axis
ax = plt.gca()

# set minor ticks
ax.set_xticks(np.arange(-.5, (width), 1), minor=True)
ax.set_yticks(np.arange(-.5, (height), 1), minor=True)
    
# add gridlines based on minor ticks
ax.grid(which='minor', color='w', linestyle='-', linewidth=2)

plt.xticks([])
plt.yticks([])
plt.show()

#%%

import matplotlib.patches as mpatches

# instantiate a new figure object
fig = plt.figure()

# use matshow to display the waffle chart
colormap = plt.cm.coolwarm
plt.matshow(waffle_chart, cmap=colormap)
plt.colorbar()

# get the axis
ax = plt.gca()

# set minor ticks
ax.set_xticks(np.arange(-.5, (width), 1), minor=True)
ax.set_yticks(np.arange(-.5, (height), 1), minor=True)
    
# add gridlines based on minor ticks
ax.grid(which='minor', color='w', linestyle='-', linewidth=2)

plt.xticks([])
plt.yticks([])

# compute cumulative sum of individual categories to match color schemes between chart and legend
values_cumsum = np.cumsum(df_dsn['Total'])
total_values = values_cumsum[len(values_cumsum) - 1]

# create legend
legend_handles = []
for i, category in enumerate(df_dsn.index.values):
    label_str = category + ' (' + str(df_dsn['Total'][i]) + ')'
    color_val = colormap(float(values_cumsum[i])/total_values)
    legend_handles.append(mpatches.Patch(color=color_val, label=label_str))

# add legend to chart
plt.legend(handles=legend_handles,
           loc='lower center', 
           ncol=len(df_dsn.index.values),
           bbox_to_anchor=(0., -0.2, 0.95, .1)
          )
plt.show()

#%%FUNCTION, FINALLYYY RAAAAAAAAAAAAAAAH

def create_waffle_chart(categories, values, height, width, colormap, value_sign=''):

    # compute the proportion of each category with respect to the total
    total_values = sum(values)
    category_proportions = [(float(value) / total_values) for value in values]

    # compute the total number of tiles
    total_num_tiles = width * height # total number of tiles
    print ('Total number of tiles is', total_num_tiles)
    
    # compute the number of tiles for each catagory
    tiles_per_category = [round(proportion * total_num_tiles) for proportion in category_proportions]

    # print out number of tiles per category
    for i, tiles in enumerate(tiles_per_category):
        print (df_dsn.index.values[i] + ': ' + str(tiles))
    
    # initialize the waffle chart as an empty matrix
    waffle_chart = np.zeros((height, width))

    # define indices to loop through waffle chart
    category_index = 0
    tile_index = 0

    # populate the waffle chart
    for col in range(width):
        for row in range(height):
            tile_index += 1

            # if the number of tiles populated for the current category 
            # is equal to its corresponding allocated tiles...
            if tile_index > sum(tiles_per_category[0:category_index]):
                # ...proceed to the next category
                category_index += 1       
            
            # set the class value to an integer, which increases with class
            waffle_chart[row, col] = category_index
    
    # instantiate a new figure object
    fig = plt.figure()

    # use matshow to display the waffle chart
    colormap = plt.cm.coolwarm
    plt.matshow(waffle_chart, cmap=colormap)
    plt.colorbar()

    # get the axis
    ax = plt.gca()

    # set minor ticks
    ax.set_xticks(np.arange(-.5, (width), 1), minor=True)
    ax.set_yticks(np.arange(-.5, (height), 1), minor=True)
    
    # add dridlines based on minor ticks
    ax.grid(which='minor', color='w', linestyle='-', linewidth=2)

    plt.xticks([])
    plt.yticks([])

    # compute cumulative sum of individual categories to match color schemes between chart and legend
    values_cumsum = np.cumsum(values)
    total_values = values_cumsum[len(values_cumsum) - 1]

    # create legend
    legend_handles = []
    for i, category in enumerate(categories):
        if value_sign == '%':
            label_str = category + ' (' + str(values[i]) + value_sign + ')'
        else:
            label_str = category + ' (' + value_sign + str(values[i]) + ')'
            
        color_val = colormap(float(values_cumsum[i])/total_values)
        legend_handles.append(mpatches.Patch(color=color_val, label=label_str))

    # add legend to chart
    plt.legend(
        handles=legend_handles,
        loc='best', 
        ncol=len(categories),
        bbox_to_anchor=(0., -0.2, 0.95, .1)
    )
    plt.show()


#%%

width = 40 # width of chart
height = 20 # height of chart

categories = df_dsn.index.values # categories
values = df_dsn['Total'] # correponding values of categories

colormap = plt.cm.coolwarm # color map class
create_waffle_chart(categories, values, height, width, colormap)

#%%SEABORN LESSSSGOOOOOOOOOOOOOOOOOO
import seaborn as sns
print('Seaborn installed and imported!')

#%%

# we can use the sum() method to get the total population per year
df_tot = pd.DataFrame(df_can[years].sum(axis=0))

# change the years to type float (useful for regression later on)
df_tot.index = map(float, df_tot.index)

# reset the index to put in back in as a column in the df_tot dataframe
df_tot.reset_index(inplace=True)

# rename columns
df_tot.columns = ['year', 'total']

# view the final dataframe
df_tot.head()


#%%

sns.regplot(x='year', y='total', data=df_tot)
 
#%%

ax = sns.regplot(x='year', y='total', data=df_tot, color='green', marker='+')
plt.show()

#%%

plt.figure(figsize=(15, 10))
ax = sns.regplot(x='year', y='total', data=df_tot, color='green', marker='+', scatter_kws={'s': 200})

ax.set(xlabel='Year', ylabel='Total Immigration') # add x- and y-labels
ax.set_title('Total Immigration to Canada from 1980 - 2013') # add title
plt.show()

#%%

plt.figure(figsize=(15, 10))

sns.set(font_scale=1.5)

ax = sns.regplot(x='year', y='total', data=df_tot, color='green', marker='+', scatter_kws={'s': 200})
ax.set(xlabel='Year', ylabel='Total Immigration')
ax.set_title('Total Immigration to Canada from 1980 - 2013')
plt.show()

#%%

plt.figure(figsize=(15, 10))

sns.set(font_scale=1.5)
sns.set_style('ticks')  # change background to white background

ax = sns.regplot(x='year', y='total', data=df_tot, color='green', marker='+', scatter_kws={'s': 200})
ax.set(xlabel='Year', ylabel='Total Immigration')
ax.set_title('Total Immigration to Canada from 1980 - 2013')
plt.show()
#%%

plt.figure(figsize=(15, 10))

sns.set(font_scale=1.5)
sns.set_style('whitegrid')

ax = sns.regplot(x='year', y='total', data=df_tot, color='green', marker='+', scatter_kws={'s': 200})
ax.set(xlabel='Year', ylabel='Total Immigration')
ax.set_title('Total Immigration to Canada from 1980 - 2013')
plt.show()

#%%




