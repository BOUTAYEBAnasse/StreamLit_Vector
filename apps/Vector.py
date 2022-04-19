import streamlit as st
import leafmap.foliumap as leafmap


def app():

    st.title("Heatmap")

    filepath = "C:\Users\admin\Desktop\GBR_rrd\GBR_rails.shp"
    m = leafmap.Map(tiles="stamentoner")
    m.add_heatmap(
        filepath,
        latitude="latitude",
        longitude="longitude",
        #value="pop_max",
        name="Heat map",
        radius=20,
    )
    m.to_streamlit(height=700)
