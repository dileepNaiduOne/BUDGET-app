import streamlit as st


with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)


st.title(":red[Glimpse of Pipeline ]", anchor=False)
with st.container(key="pipehome"):
    b1 = st.button(label="Back to Home", type="primary")
    if b1:
        st.switch_page("papers/home_page.py")

st.components.v1.html('''
    <div 
        style="
            position: relative; 
            width: 100%; 
            height: 0; 
            padding-top: 141.4141%;
            padding-bottom: 0; 
            box-shadow: 0 2px 8px 0 rgba(63,69,81,0.16); 
            margin-top: 1.6em; 
            margin-bottom: 0.9em; 
            overflow: hidden;
            border-radius: 8px; 
            will-change: transform;">
        <iframe loading="lazy" style="
            position: absolute; 
            width: 100%; 
            height: 100%; 
            top: 0; 
            left: 0; 
            border: none; 
            padding: 0;
            margin: 0;
            " src="https://www.canva.com/design/DAGbezU1w9c/TbVwTObt2wkBqDDEGQMXQQ/view?embed">
        </iframe>
    </div>
''',height=2400)

