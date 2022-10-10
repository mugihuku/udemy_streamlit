import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('Interactive Widgets')

text = st.text_input('あなたの趣味を教えてください。')
'あなたの趣味: ', text,

condition = st.slider('あなたの今の調子は?', 0, 100, 50)
'コンディション: ', condition

# option = st.selectbox(
#     'あなたが好きな数字を教えてください。',
#     list(range(1, 11))
#)

#'あなたの好きな数字は、', option, 'です。'

# if st.checkbox('Show Image'):
#     img = Image.open('IMGP8156.JPG')
#     st.image(img, caption='猫背', use_column_width=True)
# .checkboxにチェックを入れるとTrue、外れているとFalseという仕掛け
