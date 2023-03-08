import app
import hom

import streamlit as st

pages={"Make a prediction": app,
       "Add new patient":hom}


st.sidebar.title('Explore')
selection = st.sidebar.radio("go to",list(pages.keys()))
page = pages[selection]
page.app()
