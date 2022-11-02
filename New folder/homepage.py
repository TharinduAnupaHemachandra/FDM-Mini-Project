import matplotlib
import streamlit as st
from PIL import Image
import hydralit_components as hc

import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt

st.set_page_config(layout='wide',initial_sidebar_state='collapsed',)

#st.title("Oyo Rentals")
#from matplotlib.backends._backend_agg import RendererAgg
from matplotlib.backends.backend_agg import RendererAgg

st.markdown("<h1 style='text-align: center; color: white;'>Oyo Rentals</h1>",
	            unsafe_allow_html = True)
st.sidebar.success("Select a page above.")
data = pd.read_csv(r'F:\preprocessed_dataset_1.csv')

df_cluster_lonlat = data['Cluster_Lon_Lat'].value_counts()
x_axis = df_cluster_lonlat[0]
y_axis = df_cluster_lonlat[1]

st.subheader('Full Dataset')
st.write(data)
#Bar Chart
st.subheader('Bar Chart for Clusters based on Longitude and Latitude')
st.bar_chart(data = df_cluster_lonlat, x = x_axis, y = y_axis)


#specify the primary menu definition
#menu_data = [
#    {'icon': "far fa-copy", 'label':"Left End"},
#    {'id':'page1()', 'label':"🌃Most Demanding Property Type"},
#    {'id':'page2()', 'label':"✒️Cancellation Policy Prediction"}
#    {'id':'page3()', 'label':"💵 Rental Price Prediction"}
#]

#matplotlib.use("agg")
#_lock = RendererAgg.lock
property_type_df = data['property_type'].value_counts()
#property_type_x_axis = df_cluster_lonlat[1].tolist()
#property_type_y_axis = df_cluster_lonlat[0].tolist()
df = pd.merge(pd.DataFrame(property_type_df), data, left_index=True, right_on= 'property_type')
#colors = df['color'].tolist()

row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((0.2, 1, .2, 1, .2))
with row0_1:
    st.header("Property Types")
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(property_type_df, labels=(property_type_df.index + ' (' + property_type_df.map(str)
                                     + ')'), wedgeprops = { 'linewidth' : 5, 'edgecolor' : 'white'
    })
    #display a white circle in the middle of the pie chart
    p = plt.gcf()
    p.gca().add_artist(plt.Circle( (0,0), 0.7, color='white'))
    st.pyplot(fig)

#with row0_2:
df = df.reset_index(drop=True)
t = ''
for i in range(len(df)):
    t=t+df.loc[i,'property_type'] + '\n'
for i in range(5):
    st.write("")








#st.set_page_config(
#    page_title="Oyo Rentals",
#    page_icon="🌇",
#)