import streamlit as st
from streamlit.components import v1 as st_comp

st.set_page_config(layout="wide", page_title="clustering")

#Style setting
st.markdown("""
    <style>
    .stMarkdown p {
        font-size: 22px;
    }
    </style>

    <style>
    /* Slider labels */
    .stSlider label {
        font-size: 18px !important;
    }

    /* Selectbox labels */
    .stSelectbox label {
        font-size: 18px !important;
    }

    /* General widget labels fallback */
    label {
        font-size: 18px !important;
    }
    </style>

    <style>
    /* Slider tick/value text */
    .stSlider div[data-baseweb="slider"] {
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Clustering problems in machine learning")


st.title("Over to you!")

st.markdown("""

## Can you determine a useful clustering of data within the Iris dataset? Perhaps even use it to aid classification?

This tutorial will guide you through the fundamentals of doing clustering in scikit-learn. While it may give you the tools you need to get started, you 
are encouraged to do your own research and to play around in the tutorial to get the most out of it.

Click the link to access the tutorial on Binder:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cly20/ml_clustering_tutorial/HEAD?urlpath=%2Fdoc%2Ftree%2FIrisClustering.ipynb)

""")


#if st.button("Next page"):
  #st.switch_page("pages/3_nn.py")
if st.button("Previous page"):
  st.switch_page("pages/3_nn.py")
