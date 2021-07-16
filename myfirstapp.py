import streamlit as st

import numpy as np
import pandas as pd
import time

st.header("My first Streamlit App")

option = st.sidebar.selectbox(
    'Select a mini project',
     ['line chart','map','T n C','Long Process'])


if option=='line chart':
    chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

elif option=='map':
    map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

    st.map(map_data)

elif option=='T n C':

    st.write('Before you continue, please read the [terms and conditions](https://www.gnu.org/licenses/gpl-3.0.en.html)')
    show = st.checkbox('I agree the terms and conditions')
    if show:
        st.write(pd.DataFrame({
        'Intplan': ['yes', 'yes', 'yes', 'no'],
        'Churn Status': [0, 0, 0, 1]
        }))


else:
    'Starting a long computation...'

    
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
   
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)

    '...and now we\'re done!'