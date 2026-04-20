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

st.title("AI & ML diversity")
col1, col2 = st.columns([0.7, 0.3])

with col1:
        st.image("assets/SusxHorizontal.jpg")
with col2:
        st.image("assets/ukri-epsrc-square-logo.png")

st.title("Clustering problems in machine learning")

st.markdown(
r"""
# What is clustering?

Clustering is an *unsupervised* technique used to group (cluster) data 
based on similarities within the feature space $X$. Unlike classification and
regression, this means that data does not have to be labelled with some
output or target $Y$. This is what makes clustering especially powerful in 
cases where the data cannot be labelled, either because we want to extract
something *new* from the data or because there are practical limitations
with labelling the dataset (e.g. it is too large). 

A visualisation of three-way clustering in two dimensions is shown below:
"""
)

st.image(
"images/clustering_example.png",
caption=
"""Unlabelled data in a hypothetical heathcare context clustered into 
three groups. Image from Google.
"""
) 

st.markdown(
r"""
# Why is it useful?

## Grouping & segmentation
Some data science or research problems may require or can be made easier if
the data is grouped or **segmented** into smaller subsets. Each group may
have enough in common that they can each be labelled and subsequently dealt 
with separately. Alternatively, such segmentation can be useful for 
identifying broader trends across the feature space.

From the other side, clusters may be constructed using a *hierarchical* 
modelling which can show how more granular data clusterings relate to each
other and in relation to larger, more general clusters of relationships.

## Dimensionality reduction
Real world data can be messy or complicated. More specifically data can 
possess high degrees of non-linearities or overlaps. Even if data is 
labelled $Y$, such complexity can be difficult during development of 
solutions for providing predictions of the target $\bar{Y}$. 
However, various clustering techniques can make fuller use of the 
feature space (potentially in very large number of features or dimensions) 
and potentially provide an additional handle for separating the data out
in subsequent analysis. 
In a sense, the clustering across a large number of dimensions is thus
reduced to a 1D distribution - "what cluster is this?". 
It isn't *strictly* the same as dimensionality reduction, but results can be
similar.
"""
)

st.image(
"images/DimRed.png",
caption="""
Unsupervised learning compared between clustering and dimensionality
reduction. 
Taken from A Perspective on Machine Learning Methods in Turbulence Modelling,
Beck, A D & Kurz, M. DOI:10.13140/RG.2.2.17469.69608.
"""
)

st.markdown(
r"""
## Anomaly detection
When analysing data, sometimes it is useful to understand what is 'normal' 
in the situation. Although traditional statistics equips researchers with 
tools for identifying anomalies, it can become harder as the number of 
features increases. Clustering allows us to identify 'normal' and 
'anomalous' data in very high dimensions. It can also be used for identifying
anomalies against several 'normal' groups of data within the feature space. 
"""
)

st.image(
"images/AnomalyDetection.png",
caption="""
Examples of anomaly (red) detection in 2D against several 'normal' 
clusters (blue). Taken from Deep-Compact-Clustering Based Anomaly Detection Applied to Electromechanical Industrial Systems, Arellano-Espita, F. et al.
DOI:10.3390/s21175830.
"""
)

st.markdown(
r"""
# Real world examples
Clustering has become such a standard part of the machine learning toolbox
that we don't always notice that it is there. Some examples include the 
following:

- Identifying spam emails
- Fraud detection in finance or cybersecurity
- Identifying healthy and unhealthy cells in cultures
- Functional MRI studies
- Streaming service recommendations and tailored social media advertising
- Facial and biometrics recognition
- Social network identification and analysis

## How many do you recognise? Can you think of any more?
"""
)

st.image(
"images/ClusteringExamplesIRL.png",
caption="""
An overview of some of the many ways in which clustering is used
in industry and research.
"""
)

st.title("Over to you!")

st.markdown("""

## Can you determine a useful clustering of data within the Iris dataset? Perhaps even use it to aid classification?

This tutorial will guide you through the fundamentals of doing clustering in scikit-learn. While it may give you the tools you need to get started, you 
are encouraged to do your own research and to play around in the tutorial to get the most out of it.

Click the link to access the tutorial on Binder:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cly20/ml_clustering_tutorial/HEAD?urlpath=%2Fdoc%2Ftree%2FIrisClustering.ipynb)

""")


if st.button("Next page"):
  st.switch_page("pages/5_AI_Ethics.py")
if st.button("Previous page"):
  st.switch_page("pages/3_Neural_Networks.py")
