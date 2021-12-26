
import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly
import plotly.figure_factory as ff
import seaborn as sns
from PIL import Image


import streamlit as st


st.write("""
    # Data Analysis App
    *:p*
""")


st.write("""
    ## Upload a file
""")

# Sidebar

upload_file = st.file_uploader("Choose a .csv file", type='csv')

if upload_file is not None:
    data = pd.read_csv(upload_file)
    st.write(data)
    st.success('your file has been successfully uploaded')
    st.write(data.head(20))
    st.write(data['SalePrice'].skew())

    st.subheader("SalePrice vs Neighborhood")
    var1 = pd.concat([data['SalePrice'], data['Neighborhood']], axis=1)
    st.write(var1)

    # Describe data
    st.subheader("Describe data")
    desc = data.describe()
    st.write(desc)

    # Mean SalesPrice
    st.subheader("Mean SalePrice")
    st.write(data['SalePrice'].mean())

    # bar chart
    # get number of appareances
    st.subheader('YEAR BUILT')
    cnt = data['YearBuilt'].value_counts()
    st.bar_chart(cnt)

    st.subheader('OVERALL QUALITY')
    qlt = data['OverallQual'].value_counts()
    st.bar_chart(qlt)

    st.subheader('Distritubion')
    sns.distplot(data['SalePrice'])
    st.pyplot()

    st.subheader('Distritubion')
    sns.distplot(data['OverallQual'])
    st.pyplot()

    plt.hist(data['YearBuilt'])
    st.pyplot()

    f, ax = plt.subplots(figsize=(20, 8))
    st.set_option('deprecation.showPyplotGlobalUse', False)
    fig = sns.boxplot(x='YearBuilt', y='SalePrice', data=data, orient='v')
    fig.axis(ymin=0, ymax=800000)
    plt.xticks(rotation=45)
    st.pyplot()

    st.subheader("")
    cormat = data.corr()
    f, ax = plt.subplots(figsize=(12, 9))
    sns.heatmap(cormat, vmax=0.8, square=True)
    st.pyplot()

    # Linear regression
    st.subheader("Linear regression YearBuilt / SalePrice")
    f, ax = plt.subplots(figsize=(10, 8))
    sns.regplot(x='YearBuilt', y='SalePrice', data=data, ax=ax)
    st.pyplot()

    # distplot
    st.subheader("Distplot")
    sns.distplot(data['SalePrice'], kde=False, color="b")
    st.pyplot()


else:
    st.markdown("the file is empty or invalid, please upload a valid file")
