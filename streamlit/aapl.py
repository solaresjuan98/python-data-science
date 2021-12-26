
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly
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

if upload_file is not None:
    data = pd.read_csv(upload_file)
    st.write(data)
    st.success('your file has been successfully uploaded')

    data = data.astype({"Close": float})

    data['Date'] = pd.to_datetime(data.Date, format="%Y-%m-%d")
    #data['Date'] = pd.to_datetime(data.Date, format="%d/%m/%Y")

    #st.write(data.dtypes)

    # datanew = pd.DataFrame(index=range(0, len(data)), columns=['Date', 'Close'])

    # for i in range (0, len(data)):
    #     datanew['Date'][i] = data['Date'][i]
    #     datanew['Close'][i] = data['Close'][i]

    # st.write(datanew.head(20))
    
    #data['Date']
    data.index = data['Date']
    plt.plot(data['Close'], label="History")
    st.pyplot()
    st.line_chart(data['Close'])


else:
    st.markdown("the file is empty or invalid, please upload a valid file")
