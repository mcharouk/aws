import streamlit as st
from st_pages import add_page_title, get_nav_from_toml

st.set_page_config(
    page_title="Home",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded",
)

nav = get_nav_from_toml(".streamlit/pages.toml")

pg = st.navigation(nav)

add_page_title(pg)

pg.run()
