import streamlit as st
from streamlit.components import v1 as st_comp

st.set_page_config(layout="wide", page_title="Intro")

st.title("Introduction")

st.markdown(
"""
# Read on to get a bit more detail on the LHC and ATLAS.
"""
)

st_comp.iframe(
src="https://opendata.atlas.cern/docs/documentation/introduction/introduction_ATLAS",
    height=3500,
    #width=8000,
    scrolling=True
)


st.markdown(
"""
# But why??
Although ATLAS is a technical marvel, it is **physical tool** to probe 
theory and models which otherwise may **seem** abstract. In a sense, it is
like a microscope used to zoom-in on the most fundamental of scales.
In so doing, physicists can begin to understand the Standard Model - 
particle physicists' version of the periodic table - and unravel some of 
its quirks and mysteries.
While a more humorous representation of new physics is given below, further
detail is provided in its own page.
"""
)

st.image("images/standard_model_changes_2x.png")

if st.button("Next page"):
  st.switch_page("pages/2_Essential_physics.py")
if st.button("Previous page"):
  st.switch_page("Welcome.py")
