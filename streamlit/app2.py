
import time

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.figure_factory as ff
import seaborn as sns
from PIL import Image
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

import streamlit as st

# Title

st.title('Proyecto 2')

# image


# Subtitle
st.write("""
## A Simple data app
""")

# Sidebar
add_sidebar = st.sidebar.subheader("Options")


dataset_name = st.sidebar.selectbox(
    'Select dataset', ('Breast Cancer', 'Iris', 'Wine'))

classifier_name = st.sidebar.selectbox('Select Classifier', ('SVM', 'KNN'))


# get dataset
def get_dataset(name):
    data = None

    if name == 'Iris':
        data = datasets.load_iris()
    elif name == 'Wine':
        data = datasets.load_wine()
    else:
        data = datasets.load_breast_cancer()

    x = data.data
    y = data.target

    return x, y


# ==================================================


x, y = get_dataset(dataset_name)

st.dataframe(x)
st.write('Shape of your dataset selected is: ', x.shape)
st.write('Unique target variables: ', len(np.unique(y)))
st.set_option('deprecation.showPyplotGlobalUse', False)

fig = plt.figure()
sns.boxplot(data=x, orient='h')
st.pyplot()

plt.hist(x)
st.pyplot()


# Building our algorithm
def add_parameter(name_of_clf):
    params = dict()

    if name_of_clf == 'SVM':
        C = st.sidebar.slider('C', 0.01, 15.0)
        params['C'] = C
    else:
        name_of_clf = 'KNN'
        k = st.sidebar.slider('K', 1, 15)
        params['k'] = k

    return params


params = add_parameter(classifier_name)


# Accesing our classifier
def get_classifier(name_of_clf, params):
    clf = None
    if name_of_clf == 'SVM':
        clf = SVC(C=params['c'])
    elif name_of_clf == 'KNN':
        clf = KNeighborsClassifier(n_neighbors=params['k'])
    else:
        st.warning("you didn't select any option, please select at leaste one algorithm")

    return clf


clf = get_classifier(classifier_name, params)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state=10)

clf.fit(x_train, y_train) ## 80% for training

y_pred = clf.predict(x_test) ## 20% for testing

st.write(y_pred)


accuracy = accuracy_score(y_test, y_pred)
st.write('Classifier name: ', classifier_name)
st.write('Accuracy for your model is: ', accuracy)