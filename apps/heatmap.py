import streamlit as st
import leafmap.foliumap as leafmap


def app():

    st.title("Railways")

    filepath = "C:\Users\admin\Desktop\GBR_rrd\GBR_rails.shp"

    m = leafmap.Map(center=[0, 0], zoom=2)


    m.add_shp(filepath, layer_name="Railways")

