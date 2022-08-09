import streamlit as st
import pandas as pd
import numpy as np

st.header('sine(x) & cosine(x)')

x = np.arange(0, np.pi * 4, 0.1)
df = pd.DataFrame({'x' : x, 'sin_x' : np.sin(x), 'cos_x' : np.cos(x)})

df
