import streamlit as st


with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

c1, c2, c3 = st.columns([2, 3, 2])

with c2:
    st.write('''<div style="position: relative; width: 100%; height: 0; padding-top: 56.2500%;
        padding-bottom: 0; box-shadow: 0 2px 8px 0 rgba(63,69,81,0.16); margin-top: 1.6em; margin-bottom: 0.9em; overflow: hidden;
        border-radius: 8px; will-change: transform;">
            <iframe loading="lazy" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border: none; padding: 0;margin: 0;"
                src="https://www.canva.com/design/DAGa2SOubrs/922Q6rE61VA1SFQ0FoiBHw/view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
            </iframe>
        </div>
        <a href="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAGa2SOubrs&#x2F;922Q6rE61VA1SFQ0FoiBHw&#x2F;view?utm_content=DAGa2SOubrs&amp;utm_campaign=designshare&amp;utm_medium=embeds&amp;utm_source=link" target="_blank" rel="noopener">Tableau Dashboards Design</a> by Dileep Naidu''',
        unsafe_allow_html=True)
    
    st.write("This is just the designs of dashboards, Like how the actual dashboards would look like.")
    st.write("#### The actual dashboards will be replace here as I finish making them")