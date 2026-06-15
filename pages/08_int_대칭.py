import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(layout="wide")

url1 = "https://www.geogebra.org/classic/tvzgwvbc"

components.html( f""" <iframe src="{url1}" width="100%" height="900" style="border:none; border-radius:12px;" allowfullscreen> </iframe> """, height=920 )

