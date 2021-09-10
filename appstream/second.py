import streamlit as st
import numpy as np
import pandas as pd
import time

# interativity using check box
if st.checkbox('Show Data Frame'):
    chart_data = pd.DataFrame(
        np.random.randn(20,3),
        columns=['A','B','C']
    )
    chart_data
st.write('Please check above box')

# select box
num = pd.DataFrame({'number':[1,2,3,4,5],})
option = st.selectbox(
    'Your favotire color?',
    num['number']
)
'result: ', option

option = st.sidebar.selectbox(
    'Which number do you like best?',
     num['number'])

'You selected:', option

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)
