import streamlit as st
from streamlit.components import v1 as st_comp
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(layout="wide", page_title="NNs")

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

            """)


st.header("Basic Structure")

st.markdown("""

            A neural network is made up of several core components that work together to process information and learn patterns. Neural networks are organised into layers of **nodes** (neurons). The **input layer** receives the raw data, then come the **hidden layers** where most of the computation happens, and finally the final prdiction is produced by the **output layer**. The following image shows the structure of a simple neural network with one hidden layer:

            """)

st.image("images/simple_NN_1hiddenlayer.jpg")

st.markdown("""
            In the diagram above:
            - Blue nodes represent inputs  
            - Green nodes are hidden neurons where computation happens  
            - The orange node produces the final output

            Nodes are like small decision units which take an input, apply **weigths** and add a **bias**. They then pass the result through an **activation function**. Each line between nodes represents a weighted connection which determines how important one neuron’s output is to the next neuron. When a neural network is "learning" these weights are adjusted. A bias is an extra value added to a neuron. It helps the model adjust and improves flexibility (like shifting a line up or down). After combining inputs, a neuron passes the result through an activation function. This decides whether the neuron “fires” and introduces non-linearity. Non-linearity is crucial for neural networks because it allows them to model complex, real-world patterns that are not simply linear. There common activation functions used are:
            - ReLU (Rectified Linear Unit)
            - Sigmoid
            - Tanh
            
            In addition, neural networks use a **loss function** to measure how far the model’s prediction is from the actual answer. The goal of training is to minimize this error. The weights and biases are updated using an optimiser reducing the loss.
            """)

st.markdown("""
            One can think of a neural network like a decision-making system:

            1. Inputs (numbers) go into the network  
            2. Each neuron combines inputs using weights and bias  
            3. The result is passed through an activation function  
            4. This continues layer by layer  
            5. The final layer produces a prediction  

            During training:
            - The model makes a prediction
            - It checks how wrong it was (loss)
            - It adjusts itself to improve next time
            """)

st.markdown("""
            #### Neural Networks vs the Human Brain

            Neural networks are inspired by how the human brain works, but they are much simpler.
            """)

data = {
    "Aspect": [
        "Neuron Function", 
        "Learning Process", 
        "Connections", 
        "Processing Speed", 
        "Energy Consumption", 
        "Flexibility"
    ],
    "Biological Brain": [
        "Neurons process signals through dendrites, cell body, and axons.",
        "Learning through strengthening/weakening synapses (synaptic plasticity).",
        "Neurons are connected in highly complex, dynamic networks.",
        "Much slower (milliseconds per signal), but massively parallel.",
        "Very energy efficient (about 20 watts for the whole brain).",
        "Extremely flexible, capable of generalizing across tasks."
    ],
    "Artificial Neural Network": [
        "Artificial neurons compute weighted sums of inputs and apply an activation function.",
        "Learning via gradient descent (adjusting weights and biases) during training.",
        "Connections (weights) are adjustable, but simpler and more static.",
        "Much faster in terms of computational power, especially on GPUs/TPUs.",
        "Requires much more energy (high computational demand, large data centers).",
        "Less flexible than the brain, struggles with tasks outside its training."
    ]
}
df = pd.DataFrame(data)
st.table(df)

st.subheader("Vectors and Matrices")

st.markdown(r"""
            While we’ve described neural networks in terms of individual neurons and connections, computers don’t actually process them one neuron at a time.

            Instead, entire layers are computed all at once using vectors and matrices. This allows neural networks to run efficiently using optimized linear algebra operations. Layers are defined as vectors, $X$, where each node is component of the vector; wieights are the elements of a matrix, $W$. Each layer then computes

            """)
st.latex(r'''
        X \cdot W + b
        ''')
st.markdown("""
            where $b$ is the bias vector.

            Below is an interactive function where you can set the values of the vector $X$ and matrix $W$ by simply tiping the values. You will see that the vector/matrix on the left will be updated with the new values. And The output shows the result of the dot procuct between $X$ and $W$.
            """)

def to_latex_vector(vec):
    return r"\begin{bmatrix}" + r" \\ ".join(map(str, vec)) + r"\end{bmatrix}"
def to_latex_matrix(mat):
    rows = [" & ".join(map(str, row)) for row in mat]
    return r"\begin{bmatrix}" + r" \\ ".join(rows) + r"\end{bmatrix}"
vector_df = pd.DataFrame({"X": [1.0, 2.0]})
col1, col2, col3, col4 = st.columns([3, 1, 1, 3])
with col3:
    vector_df = st.data_editor(vector_df, num_rows="fixed", hide_index=True)
X = vector_df["X"].values
with col2:
    st.latex(r"X = " + to_latex_vector(X))
matrix_df = pd.DataFrame([
    [1.0, 0.5],
    [-1.0, 2.0]
])
col1, col2, col3, col4 = st.columns([2, 1, 1, 2])
with col3:
    matrix_df = st.data_editor(matrix_df, num_rows="fixed", hide_index=True)
W = matrix_df.values
with col2:
    st.latex(r"W = " + to_latex_matrix(W))
result = X @ W
st.write("Output:")
st.latex(rf"""
X \cdot W = {to_latex_vector(X)} \cdot {to_latex_matrix(W)} = {to_latex_vector(result)}
""")





st.header("Interactive Example: Learn Like a Neural Network")

st.markdown(r"""
            We have now learned the basic structure of a neural network, and we can strat seing how they are build and how to train them.

            In this interactive example, you will act like a neural network and learn step by step.

            We will use a simple model:

            $$y = w x + b$$

            Your goal is to adjust **w (weight)** and **b (bias)** so that your model matches the true data.

            ---

            ### What to do:
            1. Move the sliders to change the model  
            2. Watch how the prediction line changes  
            3. Try to reduce the loss  
            4. Then let the computer learn automatically 🚀
            """)

# Create training data
x_train = np.linspace(-5, 5, 100)
y_true = 2 * x_train + 1   # True function (unknown to user)

# Session state (VERY IMPORTANT)
if "w" not in st.session_state:
    st.session_state.w = 0.0
if "b" not in st.session_state:
    st.session_state.b = 0.0

# Sliders (manual control)
st.subheader("Step 1: Make a Prediction")

col1, col2 = st.columns(2)

with col1:
    st.session_state.w = st.slider("Weight (w)", -5.0, 5.0, st.session_state.w, step=0.1)

with col2:
    st.session_state.b = st.slider("Bias (b)", -5.0, 5.0, st.session_state.b, step=0.1)

# Prediction
y_pred = st.session_state.w * x_train + st.session_state.b

# Plot prediction vs truth
st.subheader("Step 2: Compare Prediction vs Reality")

fig, ax = plt.subplots()
ax.plot(x_train, y_true, label="True function (target)")
ax.plot(x_train, y_pred, label="Your model", linestyle="--")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
ax.set_title("Try to match the lines!")
st.pyplot(fig)

# Loss calculation
loss = np.mean((y_true - y_pred) ** 2)

st.subheader("Step 3: Measure Error (Loss)")

st.markdown("""
We measure how wrong the model is using **Mean Squared Error (MSE)**:

Lower loss = better model
""")

st.metric("Current Loss", f"{loss:.4f}")

st.info("👉 Try to reduce the loss using only the sliders!")

# Learning section
st.subheader("Step 4: Let the Model Learn Automatically")

st.markdown("""
Instead of adjusting manually, neural networks **learn automatically** using gradient descent.

This means:
- Compute how wrong we are
- Adjust w and b to reduce the error
""")

lr = st.slider("Learning rate", 0.001, 0.1, 0.01)

# One training step
if st.button("Train one step"):
    grad_w = np.mean(2 * (y_pred - y_true) * x_train)
    grad_b = np.mean(2 * (y_pred - y_true))

    st.session_state.w -= lr * grad_w
    st.session_state.b -= lr * grad_b

    st.success("Model updated! Watch the line move.")

# Train multiple steps
if st.button("Train 50 steps"):
    for _ in range(50):
        y_pred = st.session_state.w * x_train + st.session_state.b

        grad_w = np.mean(2 * (y_pred - y_true) * x_train)
        grad_b = np.mean(2 * (y_pred - y_true))

        st.session_state.w -= lr * grad_w
        st.session_state.b -= lr * grad_b

    st.success("Model trained for 50 steps!")

# Reset button
if st.button("Reset model"):
    st.session_state.w = 0.0
    st.session_state.b = 0.0
    st.success("Model reset!")

# Explanation
st.subheader("Step 5: What Just Happened?")

st.markdown("""
You just trained a neural network 🎉

Here's what happened:
- The model made predictions
- It measured how wrong it was (loss)
- It adjusted w and b to improve
- It repeated this process

This is exactly how real neural networks work—just with many more parameters!
""")


st.subheader("Activation Function Explorer")
st.markdown("""
Activation functions introduce **non-linearity**, allowing neural networks to learn complex patterns.

👉 Try switching between functions and observe:
- Shape of the curve
- Where outputs saturate (flatten)
- Whether negative values are allowed
""")
x = np.linspace(-10, 10, 200)
activation = st.selectbox(
    "Choose activation function",
    ["ReLU", "Sigmoid", "Tanh", "Leaky ReLU"]
)
if activation == "ReLU":
    y = np.maximum(0, x)
    explanation = "ReLU outputs 0 for negative values and grows linearly for positive values."
elif activation == "Sigmoid":
    y = 1 / (1 + np.exp(-x))
    explanation = "Sigmoid squashes values between 0 and 1 (useful for probabilities)."
elif activation == "Tanh":
    y = np.tanh(x)
    explanation = "Tanh outputs values between -1 and 1, centered around zero."
elif activation == "Leaky ReLU":
    y = np.where(x > 0, x, 0.1 * x)
    explanation = "Leaky ReLU allows small negative values instead of cutting them off."
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title(activation)
st.pyplot(fig)
st.info(explanation)

st.subheader("Loss Landscape")
st.markdown("""
This plot shows how the **loss changes** for different values of weight (w) and bias (b).

👉 Think of this like a landscape:
- High areas = high error ❌  
- Low areas = low error ✅  

Training a neural network = **rolling downhill to the lowest point**
""")
w_vals = np.linspace(-3, 3, 50)
b_vals = np.linspace(-3, 3, 50)
W, B = np.meshgrid(w_vals, b_vals)
loss_grid = np.zeros_like(W)
x_train = np.linspace(-5, 5, 100)
y_true = 2 * x_train + 1
for i in range(W.shape[0]):
    for j in range(W.shape[1]):
        y_pred = W[i, j] * x_train + B[i, j]
        loss_grid[i, j] = np.mean((y_true - y_pred) ** 2)
fig, ax = plt.subplots()
contour = ax.contourf(W, B, loss_grid, levels=100)
plt.colorbar(contour)
ax.set_xlabel("Weight (w)")
ax.set_ylabel("Bias (b)")
ax.set_title("Loss Landscape")
st.pyplot(fig)
st.info("👉 The lowest point on this plot is where the model performs best.")


st.header("Two-Layer Neural Network")
st.markdown("""
Now let's go beyond a single line.

This model has:
- **1 input**
- **1 hidden layer (with neurons)**
- **1 output**

👉 This allows the model to learn **curved / complex patterns**
""")
# Data (non-linear!)
x = np.linspace(-5, 5, 200)
y_true = np.sin(x)
# Controls
hidden_neurons = st.slider("Number of hidden neurons", 1, 10, 3)
lr = st.slider("Learning rate", 0.001, 0.1, 0.01, key="lr2layerNN")
# Initialize weights (store in session)
if "W1" not in st.session_state:
    st.session_state.W1 = np.random.randn(hidden_neurons)
    st.session_state.b1 = np.zeros(hidden_neurons)
    st.session_state.W2 = np.random.randn(hidden_neurons)
    st.session_state.b2 = 0.0
# Resize safely if slider changes
if len(st.session_state.W1) != hidden_neurons:
    st.session_state.W1 = np.random.randn(hidden_neurons)
    st.session_state.b1 = np.zeros(hidden_neurons)
    st.session_state.W2 = np.random.randn(hidden_neurons)
# Forward pass
def relu(z):
    return np.maximum(0, z)
z1 = np.outer(x, st.session_state.W1) + st.session_state.b1
a1 = relu(z1)
y_pred = a1 @ st.session_state.W2 + st.session_state.b2
# Loss
loss = np.mean((y_true - y_pred) ** 2)
fig, ax = plt.subplots()
ax.plot(x, y_true, label="True function")
ax.plot(x, y_pred, label="Neural network", linestyle="--")
ax.legend()
ax.set_title("Learning a Non-Linear Function")
st.pyplot(fig)
st.metric("Loss", f"{loss:.4f}")
# Training step
if st.button("Train network"):
    for _ in range(50):
        # Forward
        z1 = np.outer(x, st.session_state.W1) + st.session_state.b1
        a1 = relu(z1)
        y_pred = a1 @ st.session_state.W2 + st.session_state.b2

        # Gradients (simplified backprop)
        dloss = 2 * (y_pred - y_true) / len(x)

        dW2 = a1.T @ dloss
        db2 = np.sum(dloss)

        da1 = np.outer(dloss, st.session_state.W2)
        dz1 = da1 * (z1 > 0)

        dW1 = (dz1 * x[:, None]).sum(axis=0)
        db1 = dz1.sum(axis=0)

        # Update
        st.session_state.W1 -= lr * dW1
        st.session_state.b1 -= lr * db1
        st.session_state.W2 -= lr * dW2
        st.session_state.b2 -= lr * db2

    st.success("Network trained!")


st.header("Neural Network Visualisation")
st.markdown("""
This diagram shows how inputs flow through the network.

👉 Thickness of lines ≈ strength of weights  
👉 Each node = a neuron
""")
fig, ax = plt.subplots()
input_nodes = [(-1, 0)]
hidden_nodes = [(0, i) for i in range(-1, 2)]
output_nodes = [(1, 0)]
for (x0, y0) in input_nodes:
    ax.scatter(x0, y0)

for (x0, y0) in hidden_nodes:
    ax.scatter(x0, y0)

for (x0, y0) in output_nodes:
    ax.scatter(x0, y0)
for h in hidden_nodes:
    ax.plot([-1, h[0]], [0, h[1]])

for h in hidden_nodes:
    ax.plot([h[0], 1], [h[1], 0])

ax.set_title("Simple Neural Network Structure")
ax.axis("off")

st.pyplot(fig)

st.info("""
👉 In real neural networks:
- Each connection has a weight
- Training adjusts these weights
- Stronger weights = more influence
""")



st.header("Bilding a Neral Network from Scratch in Pyhton")
st.markdown("""
            Now it's your turn to build a neural network from scratch using Python!

            Click below to open the guided notebook:
            """)

st.link_button(
    "🚀 Open Notebook (your own copy)",
    "https://colab.research.google.com/drive/1Wqi3-ijbr-MIyZjpvuNx6VLR7FvohQDZ?copy=true"
)


col1, col2 = st.columns(2)
with col1:
    if st.button("Previous page"):
        st.switch_page("pages/2_Classification.py")  # CAHNGE
with col2:
    if st.button("Next page"):
        st.switch_page("pages/4_Clustering.py")  # CHANGE
