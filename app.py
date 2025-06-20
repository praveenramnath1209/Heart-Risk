# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KhDaUw9o3MnQMAuljuE1C5S6pdCcDX7u
"""

import streamlit as st
import pickle
import numpy as np

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title('Heart Risk Prediction')

BP = st.number_input('Enter Blood Pressure',format='%.2f')
CH = st.number_input('Enter Cholesterol',format='%.2f')

if st.button('Predict'):
  data = np.array([[BP,CH]])
  pred = model.predict(data)
  if pred[0] == 0:
    st.success('Low Risk')
    st.balloons()
  else:
    st.error('High Risk')
