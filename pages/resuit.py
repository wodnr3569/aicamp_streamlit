import streamlit as st
text_1 = f"{st.session_state.num} {st.session_state.name}님"
st.markdown(text_1)

sum = st.session_state.answer1 + st.session_state.answer2
text_2 = f"당신의 점수는 {sum}점 입니다."
st.markdown(text_2)