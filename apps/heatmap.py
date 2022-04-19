import streamlit as st
import leafmap.foliumap as leafmap


def app():

    st.title("Heatmap")

    #m = leafmap.Map(center=[0, 0], zoom=2)

    #in_shp = 'C:\Users\Lenovo\Desktop\GBR_rrd\'
    #m.add_shp(in_shp, layer_name="Countries")

    filepath = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
    m = leafmap.Map(tiles="stamentoner")
    m.add_heatmap(
        filepath,
        latitude="latitude",
        longitude="longitude",
        value="pop_max",
        name="Heat map",
        radius=20,
    )
    m.to_streamlit(height=700)

