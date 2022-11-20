from bokeh.models.widgets import Div
import streamlit as st


st.set_page_config(
    page_title="Code-Project",
    page_icon="👋",
)

st.title("Halo Semuanya !👋")

st.write('Kamu Bisa menemukan Source Code Project ini')

link = '[GitHub](https://github.com/khikisb/Harga-Diamond/)'
st.markdown(link, unsafe_allow_html=True)
