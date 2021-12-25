
import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly
import plotly.figure_factory as ff
from PIL import Image

import streamlit as st

st.write("""
# My first app
Que onda *que onda*
""")

st.subheader('This is a subheader')

# Insert an image
#image = Image.open("")
## st.image(image, use_column_width = True)

st.write("writing a text here")

st.markdown("this is a markdown xd")

# Meesages
st.success("Success!!")
st.info("This is information for you")
st.warning("Be careful")
st.error("This is an error")
##st.help("Do you need help?")


dataframe = np.random.rand(10, 20)
st.dataframe(dataframe)
# st.line_chart(dataframe)

st.text("---"*100)

df = pd.DataFrame(np.random.rand(10, 20), columns=(
    'col %d' % i for i in range(20)))
st.dataframe(df.style.highlight_max(axis=1))

# Display Chart
st.subheader('Line Chart')
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.line_chart(chart_data)

st.text("---"*100)

# Area chart
st.subheader('Area Chart')
st.area_chart(chart_data)


# Bar Chart
st.set_option('deprecation.showPyplotGlobalUse', False)
st.subheader('Bar chart')
st.bar_chart(chart_data)

##
arr = np.random.normal(1, 1, size=100)
plt.hist(arr, bins=20)
st.pyplot()

st.text("---"*100)


# Adding distplot
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) - 2

hist_data = [x1, x2, x3]
group_labels = ['Group1', 'Group2', 'Group3']

fig = ff.create_distplot(hist_data, group_labels, bin_size=[.2, .25, .5])

st.plotly_chart(fig, user_container_width=True)

st.text("---"*100)

df = pd.DataFrame(np.random.randn(100, 2) /
                  [50, 50]+[37.76, - 122.4], columns=['lat', 'lon'])
st.map(df)

st.text("---"*100)

# Creating buttons
if st.button("Say hello"):
    st.write("*Que onda que onda*")
else:
    st.write("*adios xd*")


st.text("---"*100)

# Create a radiobutton
genre = st.radio("What is your favorite movie genre?",
                 ('commedy', 'drama', 'romance', 'documentary'))

if genre == 'commedy':
    st.write('you have selected commedy')
elif genre == 'drama':
    st.write('you have selected drama')
elif genre == 'romance':
    st.write('you have selected romance')
elif genre == 'documentary':
    st.write('you have selected documentary')
else:
    st.write('you dont like anything')


st.text("---"*100)

# select button
option = st.selectbox("How was your day?", ('nice', 'sad', 'awesome'))

st.write("Your day was: ", option)

st.text("---"*100)

option2 = st.multiselect(
    "How was your day?, multiple choice", ('nice', 'sad', 'awesome'))

st.write("Your day was: ", option2)

st.text("---"*100)

age = st.slider('How old are you?', 0, 150, 18)

st.write("Your age is: ", age)

values = st.slider('Select  a range of values', 0, 200, (15, 80))
st.write("You selected a range between: ", values)


number = st.number_input('Input number')
st.write(number)

st.text("---"*100)
st.text("---"*100)

# File uploader
upload_file = st.file_uploader("Choose a .csv file", type='csv')

if upload_file is not None:
    data = pd.read_csv(upload_file)
    st.write(data)
    st.success('your file has been successfully uploaded')
else:
    st.markdown("the file is empty or invalidad, please upload a valid file")

# Color picker

# color = st.sidebar.beta_color_picker("Pick your favorite color: ", '#00f900')
# st.write("This is your color", color)


# Side bar

st.text("---"*100)
st.text("---"*100)

add_sidebar = st.sidebar.selectbox(
    "What is your favorite course? ", ('Compi 1', 'Matematica Basica 1', 'Otro'))

my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)

# with st.spinner('wait for it...'):
#     time.sleep(5)

st.success('successful')

st.text("---"*100)


st.balloons()