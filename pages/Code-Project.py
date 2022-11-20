import streamlit as st


st.set_page_config(
    page_title="Code-Project",
    page_icon="👋",
)

st.title("Halo Semuanya !👋")

st.write('Kamu Bisa menemukan Source Code Project ini')

url = 'https://github.com/khikisb/Harga-Diamond/'

if st.button('Di Github'):
    webbrowser.open_new_tab(url)
