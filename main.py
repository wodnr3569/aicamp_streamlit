import streamlit as st

st.title('과목 소개')
st.header('안재민',divider='rainbow')

st.text('부곡 노짱이다')


text = st.text_input('이름을 입력하세요.')
if st.button('이름 저장', key='save_name') :
    if 'name' not in st.session_state:
        st.session_state.name = text
    else :
        st.session_state.name = text
text = st.text_input('햑번을 입력하세요.')
if st.button('학번 저장', key='save_num') :
    if 'num' not in st.session_state:
        st.session_state.num = text
    else :
        st.session_state.num = text
        