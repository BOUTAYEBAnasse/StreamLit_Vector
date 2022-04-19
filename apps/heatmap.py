
import streamlit as st

import leafmap.foliumap as leafmap
import folium 









def app():

    st.title("Get the nearest point")




    form = st.form("my_form")

 


    longitude_value=form.text_input('Longitude : ', '')
    lattitude_value=form.text_input('Lattitude : ', '')
    form.form_submit_button("Recherecher le point le plus proche")

    longitude_value=52.126744
    lattitude_value=-1.077901

    
    current_location = Point(51.509093, -0.094151, srid=4326)



    layer='./GBR_rrd/GBR_rails.shp'


    m = leafmap.Map(center=[52.126744,-1.077901], zoom=6)
    #m.add_shp(chemin, layer_name="Railways")
    #m.to_streamlit(height=700)

 
    
    #st.title("Heatmap")

    path= "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"

    m.add_shp(layer, layer_name="Countries")


    #current_location = Point(longitude_value, lattitude_value, srid=4326)



    folium.Marker( location=[52.126744,-1.077901]).add_to(m)

    #leafmap.Marker([longitude_value, lattitude_value], tooltip='click here for more', popup=user_location,
    #icon=leafmap.Icon(color='red', icon='cloud')).add_to(m)




    #m.fitBounds(chemin.getBounds())
    """
    m.add_heatmap(
        filepath,
        latitude="latitude",
        longitude="longitude",
        value="pop_max",
        name="Heat map",
        radius=20,
    )
    """
    m.to_streamlit(height=700)
