from bokeh.models.widgets import Div
import streamlit as st


st.set_page_config(
    page_title="Code-Project",
    page_icon="👋",
)

st.title("Halo Semuanya !👋")

st.write('Kamu Bisa menemukan Source Code Project ini')


if st.button('Di Github'):
    js = "window.open('https://github.com/khikisb/Harga-Diamond/')"  # New tab or window
    js = "window.location.href = 'https://github.com/khikisb/'"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)
