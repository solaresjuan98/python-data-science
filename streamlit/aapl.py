
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly
import plotly.express as px
import plotly.figure_factory as ff
import seaborn as sns
from PIL import Image

import streamlit as st


st.write("""
# AAPL STOCK
Que onda *que onda*
""")


add_sidebar = st.sidebar.subheader("Options")

upload_file = st.file_uploader("Choose a .csv file", type='csv')

sidebar_option = st.sidebar.selectbox('Select dataset', ('APPL', 'COVID'))

if upload_file is not None:
    data = pd.read_csv(upload_file)
    st.write(upload_file.name)
    st.write(data)
    st.success('your file has been successfully uploaded')

    if sidebar_option == 'APPL' and upload_file.name == 'AAPL.csv':

        st.write('# APPL STOCK')
        data = data.astype({"Close": float})
        data['Date'] = pd.to_datetime(data.Date, format="%Y-%m-%d")
        st.subheader("Close history 2015-2017")
        data.index = data['Date']
        plt.plot(data['Close'], label="History")
        st.pyplot()
        st.subheader("XD")
        st.area_chart(data['Close'])

    elif sidebar_option == 'COVID' and upload_file.name == 'all-states-history.csv':

        st.write('# Covid Tracker')

        # Deaths by state
        st.subheader("Deaths by state")
        data['date'] = pd.to_datetime(data.date, format="%m/%d/%Y")
        data.index = data['date']
        plt.plot(data['death'], label="Covid deaths history")
        st.pyplot()

        # California data
        cali = ['CA']
        flt = data[data.state.isin(cali)]
        a = flt

        # New york data
        ny = ['NY']
        nydf = data[data.state.isin(ny)]

        # format date
        flt['date'] = pd.to_datetime(flt.date, format="%m/%d/%Y")  # %Y-%m-%d
        flt.index = flt['date']

        st.subheader("Deaths in California")
        plt.plot(flt['death'], label="Covid deaths history")
        st.pyplot()

        st.subheader('Positive cases in California')
        plt.plot(flt['positive'], label="California Positive cases history")
        st.pyplot()

        st.write(flt)
        st.subheader('Positive increase in California')
        plt.plot(flt['positiveIncrease'], label="Califoria Positive Increase")
        st.pyplot()

        # distplot
        st.subheader("distplot postive cases California ")
        f, ax = plt.subplots(figsize=(10, 8))
        sns.distplot(flt['positive'], kde=False, color="b")
        st.pyplot()

        # new york
        st.write(nydf['positive'].head(5))

        # df = pd.DataFrame(
        #     [["Product A", 5.6, 7.8, 5], ["Product B", 5.8, 7.2, 4.9]],
        #     columns=["Product", "Comfort", "Sound", "Calls"]
        # )

        # fig = px.bar(df, x="Product", y=[
        #     "Comfort", "Sound", "Calls"], barmode='group', height=400)
        # st.dataframe(df) # if need to display dataframe
        # st.plotly_chart(fig)

        st.subheader("California / New York Deaths")
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plotdata = pd.DataFrame({
            "Deaths": [flt['death'].sum(), nydf['death'].sum()],
        },
            index=["California", "New york"]
        )

        plotdata.plot(kind="bar")
        plt.title("Covid deaths California and New york")
        st.pyplot()

        

        st.subheader("California Deaths vs Positive")
        plotdata = pd.DataFrame({
            "Positive": [flt['positive'].sum(), nydf['positive'].sum()],
            "Death": [flt['death'].sum(), nydf['death'].sum()]
        },
            index=["California", "New York"]
        )
        plotdata.plot(kind="bar")
        #plt.title("Covid deaths California and New york")
        st.pyplot()

        ## Modify y-axis size
        # plt.plot(range(0, 10))
        # scl_factor = 10**6
        # xmin, xmax = plt.xlim()
        # ymin, ymax = plt.ylim()

        # plt.xlim(xmin * scl_factor, xmax * scl_factor)
        # plt.ylim(ymin * scl_factor, ymax * scl_factor)
        # st.pyplot()

else:
    st.markdown("the file is empty or invalid, please upload a valid file")
