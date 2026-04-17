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

st.markdown("""

# What is classification?

A classification problem is any which can be formulated in the following
way:

**Given some known input features for some data, are we able to predict or
classify the category the data belongs to?**

Some examples could include:

- Given properties of an image, is it a cat or a dog?
- Given measurements of a sample, is it benign or malignant tissue?
- Given the details of a bank transaction, is it legitimate or fraud?
- Given information of an individual, are they a member of a target group
of interest for marketing, surveying, or intervention?
- Given details of a social group, are they a demographic of interest in
a social or medical study?
- **Given details of a property, what council tax band is it in?**

This differs from **regression** which instead are problems seeking to find
a continuous mapping to some output. In other words:
**Given some known input features for some data, are we able to predict the target's continuous value?**

e.g. **Given details of a property, how much is the property worth?**

![](images/regression-vs-classification.png)
A comparison between classification and regression. Left: an attempt to 
separate blue and green data is made by drawing a decision boundry. Right: 
an attempt to predict a continuous output is made by drawing a line of best
fit.

# The goal of classification
Stating the above in a slightly more formal and explicit way, the aim of 
classification is to **predict the correct category while minimising 
errors against the true categorisation**.
It's this second point which provides the true challenge of machine learning
categorisation: building a machine learning model which continues to behave
as expected when it encounters some new, unseen data. 

## Why bother?
It is understandable to be skeptical of machine learning or "AI" for these
purposes, especially if one is used to using more manual, traditional 
approaches to classifying data. However, like any tool, responsible use with
understanding of its strength and limitations can bring a world of good:

1. **Scalability** : Machine learning models scale very well for larger and larger datasets, even if the size starts becoming intractable for human-
driven processing.

2. **Consistency** : Whie some manual classification schemes may be simple,
they may be subject to certain human biases which may or may not change
depending on the day or datapoint. For example, a tired doctor may miss an 
important feature from an MRI and misclasify the image but a ML model is 
incapable of "getting tired."

3. **Caveat** : Yet, machine learning models are never infalible. The data 
they are trained on can inherit the same biases present in another other. 
Further, without proper care given to what a model is being optimised for,
one category may be classified more accurately than another, and models can
even fall victim of something called **overtraining** or **overfitting**.

4. **Adaptability** : While more "traditional" methods of classifying data 
may be easier to interpret, human interaction is limited by our capacity 
to visualise only two or three dimensions simultaneously. Just like plotting
data in 2D can provide more information than plotting each variable
separately in 1D, machine learning models are able to "see" data presented
in an arbitrary number of dimensions for every one of its features, thus
bringing increased categorisation ability with respect to the human mind.

""")

st.image("images/xkcd_ml.png", 
caption="""
An illustration of the "garbage in == garbage out" maxim which we must
always be mindful of in machine learning. "Garbage" can be as simple as 
poorly formatted or normalised data but can also be all the biases which one
puts into a model's training data. *xkcd 1838*.
"""
)

st.image("images/multidimPlot.png",
caption="""
An example of plotting in 1D vs 2D using the Iris dataset to show how the 
dimensionality of a feature space can leverage better separability in the 
data. Image by *kassambara*, https://www.sthda.com/.
"""
)

st.markdown(
"""
# Dream vs reality
While classification problems can usually be framed in a very 
straightforward manner, the reality is usualy a different situation.

Most trained classifier models will provide a result which can often be 
interpreted as the probability that given data belongs to a given class.
While solutions may aspire to have a perfect, extremely well-separated
output between, say, signal and background data...
"""
)
st.image("images/classification_hope.png")

st.markdown("""
...the reality is that most datasets are "messy", leading to less than 
perfect results.
""")

st.image("images/classification_reality.png")

st.markdown(r"""
The results of such classifications thus have to be assessed with an 
appreciation of true- and false-positive rates in mind (alternatively,
type-1 or $\alpha$ error and type-2 or $\beta$ classification errors).

Depending on the details of a particular classification problem, maximising
true-positives may be more important than minimising false-positives; 
alternatively, the objective may be to worry more about minimising type-1 
or type-2 errors.
""")
st.image("images/Type1_2_errors.png",
caption="""
An illustration of types of error when making a decision (classification) 
using an example taken from Loyola University Chicago Law Journal. 
52 (4): 1029.
""")

st.markdown(
"""
# Assessing a classifer model

## ROC curves
blah blah blah
""")

st.image("images/ROC_curves.png",
caption="""
TEST
""")

st.markdown(
"""
## Managing over- and under-training

blah blah blah

""")

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
