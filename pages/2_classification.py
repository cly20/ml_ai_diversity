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
""",
width=400
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
r"""
# Assessing a classifer model

## ROC curves
In a binary classification problem, any result contains some inherent rate
of drawing false positives in addition to desirable true positives.
Using this understanding allows us to assess the effectiveness of a 
machine learning classifier using a receiver operator characteristic or 
**ROC curve**.

The figure below demonstrates how this metric relates to the output of some 
classifer model. 
Let's assume a machine learning classifier has been trained and assigns 
some score $x$ to some data. This score then needs to be used to
differentiate between "positive" $Y=1$ and "negative" $Y=0$ datapoints.
In order to use this score $x$, some selection boundary (green line) has
to be decided to convert this score into a predicted classification 
$\bar{Y}$.

In a dream world, it is possible to choose a boundary such that $\bar{Y}=Y$
for **all** data passing through the model. Unfortunately, the reality is 
that for any choice of boundary in the model's output, there is some chance
that
1. not all true positives $\bar{Y}=Y=1$ are selected (TPR$<100\%$)
2. some false postives $\bar{Y}=1,~Y=0$ are selected (FPR$>0\%$)

where such true- and false-positive rates depend on how aggressive the 
decision boundary is.

Therefore, ROC curves provide a visual tool for assessing how well a ML
classifier performs at separating the data. The closer an ROC curve is to
the upper-left corner, the better the model is expected to perform. The
closer it is to the diagonal line, the closer the model is to behaving as
a random selection corner, the better the model is expected to perform. The
closer it is to the diagonal line, the closer the model is to behaving as
a random selection.

Depending also on the shape of the ROC curve, a decision may also be made
regarding how aggressively to apply the classifier's output, in addition to
deciding whether to seek further optimisations through the choice of model
hyperparameters (discussed in linked tutorial at bottom of page). 
""")

st.image("images/ROC_curves.png",
caption="""
An illustration of an ROC curve (lower) in relation to data with a positive
and negative target label.
Upper left: A bimodal distribution of positive (red) and negative (blue) 
data as a function of some variable $x$. The vertical green line indicates 
a choice of selection along the $x$-axis to define a prediction $\bar{Y}$. 
For any choice, it is possible to compare this against the truth label $Y$
and calculate the true- and false-positive rates.
Upper right: A confusion matrix showing the relationship between predicted 
and truth labels and the following rates: true- and false-positive (TP, FP)
& false- and true-negative (FN, TN).
Lower: The ROC curve is plotted by scanning the selection boundary in the 
upper left plot across all possible choices - between fully exclusive and 
fully inclusive. Random selection (flat 50% probability) is shown in the
diagnonal straight line while increasingly powerful selections have their 
ROC close to the upper left of the axes.
Image by kakau, Wikipedia Commons.
""")

st.markdown(
"""
## Managing over- and under-training
Let's assume we've developed a model which we believe to be optimised for 
our purposes according to the above. Its performance on the seen training
data is very strong so we now want to apply the model to some new, unseen
data. 

### Can we be certain that the model is robust and will behave consistently?

**In general, not unless we have tested for for overtraining.**

It is possible for a trained classifier to behave amazingly for
its training data but then behave inconsistently for new, unseen data. In
particular, we are concerned with the model behaving **overaggresively**
based on the data it has been trained with such that it no longer fits
more general patterns observable in unseen data. 
An example of **overtraining** or **overfitting** is shown below:
""")

st.image("images/overfitting.png",
caption="""
An illustration of overfitting inherent to using finite datasets during
training.
""")

st.markdown(
r"""
As a result of models being developed using only a *finite* dataset, there
is always a risk that a model identifies "patterns" among the data which 
vanish when more data is introduced. 
This is why it is *essential* to test machine learning classifiers on some
data which wasn't used during training - called a *test dataset*. Typically
a known, labelled dataset is split such that the majority is used to *train*
while a minority ($10-20\%$) is used for testing. 

If a classifier behaves
the same with the test dataset as the train dataset, this indicates that 
the model is robust; i.e. we can be confident that it'll behave in a 
well-defined way when used for its intended purpose. 

If a classifier behaves differently between the two datasets, this indicates
**overtraining** and suggests that the model will not behave in a 
well-understood way *in-situ*. The solution is to revisit how the model is 
setup and start training again.

### Hyperparameter optimisation

If metrics such as the accuracy or ROC curve indicate **undertraining** 
- a model behaving poorly as a result of it not "making the most" of the 
train dataset - or if comparison between train and test datasets indicate 
**overtraining**, the **hyperparameters** which define the model's behaviour
have to be reconsidered.

These are tuneable parameters that define the machine learning architecture
and how the model evolves during training. Examples include:

- The choice of model itself
- The depth of a decision tree
- The number of hidden layers in a neural network
- The choice of optimisation function used at various points in a model

A simple rule-of-thumb to understand what a hyperparameter is when it comes
to coding-in a model is this:
**If it is an adjustable parameter during a machine learning model's 
initialisation, it is probably a hyperparameter.**
 
""")

st.title("Over to you!")

st.markdown("""

## Can you train a model to determine whether a passenger survived the 
Titanic disaster or not?

This tutorial provides a very brief rundown of how to use machine learning 
for classification in python. This tutorial uses scikit-learn because of its 
relative simplicity.

While you should be able to get started very quickly, you are encouraged to 
consider the steps more carefully to ensure a robust result. Keep in mind the
discussions above.

To access the tutorial, click the link to take you to Binder:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cly20/ml_classification_tutorial/HEAD?urlpath=%2Fdoc%2Ftree%2FTitanicClassification.ipynb)

""")

if st.button("Next page"):
  st.switch_page("pages/3_nn.py")
if st.button("Previous page"):
  st.switch_page("pages/1_Intro.py")
