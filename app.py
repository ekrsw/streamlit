import streamlit as st
import settings
import webbrowser

url = "http://sv-vw-ejap:5555/SupportCenter/main.aspx?etc=127&extraqs=%3fetc%3d127%26id%3d%257bEC01B58B-33BB-EA11-8826-00505695A183%257d&histKey=243406700&newWindow=true&pagetype=entityrecord"

with st.sidebar:
    st.sidebar.title('ナレッジメンテナンス')
    st.sidebar.write('Category')
    st.selectbox("カテゴリ選択", ("カテゴリ1", "カテゴリ2", "カテゴリ3")) 
    with st.form(key="sidebar_form"):
        st.write("sidebar")
        st.text_input("サイドバーのテキスト入力", "")
        st.selectbox("サイドバーの選択ボックス", ("選択肢1", "選択肢2", "選択肢3"))
        st.form_submit_button("サイドバーのボタン")

st.subheader('KBA-00000-00000')
st.link_button("記事を表示", url=url)

col1, col2 = st.columns([3, 1])
with col1:
    st.text_input("タイトル:", "")
with col2:
    st.selectbox("情報カテゴリ:", settings.CATEGORY_LIST)
col3, col4 = st.columns([3, 1])
with col3:
    st.text_input("キーワード:", "")
with col4:
    st.radio("重要:", ("一般","重要"), horizontal=True)
st.text_area("質問:", "")
st.text_area("回答:", "", height=300)
st.text_area("追加コメント:")
st.text_area("備考:", "")

b1, b2, empty1, empty2 = st.columns([1, 1, 4, 4])
with b1:
    st.button("保存")
with b2:
    st.button("提出")