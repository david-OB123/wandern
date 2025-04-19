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
tracks = pd.read_parquet('data.parquet')


#### Sidebar
# st.sidebar.title("Sidebar Title")
# st.sidebar.markdown("This is the sidebar content")
option = st.sidebar.selectbox(
    label='Choose your tour.',
    options=tracks['name'].unique()
)

st.write('Your selected tour:', option)

# Call to render Folium map in Streamlit
track = tracks.loc[lambda x: x['name']==option]
map = make_map(track)
st_data = st_folium(map) # , width=725
# st.write(tracks.loc[lambda x: x['name']==option])
