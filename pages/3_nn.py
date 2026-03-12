import streamlit as st
from streamlit.components import v1 as st_comp

st.set_page_config(layout="wide", page_title="NNs")

st.title("Neural Networks")

st.markdown("blah blah blah")

if st.button("Next page"):
  st.switch_page("pages/3_<InsertPageName>.py")
if st.button("Previous page"):
  st.switch_page("pages/1_Intro.py")