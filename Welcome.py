import streamlit as st
from streamlit.components import v1 as st_comp


st.set_page_config(
    layout="wide",
    page_title="Hello",
    page_icon="👋",
)

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

st.title("AI & ML diversity")

st.markdown("# Welcome! 👋")

col1, col2 = st.columns([0.7, 0.3])

with col1:
	st.image("assets/SusxHorizontal.jpg")
with col2:
	st.image("assets/ukri-epsrc-square-logo.png")

st.markdown(
"""
A warm welcome to this webapp aimed to introduce you to some of the 
fundamentals of AI and machine learning (ML). As part of broader work 
at Sussex, we hope this guides you through enough of the fundamentals to 
debunk some of the misconceptions and fears and to equip you with some of
the key skills and knowledge to get you started for your own research 
projects.

## Credits:
Part of an ESPRC-funded project on AI & ML diversity led by Dr Alice King
at the University of Sussex.

- Caley Yardley, lead developer
- Eva Sabater-Andres, content developer (neural networks)
- Lauren McMahon, content developer (AI ethics) 
"""
)

if st.button("Next page"):
  st.switch_page("pages/1_Intro.py")
