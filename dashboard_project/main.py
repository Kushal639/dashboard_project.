import streamlit as st
import pandas as pd
from utils import load_csv, preprocess_data
from visualizer import plot_bar, plot_line, plot_pie

st.title("📊 Data Visualization Dashboard")


uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file:
    
    df = load_csv(uploaded_file)
    st.write("🔍 Preview of Uploaded Data", df.head())


    if st.checkbox("Preprocess Data (parse dates, drop empty rows)"):
        date_col = st.selectbox("Select Date Column", df.columns)
        df = preprocess_data(df, date_col)
        st.write("✅ Preprocessed Data", df.head())

    
    x_axis = st.selectbox("Select X-Axis", df.columns)
    y_axis = st.selectbox("Select Y-Axis", df.columns)

    chart_type = st.selectbox("Select Chart Type", ["Bar", "Line", "Pie"])


    if st.button("Generate Chart"):
        if chart_type == "Bar":
            plot_bar(df, x_axis, y_axis)
        elif chart_type == "Line":
            plot_line(df, x_axis, y_axis)
        elif chart_type == "Pie":
            plot_pie(df, x_axis, y_axis)