import streamlit as st
import leafmap.foliumap as leafmap


def app():

    #st.title("Heatmap")

    #chemin="C:\Users\Lenovo\Desktop\GBR_rrd\GBR_rails.shp"

    chemin='../GBR_rrd/GBR_rails.shp'

    #filepath = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
    m = leafmap.Map(tiles="stamentoner")
    m.add_shp(chemin, layer_name="Railways")
    m.to_streamlit(height=700)
