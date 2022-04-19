import streamlit as st
import leafmap.foliumap as leafmap


def app():

    st.title("Get the nearest point")




    form = st.form("my_form")

    # Now add a submit button to the form:
    form.form_submit_button("Submit")


    #random_column = st.selectbox("Select a column to apply random colors", column_names)





    layer='./GBR_rrd/GBR_rails.shp'


    m = leafmap.Map(center=[52.126744,-1.077901], zoom=6)
    #m.add_shp(chemin, layer_name="Railways")
    #m.to_streamlit(height=700)

 
    
    #st.title("Heatmap")

    path= "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"

    m.add_shp(layer, layer_name="Countries")


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
