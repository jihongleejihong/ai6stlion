import streamlit as st
import pandas as pd

x = np.arange(0, 9, 0.1)
df = pd.DataFrame({'x' : x, 'sin_x' : np.sin(x)})

df
