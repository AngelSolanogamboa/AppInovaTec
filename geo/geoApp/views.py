from django.shortcuts import render, redirect 
import os
import folium
# Create your views here.


def home(request):
    shp_dir = os.path.join(os.getcwd(),'media','shp')
    m = folium.Map(location=[16.751651,-93.105770],zoom_start=13)
    style_basin = {'fillcolor':'#228822','color':'#228822'}
    style_rivers = {'color': 'blue'}
    folium.GeoJson(os.path.join(shp_dir,'basin.geojson'),name = 'basin',
                   style_function=lambda x:style_basin).add_to(m)
    folium.GeoJson(os.path.join(shp_dir,'rivers.geojson'),name = 'basin',
                   style_function=lambda x:style_rivers).add_to(m)
    folium.LayerControl().add_to(m)
    m = m._repr_html_()
    context={'my_map':m}
    return render(request, 'geoApp/home.html', context)