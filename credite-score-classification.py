import streamlit as st
import numpy as np
import pandas as pd

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from collections import OrderedDict
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, precision_score, f1_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.datasets import make_classification
from sklearn.svm import SVC

st.write(""" 
# Aplikasi Web Klasifikasi Credit Score
Oleh Okhi Sahrul Barkah
""")

dataset = "https://gist.github.com/khikisb/7f53f136bf6dd98639fc3042af46fbdc"
data = pd.read_csv(dataset)
# data

# data.head()
# create a dataframe with all training data except the target column
X = data.drop(columns=["risk_rating"])


st.write("======================================================================")
nama_nasabah = st.text_input('Masukkan Nama Nasabah')
pendapatan_per_tahun = st.number_input('Masukkan pendapatan pertahun')
durasi_peminjaman = st.number_input('Masukkan Durasi Peminjaman')
jumlah_tanggungan = st.number_input('Masukkan Jumlah Tanggungan')

cek_rasio = st.button('Cek Risk Ratio')

if cek_rasio:
    result_test_naive_bayes = clf_pf.predict([[0,	0,	0,	0,	0,	0,	1,	pendapatan_per_tahun,	durasi_peminjaman, jumlah_tanggungan]])[FIRST_IDX]
    st.write(f"Customer Name : ", nama_nasabah,  "has risk rating", result_test_naive_bayes ,"based on Gaussian Naive Bayes model")
