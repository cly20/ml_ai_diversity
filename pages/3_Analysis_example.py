import streamlit as st
from streamlit.components import v1 as st_comp

st.set_page_config(layout="wide", page_title="Example physics analysis")

st.title("Let's look for some dark matter!!!")

st.markdown(
"""
Putting together everything we have looked at thus far, let's take a look
at an example exercise doing **cut-and-count** analysis to search for 
**dark matter**.

**Note: you may wish to minimise the sidebar to give yourself a clearer view
of the tutorial**
"""
)

st_comp.iframe(
   src="https://histogram-analyser-dark-matter-atlas-open-data.app.cern.ch/main",
   height=1800,
   scrolling=True
)

st.markdown(
"""
# What next?
While the above type of analysis has been and continues to be powerful for
making some measurements at the LHC (such as measurements of the *Z*-boson),
we have seen that some physics signatures are difficult to find in this
way because they are small and/or too similar (by eye) to backgrounds.
Therefore, physicists can use a powerful friend to gain more sensitivity to new physics:
## machine learning!!
Have a play on the next page.
"""
)

if st.button("Next page"):
  st.switch_page("pages/4_Machine_Learning.py")
if st.button("Previous page"):
  st.switch_page("pages/2_Essential_physics.py")
