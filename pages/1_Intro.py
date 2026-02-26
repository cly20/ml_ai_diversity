import streamlit as st
from streamlit.components import v1 as st_comp

st.set_page_config(layout="wide", page_title="Intro")

st.title("Introduction")

st.markdown(
"""
# Read on to get a bit more detail on the LHC and ATLAS.
"""
)

#st.image("InsertImageHere")
#st.video("InsertVideoHere")
#st_comp.iframe(src="Insert URL or local-host path to web-app in iframe",
    #height=1000,
    #width=800,
    #scrolling=True
#)

if st.button("Next page"):
  st.switch_page("pages/2_<InsertPageName>.py")
if st.button("Previous page"):
  st.switch_page("Welcome.py")
