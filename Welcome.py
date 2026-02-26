import streamlit as st
from streamlit.components import v1 as st_comp


st.set_page_config(
    layout="wide",
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome! 👋")

st.image("assets/SusxHorizontal.jpg")

st.markdown(
"""
A very warm welcome to the University of Sussex from the Experimental Particle Physics Research Group!
We hope that this brief tutorial will provide you with a taster of the kind of work and projects we do
to study the Universe at the smallest of scales - empowered by **machine learning** to get the most out
of our experiments.

At Sussex, particle physicists are involved on several experimental
collaborations ranging from smaller groups such as LiquidO, to larger teams 
such as DUNE (deep underground neutrino experiment) and ATLAS. 
This tutorial will focus on physics, data analysis, and machine learning
through the lens of collider physics done by ATLAS at the LHC. However, 
a lot of the concepts are broadly similar between different experiments.
"""
)

st.image("images/NoVa.jpeg", caption="An inside view of NoVa while under construction.")
st.image("images/DUNE.jpg", caption="A diagramatic view of DUNE.")

st.markdown(
"""
Insert introductory text background yadayadayada
"""
)


if st.button("Next page"):
  st.switch_page("pages/1_Intro.py")
