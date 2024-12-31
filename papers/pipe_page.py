import streamlit as st


with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

c1, c2, c3 = st.columns([2, 3, 2])

with c2:
    st.title("Pipeline Page", anchor=False)