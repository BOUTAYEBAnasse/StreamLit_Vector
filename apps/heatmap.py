import streamlit as st
import leafmap.foliumap as leafmap


def app():

    #st.title("Heatmap")


    chemin='./GBR_rrd/GBR_rails.shp'


    m = leafmap.Map(center=[0, 0], zoom=2)
    #m.add_shp(chemin, layer_name="Railways")
    #m.to_streamlit(height=700)



    #st.title("Heatmap")

    filepath = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"

    m.add_shp(chemin, layer_name="Countries")

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
