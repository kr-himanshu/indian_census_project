import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
st.set_page_config(layout='wide')
df=pd.read_csv('data/indian census.csv')
print(df.columns[5:])


list_of_state=list(df['State'].unique())
list_of_state.insert(0,"Overall India")

st.sidebar.title("Indian Census Data Viz")
Selectd_State=st.sidebar.selectbox("Select a State",list_of_state)
primary=st.sidebar.selectbox("Select Primary Option", sorted(df.columns[5:]))
secondary=st.sidebar.selectbox("Select secondary Option",sorted(df.columns[5:]))


plot=st.sidebar.button("Plot Graph")

if plot:
    st.text("size represents primary parameter")
    st.text("color represents secondary parameter")
    if Selectd_State=="Overall India":
        # plot for india
        fig=px.scatter_mapbox(df,lat='Latitude',lon='Longitude',zoom=6,size=primary,
                              color=secondary,mapbox_style='carto-positron',size_max=35,width=1200,height=700,hover_name='District')
        st.plotly_chart(fig,use_container_width=True)
    else:
        #plot for state
        state_df=df[df['State']==Selectd_State]
        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', zoom=4, size=primary,
                                color=secondary, mapbox_style='carto-positron', size_max=35, width=1500, height=900,
                                hover_name="District",color_continuous_scale=px.colors.cyclical.IceFire)
        st.plotly_chart(fig, use_container_width=True)
