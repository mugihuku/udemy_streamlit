import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

#st.table(df.style.highlight_max(axis=0))
# table: 静的（スタティック）なテーブルを使いたいとき、ただ、表を表示させたいときに使う
# dataframe: 動的なデータフレームを使いたいとき、ソートなど行いたいときに使う

# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """
