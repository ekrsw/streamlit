import streamlit as st

st.title('Hello, Streamlit!')
st.write('This is a simple Streamlit app.')
col1, col2 = st.columns(2)
with col1:
    st.text_input("タイトル:", "")
with col2:
    st.selectbox("情報カテゴリ:", ("カテゴリ1", "カテゴリ2", "カテゴリ3"))
col3, col4 = st.columns(2)
with col3:
    st.text_input("キーワード:", "")
with col4:
    st.radio("重要:", ("一般","重要"), horizontal=True)
st.text_area("質問:", "")
st.text_area("回答:", "")
st.text_area("追加コメント:")
st.text_area("備考:", "")