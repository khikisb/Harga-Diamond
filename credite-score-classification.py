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
# APLIKASI CREDIT BANK
Oleh Okhi Sahrul Barkah
""")




dataset = "https://raw.githubusercontent.com/wahyuarilsaputra/dataset/main/credit_score.csv"
data = pd.read_csv(dataset)
# data

# data.head()
# create a dataframe with all training data except the target column
X = data.drop(columns=["risk_rating"])

# # check that the target variable has been removed
# X.head()

split_overdue_X = pd.get_dummies(X["rata_rata_overdue"], prefix="overdue")
X = X.join(split_overdue_X)

X = X.drop(columns = "rata_rata_overdue")

labels = data["risk_rating"]
# 
KPR_status = pd.get_dummies(X["kpr_aktif"], prefix="KPR")
X = X.join(KPR_status)

# remove "rata_rata_overdue" feature
X = X.drop(columns = "kpr_aktif")

# st.write("menampilkan dataframe X")
# st.dataframe(X)

# st.write("normalisasi")
# normalize feature 'pendapatan_setahun_juta', 'durasi_pinjaman_bulan', 'jumlah_tanggungan'
old_normalize_feature_labels = ['pendapatan_setahun_juta', 'durasi_pinjaman_bulan', 'jumlah_tanggungan']
new_normalized_feature_labels = ['norm_pendapatan_setahun_juta', 'norm_durasi_pinjaman_bulan', 'norm_jumlah_tanggungan']
normalize_feature = data[old_normalize_feature_labels]

# st.dataframe(normalize_feature)

scaler = MinMaxScaler()

scaler.fit(normalize_feature)

normalized_feature = scaler.transform(normalize_feature)

normalized_feature_df = pd.DataFrame(normalized_feature, columns = new_normalized_feature_labels)

# st.write("data setelah dinormalisasi")
# st.dataframe(normalized_feature_df)

X = X.drop(columns = old_normalize_feature_labels)

X = X.join(normalized_feature_df)

X = X.join(labels)

# st.write("dataframe X baru")
# st.dataframe(X)

subject_lables = ["Unnamed: 0",  "kode_kontrak"]
X = X.drop(columns = subject_lables)

# percent_amount_of_test_data = / HUNDRED_PERCENT
percent_amount_of_test_data = 0.3

# st.write("dataframe X baru")
# st.dataframe(X)

# separate target 

# values
matrices_X = X.iloc[:,0:10].values

# classes
matrices_Y = X.iloc[:,10].values

X_1 = X.iloc[:,0:10].values
Y_1 = X.iloc[:, -1].values

# X_train, X_test, y_train, y_test = train_test_split(matrices_X, matrices_Y, test_size = percent_amount_of_test_data, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X_1, Y_1, test_size = percent_amount_of_test_data, random_state=0)

# X_1

# Y_1

### Dictionary to store model and its accuracy

model_accuracy = OrderedDict()

### Dictionary to store model and its precision

model_precision = OrderedDict()

### Dictionary to store model and its recall

model_recall = OrderedDict()

### Applying Naive Bayes Classification model

naive_bayes_classifier = GaussianNB()
naive_bayes_classifier.fit(X_train, y_train)
Y_pred_nb = naive_bayes_classifier.predict(X_test)


### Making the confusion matrix
cm = confusion_matrix(y_test, Y_pred_nb)


### Printing the accuracy, precision, and recall of the model
# st.write('Confusion matrix for Gaussian Naive Bayes\n',cm)

naive_bayes_accuracy = round(100 * accuracy_score(y_test, Y_pred_nb), 2)
model_accuracy['Gaussian Naive Bayes'] = naive_bayes_accuracy

naive_bayes_precision = round(100 * precision_score(y_test, Y_pred_nb, average = 'weighted'), 2)
model_precision['Gaussian Naive Bayes'] = naive_bayes_precision

naive_bayes_recall = round(100 * recall_score(y_test, Y_pred_nb, average = 'weighted'), 2)
model_recall['Gaussian Naive Bayes'] = naive_bayes_recall

# st.write('The accuracy of this model is {} %.'.format(naive_bayes_accuracy))
# st.write('The precision of this model is {} %.'.format(naive_bayes_precision))
# st.write('The recall of this model is {} %.'.format(naive_bayes_recall))

# Y_pred_nb

clf = GaussianNB()
clf.fit(matrices_X, matrices_Y)
clf_pf = GaussianNB()
clf_pf.partial_fit(matrices_X, matrices_Y, np.unique(matrices_Y))

FIRST_IDX = 0

# # try with value [0,	0,	0,	0,	0,	0,	1,	0.582609,	0.666667,	0]
# result_test_naive_bayes = clf_pf.predict([[0,	0,	0,	0,	0,	0,	1,	0.201010,	0.00000,0]])[FIRST_IDX]
# st.write(f"Customer Name : Dio has risk rating {result_test_naive_bayes} based on Gaussian Naive Bayes model")


st.write("======================================================================")
nama_nasabah = st.text_input('Masukkan Nama Nasabah')
pendapatan_per_tahun = st.number_input('Masukkan pendapatan pertahun')
durasi_peminjaman = st.number_input('Masukkan Durasi Peminjaman')
jumlah_tanggungan = st.number_input('Masukkan Jumlah Tanggungan')

cek_rasio = st.button('Cek Risk Ratio')

if cek_rasio:
    result_test_naive_bayes = clf_pf.predict([[0,	0,	0,	0,	0,	0,	1,	pendapatan_per_tahun,	durasi_peminjaman, jumlah_tanggungan]])[FIRST_IDX]
    st.write(f"Customer Name : ", nama_nasabah,  "has risk rating", result_test_naive_bayes ,"based on Gaussian Naive Bayes model")
