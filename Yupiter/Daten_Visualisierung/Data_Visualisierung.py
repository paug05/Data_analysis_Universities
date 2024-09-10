#%%
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
#Query 1
germany = gpd.read_file("/home/paul/Database/Deutsch-Karte/gadm41_DEU_1.shp")
unis_bundesland = pd.read_csv("/home/paul/Database/Ergbnis-Queries/Query_1.csv")

# Query 2
germany_cities = gpd.read_file("/home/paul/Database/Deutsch-Karte/gadm41_DEU_2.shp")
studis_stadt = pd.read_csv("/home/paul/Database/Ergbnis-Queries/Query_2.csv")

#Query 3
uni_habilitation = pd.read_csv("/home/paul/Database/Ergbnis-Queries/Query_3.csv")

#Query 4

uni_alter = pd.read_csv("/home/paul/Database/Ergbnis-Queries/Query_4.csv")

#%%
germany_merged = germany.merge(unis_bundesland, left_on='NAME_1', right_on='NAME_1', how='left')
germany_merged['marked'] = germany_merged['NAME_1'].notnull()
fig, ax = plt.subplots(1, 1, figsize=(20, 20))

germany_merged.boundary.plot(ax=ax, linewidth=1, color='black')
germany_merged[germany_merged['marked']].plot(ax=ax, color='green')
unique_values = germany_merged['NAME_1'].unique()
cmap = ListedColormap(plt.cm.tab20c.colors[:len(unique_values)])

for idx, row in germany_merged.iterrows():
    plt.text(s=row['NAME_1'], x=row.geometry.centroid.x, y=row.geometry.centroid.y,
             horizontalalignment='center', fontsize=15, color='black', weight='bold')


plt.title("Bundesländer nach Unis Anzahl",fontsize=30)
germany_merged.plot(column='Unis', cmap=cmap, legend=True, ax=ax, missing_kwds={"color": "lightgrey"})
#%%
germany_cities_merged = germany_cities.merge(studis_stadt, left_on='NAME_2', right_on='NAME_1', how='left')
germany_cities_merged['marked'] = germany_cities_merged['NAME_2'].notnull()


fig, ax = plt.subplots(1, 1, figsize=(20, 20))
germany_cities_merged.boundary.plot(ax=ax, linewidth=1, color='black')
germany_cities_merged[germany_cities_merged['marked']].plot(ax=ax, color='green')
cmap = plt.cm.plasma  # Wähle eine Farbkodierung (z.B. viridis, plasma, inferno, etc.)


plt.title("15 Städte mit meisten Studis", fontsize=20)
germany_cities_merged.plot(column='studis', cmap=cmap, legend=True, ax=ax, missing_kwds={"color": "lightgrey"})
#%%
germany_cities_merged = germany_cities.merge(uni_habilitation, left_on='NAME_2', right_on='NAME_1', how='left')
germany_cities_merged['marked'] = germany_cities_merged['NAME_2'].notnull()
fig, ax = plt.subplots(1, 1, figsize=(30, 30))
germany_cities_merged.boundary.plot(ax=ax, linewidth=1, color='black')
germany_cities_merged[germany_cities_merged['marked']].plot(ax=ax, color='green')

unique_values = germany_cities_merged['NAME_2'].unique()
cmap = ListedColormap(plt.cm.tab20.colors[:len(unique_values)])

plt.title("Unis mit Habilitationsrecht und Städte", fontsize=30)
germany_cities_merged.plot(column='Hochschul_Name',cmap = cmap, legend=True, ax=ax, missing_kwds={"color": "lightgrey"})
#%%
germany_merged = germany.merge(uni_alter, left_on='NAME_1', right_on='NAME_1', how='left')
germany_merged['marked'] = germany_merged['NAME_1'].notnull()
fig, ax = plt.subplots(1, 1, figsize=(20, 20))
germany_merged.boundary.plot(ax=ax, linewidth=1, color='black')


germany_merged[germany_merged['marked']].plot(ax=ax, color='green')
cmap = plt.cm.plasma  # Wähle eine Farbkodierung (z.B. viridis, plasma, inferno, etc.)

for idx, row in germany_merged.iterrows():
    plt.text(s=row['NAME_1'], x=row.geometry.centroid.x, y=row.geometry.centroid.y,
             horizontalalignment='center', fontsize= 10, color='black', weight='bold')


plt.title("Älteste Unis",fontsize=30)
germany_merged.plot(column='DurchscnittsAlter', cmap=cmap, legend=True, ax=ax, missing_kwds={"color": "lightgrey"})