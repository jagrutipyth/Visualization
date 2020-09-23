import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline #offline module to render the map


# Explore the structure of the data.
filename = 'C:\\Users\dell15\PycharmProjects\pythonProject\Visualization\JSON format\eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f) #converts the data into a format Python can work with
    readable_file = r'C:\Users\dell15\PycharmProjects\pythonProject\Visualization\JSON format\readable_eq_data.json' #created new file
    with open(readable_file, 'w') as writer:
        json.dump(all_eq_data, writer, indent=4) #writes data into newly created file

all_eq_dicts = all_eq_data['features'] #data associated with the key 'features' and store it in all_eq_dicts.
print(len(all_eq_dicts))


mags, lons, lats,hover_texts = [], [], [],[]
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    location = eq_dict['geometry']['coordinates']
    title = eq_dict['properties']['title']
    lon = location[0]
    lat = location[1]
    lons.append(lon)
    lats.append(lat)
    mags.append(mag)
    hover_texts.append(title)

#print(mags[:10])
#print(lons[:10])
#print(lats[:5])

'''Map the earthquakes.'''

#with Plotly  you can make to a data series, each of which can be expressed as a key-value pair.
data = [{
 'type': 'scattergeo',
 'lon': lons,
 'lat': lats,
 'text': hover_texts,
 'marker': {
 'size': [5*mag for mag in mags],
 'color': mags, #color changes with severity of mag
 'colorscale': 'Viridis', # dark blue to bright yellow
 'reversescale': True,
 'colorbar': {'title': 'Magnitude'}, #To makescolorscale easy to read give it title

 },
}]

my_layout = Layout(title='Global Earthquakes')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')

'''TO see different built in colorscales'''
#import plotly.express as px

#fig = px.colors.sequential.swatches()
#fig.show()
