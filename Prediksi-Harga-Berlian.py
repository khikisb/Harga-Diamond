import xgboost as xgb
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

#Loading up the Regression model we created
model = xgb.XGBRegressor()
model.load_model('xgb_model.json')

#Caching the model for faster loading
@st.cache


# Define the prediction function
def predict(carat, cut, color, clarity, depth, table, x, y, z):
    #Predicting the price of the carat
    if cut == 'Fair':
        cut = 0
    elif cut == 'Good':
        cut = 1
    elif cut == 'Very Good':
        cut = 2
    elif cut == 'Premium':
        cut = 3
    elif cut == 'Ideal':
        cut = 4

    if color == 'J':
        color = 0
    elif color == 'I':
        color = 1
    elif color == 'H':
        color = 2
    elif color == 'G':
        color = 3
    elif color == 'F':
        color = 4
    elif color == 'E':
        color = 5
    elif color == 'D':
        color = 6
    
    if clarity == 'I1':
        clarity = 0
    elif clarity == 'SI2':
        clarity = 1
    elif clarity == 'SI1':
        clarity = 2
    elif clarity == 'VS2':
        clarity = 3
    elif clarity == 'VS1':
        clarity = 4
    elif clarity == 'VVS2':
        clarity = 5
    elif clarity == 'VVS1':
        clarity = 6
    elif clarity == 'IF':
        clarity = 7
    

    prediction = model.predict(pd.DataFrame([[carat, cut, color, clarity, depth, table, x, y, z]], columns=['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'x', 'y', 'z']))
    return prediction

st.set_page_config(
    page_title="Prediksi Harga Berlian",
    page_icon="👋",
)

st.title("")
st.sidebar.success("Pilih Halaman Yang Ingin Anda Tuju.")


st.title('Prediksi Harga Berlian')
st.image('panduanPengisian.png')
st.header('Masukkan Kriteria Berlian:')
carat = st.number_input('Berat Karat:', min_value=0.1, max_value=10.0, value=1.0)
cut = st.selectbox('Nilai Diamond:', ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
color = st.selectbox('Nilai Warna:', ['J', 'I', 'H', 'G', 'F', 'E', 'D'])
clarity = st.selectbox('Nilai Kejelasan Warna', ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'])
depth = st.number_input('Persentase Kedalaman Berlian:', min_value=0.1, max_value=100.0, value=1.0)
table = st.number_input('Persentase Tabel Berlian:', min_value=0.1, max_value=100.0, value=1.0)
x = st.number_input('Panjang Berlian (X) in mm:', min_value=0.1, max_value=100.0, value=1.0)
y = st.number_input('Lebar Berlian (Y) in mm:', min_value=0.1, max_value=100.0, value=1.0)
z = st.number_input('Tinggi Berlian (Z) in mm:', min_value=0.1, max_value=100.0, value=1.0)

if st.button('Tebak Harga Belian'):
    price = predict(carat, cut, color, clarity, depth, table, x, y, z)
    st.success(f'Harga Berlian Tersebut adalah ${price[0]:.2f} USD')

