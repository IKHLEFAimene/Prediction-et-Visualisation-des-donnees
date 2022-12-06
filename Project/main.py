import pandas as pd
import plotly.express as px
from data_prep import df_departement
import time
import guppy  
from guppy import hpy 


#Function that filters data by "département" with their yearly electricity consumption
def data_per_depart (df,departement_data):
    cons={}
    for year in range(2018,2022):
        data_year=df_departement(df,departement_data,year)
        cons[str(year)]=data_year["Consommation annuelle moyenne de la commune (MWh)"].values 
    df_cons_depart=pd.DataFrame(cons)
    df_cons_depart.rename(columns={'Consommation annuelle moyenne de la commune (MWh)':'Consommation annuelle moyenne du departement (MWh)'}, inplace=True)
    df_cons_depart["nom_departement"]=data_year.index.values
    df_cons_depart['Consommation annuelle moyenne du departement (MWh)']=df_cons_depart.mean(axis=1)
    df_cons_depart=df_cons_depart[['nom_departement','2018','2019','2020','2021','Consommation annuelle moyenne du departement (MWh)']]

    return df_cons_depart

start = time.time()

#load data
departement_data= pd.read_csv('Project\communes-departement-region.csv', sep=',')
df=pd.read_csv('Project\consommation-annuelle-residentielle-par-adresse.csv',sep=';', low_memory=False)

#Using our function on a empty data frame 
df1=data_per_depart(df,departement_data)

#Color scale
colors = ['#F0F8FF','#B0E0E6',  '#87CEFA', '#00BFFF','#1E90FF', '#4682B4', '#0000FF', '#00008B']

cons_max = df1['Consommation annuelle moyenne du departement (MWh)'].max()

#Splitting consumptions ranges for colors 
def group_cons(x):
    y = float(cons_max / 8)
    if x < y:
        return '{}~{}'.format(0, y)
    elif x < y * 2:
        return '{}~{}'.format(y, y*2)
    elif x < y * 3:
        return '{}~{}'.format(y*2, y*3)
    elif x < y * 4:
        return '{}~{}'.format(y*3, y*4)
    elif x < y * 5:
        return '{}~{}'.format(y*4, y*5)
    elif x < y * 6:
        return '{}~{}'.format(y*5, y*6)
    elif x < y * 7:
        return '{}~{}'.format(y*6, y*7)
    else:
        return '{}~{}'.format(y*7, y*8)


df1 = df1.sort_values('Consommation annuelle moyenne du departement (MWh)')
df1['Taux de csm'] = df1['Consommation annuelle moyenne du departement (MWh)'].apply(group_cons)
print(df1['Taux de csm'])

#Using plotly.express to show our map with the data we customized
fig=px.choropleth(df1,
            geojson="https://france-geojson.gregoiredavid.fr/repo/departements.geojson",
            featureidkey='properties.nom',
            locations='nom_departement',
            color='Taux de csm',
            color_discrete_map=dict(zip(df1['Taux de csm'].unique(), colors)),
            title="Consommation d'énergie en France" ,  
            height=800
              )

#Re-design of the map
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(
    hoverlabel=dict(
        bgcolor="black",
        font_size=16,
        font_family="Rockwell",
        font_color='white'
    )
)
# img = ('Carte.PNG')
# image = (img, bottom = 40,left =65).add_to(fig)
fig.show()

#Generating an html file for offline uses
fig.write_html('map.html')

end = time.time()

print(end-start)
h = guppy.hpy()
print(h.heap())