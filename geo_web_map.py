import folium
import pandas

'''
Representing Geospatial data using folium with Python.
    
    Geospatial data:
        - Volcano Height ('Volcanoes.txt')
        - Population ('world.json')
'''

volcanoes = pandas.read_csv('Volcanoes.txt')
lat = list(volcanoes['LAT'])
lon = list(volcanoes['LON'])
elev = list(volcanoes['ELEV'])

'''
To return string for folium icon to color map for volcano height
    parameters: elevation <integer> height of volcano
    returns: color <string> represents scale of height
'''

def el_color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation <= 2500:
        return 'blue'
    else:
        return 'red'

'''
Volcano data integrated with folium
'''

map = folium.Map(location = [38.58,-99.09], zoom_start = 5, tiles = 'Stamen Terrain')
fgv= folium.FeatureGroup(name = "Volcanoes")

for lt, ln, el in zip(lat,lon, elev):
    fgv.add_child(folium.Marker(location = [lt,ln], popup = str(el) + ' m' ,
    icon=folium.Icon(color= el_color(el))))

'''
Population data integrated with folium
'''

fgp = folium.FeatureGroup(name = "Populations")

fgp.add_child(folium.GeoJson(data = open('world.json','r', 
encoding = 'utf-8-sig').read(),
style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

'''
Add instances to folium object
Create html file with results
'''

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map1.html")
