import streamlit as st
from streamlit.components import v1 as st_comp

st.set_page_config(layout="wide", page_title="NNs")

st.title("Neural Networks")

st.header("What is a Neural Network?")
st.markdown("""
            A **neural network** is a machine learning model inspired by how the human brain processes information.

            It consists of layers of interconnected neurons. Each connection has a **weight**, and the network lerans by adjusting these weights
            during training.

            Neural networks and especially useful for tasks like:
            - Image recognition
            - Natural language processing
            - Speech recognition

            **POINT TO SOME BRIEF HISTORY ABOUT NEURAL NETWORKS INSTEAD OF WRITING ABOUT IT??**
            """)

st.header("Basic Structure")

st.header("Interactive Example")

st.header("Building a Neural Network with Python")

st.header("Applications of Neural Networks")

st.markdown("blah blah blah")




col1, col2 = st.columns(2)
with col1:
    if st.button("Previous page"):
        st.switch_page("pages/1_Intro.py")  # CAHNGE
with col2:
    if st.button("Next page"):
        st.switch_page("pages/3_<InsertPageName>.py")  # CHANGE