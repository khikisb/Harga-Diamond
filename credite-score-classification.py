import streamlit as st

st.write(""" 
# APLIKASI CREDIT SCORE
Oleh Okhi Sahrul Barkah
""")

st.write("======================================================================")
nama_nasabah = st.text_input('Masukkan Nama Nasabah')
pendapatan_per_tahun = st.number_input('Masukkan pendapatan pertahun')
durasi_peminjaman = st.number_input('Masukkan Durasi Peminjaman')
jumlah_tanggungan = st.number_input('Masukkan Jumlah Tanggungan')

cek_rasio = st.button('Cek Risk Ratio')
