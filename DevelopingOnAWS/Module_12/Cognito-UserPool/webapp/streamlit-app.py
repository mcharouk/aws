import streamlit as st
import sys
import os

# Add the current directory to Python path for imports
sys.path.append(os.path.dirname(__file__))

st.set_page_config(
    page_title="Home",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Define pages manually
pages = {
    "Home": "app.py",
    "Page 2": "menu/page_2.py",
    "Page 3": "menu/page_3.py",
    "Settings": "menu/settings.py"
}

# Create navigation
page_names = list(pages.keys())
page_files = list(pages.values())

# Create page objects for st.navigation
page_objects = []
for name, file_path in pages.items():
    page_objects.append(st.Page(file_path, title=name))

pg = st.navigation(page_objects)

pg.run()
