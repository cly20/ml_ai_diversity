import streamlit as st
from streamlit.components import v1 as st_comp

st.set_page_config(layout="wide", page_title="Try some machine learning")

st.title("Machine learning meets physics")

st.markdown("""
What is Machine Learning?
Machine learning is a way for computers to learn patterns from data.
Unlike humans, they machine learning models allows computers to "learn"
more complicated relationships (e.g. correlations and clusterings) faster
across several variables at once. 

## Remember this from school?
In effect, while human brains can typically visualise **one dependent 
variable** at a time against an *independent variable*, machine learning
provides an apparatus through which computers can examine **many dependent
variables** at the *same time*.

## Hands on!
The tutorial below gives you a flavour of one machine learning model called 
a **neural network** which we have trained to search of dark matter.
You should see that depending on the **hyperparameters** which define it, 
the neural network may perform better or worse at looking for dark matter.

Over to you!

**Note: you may wish to minimise the sidebar to provide you more scree 
space for the tutorial.**
""")

st.header("Interactive ML Application")

st_comp.iframe(
    src="https://ml-visual-dashboard-atlas-open-data.app.cern.ch",
    height=5000,
    width=8000,
    scrolling=True
)

if st.button("Previous page"):
  st.switch_page("pages/3_Analysis_example.py")
