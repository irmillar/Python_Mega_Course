import folium
import pandas

def elevation_color(el):
    if el < 1000:
        return "green"
    elif 1000 <= el < 3000:
        return "orange"
    else:
        return "red"

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
names = list(data["NAME"])

map = folium.Map(location=[48.77, -121.81], zoom_start=5, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanoes")
for lt, ln, el, nm in zip(lat, lon, elev, names):
    fgv.add_child(folium.CircleMarker(location=(lt, ln), radius=6, popup=str(el) + " m",
    fill=True, fill_color=elevation_color(el), color="grey", fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
style_function=lambda x: {"fillColor":"green" if x["properties"]["POP2005"] < 10000000
else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"}))

map.add_child(fgp)
map.add_child(fgv)

map.add_child(folium.LayerControl())
map.save("Map2.html")
