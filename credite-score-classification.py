import streamlit as st
import numpy as np
import pandas as pd

st.write(""" 
# Aplikasi Web Klasifikasi Credit Score
Oleh Okhi Sahrul Barkah
""")

dataset = "https://gist.github.com/khikisb/7f53f136bf6dd98639fc3042af46fbdc"
data = pd.read_csv(dataset)


st.write("======================================================================")
nama_nasabah = st.text_input('Masukkan Nama Nasabah')
pendapatan_per_tahun = st.number_input('Masukkan pendapatan pertahun')
durasi_peminjaman = st.number_input('Masukkan Durasi Peminjaman')
jumlah_tanggungan = st.number_input('Masukkan Jumlah Tanggungan')
