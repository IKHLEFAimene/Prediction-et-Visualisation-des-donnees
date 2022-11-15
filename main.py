import pandas as pd
import matplotlib.pyplot as plt
import folium
import webbrowser


m= folium.Map(location=[46.227638, 2.213749], zoom_start=6)
m.save('map.html') 
new = 2
webbrowser.open('map.html', new=new)