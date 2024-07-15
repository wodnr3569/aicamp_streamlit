import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

if st.button('이름 불러오기') :
    st.write(st.session_state.name)

if st.button('학번 불러오기') :
    st.write(st.session_state.num)


container = st.container(border=True)
container.write("문제 1번 ")

lose = st.radio(
    "안재민은 오주현한테",
    [":rainbow[진다]", "***빈사상태가 된다***", "비긴다", "빈사상태를 만든다", "이긴다"])

if lose == ":rainbow[진다]":
    st.session_state.answer1 = 50
else:
    st.session_state.answer1 = 0

color = st.text_input('안재민의 색깔은?')

if color == "빨강 && 빨간색":
    st.session_state.answer2 = 50
else:
    st.session_state.answer2 = 0
    