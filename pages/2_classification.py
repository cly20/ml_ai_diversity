import streamlit as st
from streamlit.components import v1 as st_comp

st.set_page_config(layout="wide", page_title="classification")

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

st.title("Classification problems in machine learning")


st.title("Over to you!")

st.markdown("""

## Can you train a model to determine whether a passenger survived the Titanic disaster or not?

This tutorial provides a very brief rundown of how to use machine learning for
classification in python. This tutorial uses scikit-learn because of its relative simplicity.

While you should be able to get started very quickly, you are encouraged to consider the steps
more carefully to ensure a robust result.

To access the tutorial, click the link to take you to Binder:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cly20/ml_classification_tutorial/HEAD?urlpath=%2Fdoc%2Ftree%2FTitanicClassification.ipynb)

""")

if st.button("Next page"):
  st.switch_page("pages/3_nn.py")
if st.button("Previous page"):
  st.switch_page("pages/1_Intro.py")
