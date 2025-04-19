import pandas as pd
import folium
import streamlit as st
from streamlit_folium import st_folium

def make_map(track: pd.DataFrame, zoom_start: int=15):
    #
    location = (track['latitude'].mean(), track['longitude'].mean())
    #
    map = folium.Map(location=location, zoom_start=zoom_start)
    #
    fg = folium.FeatureGroup(name='BRA3', show=True)
    folium.PolyLine(
        locations=track[['latitude', 'longitude']].values,
        # color="#FF0000",
        # weight=5,
        # tooltip="From Boston to San Francisco",
    ).add_to(fg)
    #
    map.add_child(fg)
    folium.LayerControl().add_to(map)
    #
    return map

#
st.sidebar.title("Sidebar Title")
st.sidebar.markdown("This is the sidebar content")

#
st.write("Hello ,let's learn how to build a streamlit app together")
# 

# Call to render Folium map in Streamlit
track = pd.read_parquet('data.parquet')
map = make_map(track)
st_data = st_folium(map) # , width=725