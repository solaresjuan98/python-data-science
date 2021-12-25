
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.svm import SVC
import streamlit as st
import pickle


# load data into a dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# separate training and test data
x_train, x_test, y_train, y_test = train_test_split(X, y)


lin_reg = LinearRegression()
log_reg = LogisticRegression()
svc_m = SVC()


# train models
lin_regr = lin_reg.fit(x_train, y_train)
log_regr = log_reg.fit(x_train, y_train)
svc_mo = svc_m(x_train, y_train)


# save models in a pickle file
with open('lin_reg.pkl', 'wb') as li:
    pickle.dump(lin_regr, li)


with open('log_reg.pkl', 'wb') as lo:
    pickle.dump(log_regr, lo)

with open('svc_m.pkl', 'wb') as sv:
    pickle.dumps(svc_mo, sv)
