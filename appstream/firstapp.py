import streamlit as st
import numpy as np
import pandas as pd

st.title('안녕하세요 크롱엄마입니다.^^')

st.write('Data Frame을 구성, 테이블을 만들어봅시다')
st.write(pd.DataFrame({
    'col1':[1,2,3,4],
    'col2':[10,20,30,40] 
}))

# Use magic by python doc 
'''
Data Frame을 구성, 테이블을 만들어봅시다.^^

'''
df = pd.DataFrame({
    '학번': [2001,2002,2003],
    '성명': ['고이헌','고서하','고남관']
})
df

# chart
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['A','B','C']
)

st.line_chart(chart_data)

# map
map_data = pd.DataFrame(
    np.random.randn(10,2) / [50,50]+[36.643865773370244, 127.48587203843135], # 위도,경도
    columns=['lat','lon']
)
st.map(map_data)

