import streamlit as st
from  streamlit_js_eval import streamlit_js_eval
screen_width = streamlit_js_eval(js_expressions='screen.width', key = 'SCR')
c1 = 0.15*screen_width
c2 = 0.7*screen_width
c3 = 0.15*screen_width
st.write(screen_width)


with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

c1, c2, c3 = st.columns([c1, c2, c3])

with c2:
    # st.title(":gray[Use of] BUDGET :gray[app:]", anchor=False)
    st.write('''
                <p style=color:#BFBEBA>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    This predictive model is designed for a Kaggle competition involving <strong style=color:#f3626f>regression</strong> on an <strong style=color:#f3626f>insurance dataset</strong>. 
                    The process starts by preprocessing the data, addressing missing values with KNN imputation, and cleaning the dataset. 
                    Feature engineering then expands the dataset, followed by statistical analysis to reduce the number of features. 
                    Finally, the features are encoded and scaled in preparation for machine learning.
                </p>
                <p style=color:#BFBEBA>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    This model achieved an <strong style=color:#f3626f>RMSLE</strong> of <strong style=color:#f3626f>1.04</strong> in a Kaggle competition. 
                    This score is remarkably close – only 0.03 away – from the top-performing model, placing me in <strong style=color:#f3626f>top 21% position</strong>.
                </p>
                <p style=color:#BFBEBA> 
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    The <strong style=color:#f3626f> BUDGET </strong> app helps you understand how life insurance premiums are calculated. 
                    You can explore this in <strong style=color:#f3626f>two ways:</strong> by entering your <strong style=color:#f3626f> own details </strong> on the "My Input" page or by using <strong style=color:#f3626f> randomly generated </strong> scenarios 
                    on the "Random Input" page. 
                </p>
                <p style=color:#BFBEBA>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    The app has <strong style=color:#f3626f>two more pages</strong> that you can navigate to, each with a specific purpose. 
                    The "See Tableau Charts" page shows <strong style=color:#f3626f> interactive charts </strong>, 
                    and "See Pipeline Design" page visualizes the <strong style=color:#f3626f> whole project's pipeline </strong> steps.
                </p>
             '''
             , unsafe_allow_html=True)
    
    st.write('\n')
    st.write('\n')
    st.write('\n')
    b1 = st.pills(label="None", options=['See Tableau Charts', 'See Pipeline Design',], selection_mode='single', label_visibility='collapsed')

    if b1 == 'See Tableau Charts':
        st.switch_page("papers/dash_page.py")
    if b1 == 'See Pipeline Design':
        st.switch_page("papers/pipe_page.py")


    st.divider()

    st.title(":gray[Predict with:]", anchor=False)

    b2 = st.pills(label="None", options=['My Input', 'Random Input'], selection_mode='single', label_visibility='collapsed')

    if b2 == 'My Input':
        st.switch_page("papers/data_page.py")
    if b2 == 'Random Input':
        st.switch_page("papers/random_page.py")

    st.divider()

    st.markdown("""
        <a href="https://www.linkedin.com/in/dileepnaidu/" target="_blank">
            <img src="https://img.icons8.com/?size=500&id=8808&format=png&color=5B5B5B" alt="LinkedIn Profile" width="50" height="50">
        </a>
        """, unsafe_allow_html=True)