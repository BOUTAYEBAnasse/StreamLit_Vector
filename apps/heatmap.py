import streamlit as st
import leafmap.foliumap as leafmap


def app():

    st.title("Heatmap")

    m = leafmap.Map(center=[0, 0], zoom=2)

    in_shp = 'C:\Users\Lenovo\Desktop\GBR_rrd\GBR_rails.shp'
    m.add_shp(in_shp, layer_name="Railways")

    #filepath = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
    m.to_streamlit(height=700)

