# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 18:25:48 2024

@author: sgast
"""

import folium
import webbrowser

def show_Map(map):
    map.save("map.html")
    webbrowser.open("map.html")

#%%

world_map = folium.Map(
    location=[56.130, -106.35], 
    zoom_start=4,
    tiles = "Cartodb dark_matter"
    )

show_Map(map=world_map)

#%%

lon, lat = -38.625, -12.875
zoom_start = 8
attr = (
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> '
    'contributors, &copy; <a href="https://cartodb.com/attributions">CartoDB</a>')
tiles = "https://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}.png"

show_Map(
    folium.Map(
        location=[lat, lon], 
        tiles=tiles, 
        attr=attr, 
        zoom_start=zoom_start))

#%%

import pandas as pd

df_incidents = pd.read_csv(
    r'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Police_Department_Incidents_-_Previous_Year__2016_.csv')

print("Listo!")

#%%

limit = 100
df_incidents = df_incidents.iloc[0:limit, :]
latitude = 37.77
longitude = -122.42
sanfran_map = folium.Map(
    location=[latitude, longitude], 
    zoom_start=12)
show_Map(sanfran_map)

#%%

incidents = folium.map.FeatureGroup()

for lat, long in zip(df_incidents.Y, df_incidents.X):
    incidents.add_child(
        folium.features.CircleMarker(
            [lat, long],
            radius = 5,
            color = 'black',
            fill = True,
            fill_color= 'blue',
            fill_opacity=0.6)
        )
sanfran_map.add_child(incidents)

show_Map(sanfran_map)

#%%

latitudes = list(df_incidents.Y)
longitudes = list(df_incidents.X)
labels = list(df_incidents.Category)

for lat, lng, label in zip(latitudes, longitudes, labels):
    folium.Marker([lat, lng], popup=label).add_to(sanfran_map)    
    
# add incidents to map
sanfran_map.add_child(incidents)

show_Map(sanfran_map)

#%%

# create map and display it
sanfran_map = folium.Map(
    location=[latitude, longitude], 
    zoom_start=12,
    tiles='Cartodb dark_matter')

# loop through the 100 crimes and add each to the map
for lat, lng, label in zip(df_incidents.Y, df_incidents.X, df_incidents.Category):
    folium.features.CircleMarker(
        [lat, lng],
        radius=5, # define how big you want the circle markers to be
        color='yellow',
        fill=True,
        popup=label,
        fill_color='blue',
        fill_opacity=0.6
    ).add_to(sanfran_map)

# show map
show_Map(sanfran_map)

#%%

from folium import plugins

sanfran_map = folium.Map(
    location=[latitude, longitude], 
    zoom_start=12,
    tiles='Cartodb dark_matter')

incidents = plugins.MarkerCluster().add_to(sanfran_map)

for lat, lng, label, in zip(df_incidents.Y, df_incidents.X, df_incidents.Category):
    folium.Marker(
        location=[lat, lng],
        icon=None,
        popup=label,
    ).add_to(incidents)

show_Map(sanfran_map)

#%%

import pandas as pd
import numpy as np

URL = r'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx'
df_can = pd.read_excel(
    URL,
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)
print('Data downloaded and read into a dataframe!')

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

df_can.set_index('Country', inplace=True)
df_can.columns = df_can.columns.astype(str)

years = np.array(range(1980, 2014)).astype(str)

#%%
# download countries geojson file

import requests
import json

URL = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/world_countries.json'

# Fetch the GeoJSON file
response = requests.get(URL)
world_geo = response.json()

print('GeoJSON file loaded!')


#%%

world_map = folium.Map(location=[0, 0], zoom_start=2)

#%%

world_map.choropleth(
    geo_data=world_geo,
    data=df_can,
    columns=['Country', 'Total'],
    key_on='feature.properties.name',
    fill_color='YlOrRd', 
    fill_opacity=0.7, 
    line_opacity=0.2,
    legend_name='Immigration to Canada'
)

# display map
show_Map(world_map)

#%%





