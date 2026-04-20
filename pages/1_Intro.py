import streamlit as st
from streamlit.components import v1 as st_comp

st.set_page_config(layout="wide", page_title="Intro")

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

st.title("AI & ML diversity")
col1, col2 = st.columns([0.7, 0.3])

with col1:
        st.image("assets/SusxHorizontal.jpg")
with col2:
        st.image("assets/ukri-epsrc-square-logo.png")

st.title("Introduction")

st.markdown(
"""
# Contents

### Classification
### Neural networks
### Clustering
### AI ethics

## What is not covered:

- Introductory statistics in "traditional" research or data problems
- Introductory coding in Python
- Full discussion on regression or generative machine learning ("GenAI")
- Large Language Models (LLMs) or chatbot models such as ChatGPT or Gemini

## What **is** covered:

This webapp is designed to be a brief introduction and tutorial into how 
machine learning can be used effectively and responsibly in research or 
other projects. 

It is **broad** in the sense that much of the conceptual discussion, 
especially on model design and optimisation, can be applied to a wide
range of machine learning models and data domains or scenarios.

It is **deep** in the sense that this tutorial focuses on tools and 
concepts for which the developers are best qualified to discuss: 
namely **supervised classification** and **unsupervised clustering**.
Machine learning models in these domains are well-established and 
have been used for a couple of decades across many disciplines.

At an extreme end, and one at which many may find a bit too far 
removed from their research use cases ("scary"?), classification and 
clustering are extremely important in physics problems involving 
*big data* such in astronomy, cosmology, and particle physics. 
In fact, the 2024 nobel prize in physics was awarded for the 
development of artificial neural networks widely in-use across these
physics problems today.
"""
)

st.image(
"images/Nobel2024.webp",
caption="© Johan Jarnestad/The Royal Swedish Academy of Sciences."
)

st.markdown(
"""
However, while these use cases are impressive, they represent only
a subset of the broad range of research problems which can be solved
using the machinary of "AI". 
As AI tools continue to be salient in research, industry, and personal
workflows, confidence in using machine learning is not only important
for "keeping up", but also because *responsible* use is powerful for 
enhancing ones work and conclusions. 

While this webapp doesn't try to provide solutions to combat misinformation
in broader society, it does seek to empower a relative newcomer with some 
of the skills needed to leverage the full power of machine learning.
"""
)

st.image(
"images/ClusteringExamplesIRL.png",
caption="Some of the very many use cases for machine learning in research and industry."
)

st.markdown(
"""
# A challenge for you: Can you think of a potential use-case of machine learning in your research?

## If you don't know, ask yourself if any of the following apply:

- I am working with a large dataset
- My dataset is complex - i.e. there are a large number of measurements or features which may or may not correlate with each other
- I want be able to predict or categorise my data into groups in a consistent way
- I want to see if there are any patterns within the dataset which I can't pick-out by eye
- I want to differentiate between 'normal' and 'abnormal' measurements
- I want to account for correlations between several features at once
- I am working with images, documents, tabular data, or anything which can be organised in a structured way

## If you answered "yes" to the above, it is very possible that you will be able to find a use for ML!
 
# What next?
It is recommended that this webapp is worked through in order (using the "next page" button) however
the sidebar can be used to navigate to specific pages if desired. 

If after working through this webapp you wish to do some further reading or 
hands on learning, we recommend the following resources:

## Further reading: 

- [Kaggle challenges & competitions for getting hands on practice](https://www.kaggle.com)
- [Scikit-learn documentation can be a very useful primer](https://scikit-learn.org/stable/)
- [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)
- [W3Schools can be incredibly useful for introductory development of Python programming](https://www.w3schools.com/python/)
- [Brilliant provides some fun exercises for learning a range of skills](https://brilliant.org/topics/python/)
- [Including statistics for data science](https://brilliant.org/topics/statistics/)

This is in addition to library-stocked resources which are plentiful and well-used.  
Also **do not** be afraid to find a friend or colleague to discuss anything through.
Most researchers or ML experts are too happy to help. 
"""
)

if st.button("Next page"):
  st.switch_page("pages/2_Classification.py")
if st.button("Previous page"):
  st.switch_page("Welcome.py")
