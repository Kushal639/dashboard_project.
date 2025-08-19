import plotly.express as px
import streamlit as st

def plot_bar(df, x, y):
    fig = px.bar(df, x=x, y=y, title="Bar Chart")
    st.plotly_chart(fig)

def plot_line(df, x, y):
    fig = px.line(df, x=x, y=y, title="Line Chart")
    st.plotly_chart(fig)

def plot_pie(df, names, values):
    fig = px.pie(df, names=names, values=values, title="Pie Chart")
    st.plotly_chart(fig)
