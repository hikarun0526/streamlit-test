import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('streamlit 超入門')

st.write('Display image')

st.write('プログレスバーの表示')

bar = st.progress(0)
latest_iteration = st.empty()
for i in range(100):
    latest_iteration.text(f'Interation {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
#if st.checkbox('Show Image'):
#    img = Image.open('IMG_1053.JPG')
#    st.image(img, caption='hikarun suteki', use_column_width=True)
'''
left_column, right_coulumn = st.beta_columns(2)
button = left_column.button('右カラム二文字を表示')
if button:
    right_coulumn.write('ここは右カラム')
'''

expander1 = st.beta_expander('元気がないときは？')
expander1.write('寝る')

#text = st..text_input('あなたの趣味を教えてください')
#condition = st..slider('あなたの調子は？', 0, 100, 50)

#'あなたが趣味は、', text, 'です。'
#'コンディション', condition
