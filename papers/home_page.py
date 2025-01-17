import streamlit as st


with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

c1, c2, c3 = st.columns([0.15, 0.7, 0.15])

with c2:
    c21, c22, c23 = st.columns([1, 0.05, 1])
    with c21:
        # st.title(":gray[BUDGET]", anchor=False)
        # st.write("\n")
        # st.write('\n')
        st.video(r"images/Budget Demo.mp4", autoplay=True, muted=True, loop=True)

    with c23:
        st.write('''
                    <p style=color:#BFBEBA>
                        <strong style=color:#f3626f> BUDGET </strong>, This predictive model is designed for a Kaggle competition involving <strong style=color:#f3626f>Regression</strong> on an <span style=color:#f3626f>insurance dataset</span>. 
                        The process starts by preprocessing the data, addressing missing values with KNN imputation, and cleaning the dataset. 
                        Feature engineering then expands the dataset, followed by statistical analysis to reduce the number of features. 
                        Finally, the features are encoded and scaled in preparation for machine learning.
                    </p>
                    <p style=color:#BFBEBA>
                        This model achieved an <strong style=color:#f3626f>RMSLE</strong> of <strong style=color:#f3626f>1.04</strong> in a Kaggle competition. 
                        This score is remarkably close – only 0.03 away – from the top-performing model, placing me in <strong style=color:#f3626f>top 21% position</strong>.
                    </p>
                    <p style=color:#BFBEBA> 
                        The <strong style=color:#f3626f> BUDGET </strong> app helps you understand how life insurance premiums are calculated. 
                        You can explore this in <span style=color:#f3626f>two ways:</span> by entering your <span style=color:#f3626f> own details </span> on the "My Input" page or by using <span style=color:#f3626f> randomly generated </span> scenarios 
                        on the "Random Input" page. 
                    </p>
                    <p style=color:#BFBEBA>
                        The app has <span style=color:#f3626f>three more pages</span> that you can navigate to, each with a specific purpose. 
                        The "See Tableau Charts" page shows <span style=color:#f3626f> interactive charts </span>, 
                        "See Pipeline Design" page visualizes the <span style=color:#f3626f> whole project's pipeline </span> steps,
                        and "See Insights" page tells the ML model's performance and <span style=color:#f3626f>feature importance </span>.
                    </p>
                '''
                , unsafe_allow_html=True)
    
    st.write('\n')
    st.divider()
    st.write('\n')

    with st.container(key="home-selects"):
        b1 = st.pills(label="None", options=['See Tableau Charts', 'See Pipeline Design', "See Insights"], selection_mode='single', label_visibility='collapsed')

        if b1 == 'See Tableau Charts':
            st.switch_page("papers/dash_page.py")
        if b1 == 'See Pipeline Design':
            st.switch_page("papers/pipe_page.py")
        if b1 == 'See Insights':
            st.switch_page("papers/about_model_page.py")
            


    st.divider()

    st.title(":gray[Predict with]", anchor=False)

    with st.container(key="contai"):
        b2 = st.pills(label="None", options=['My Input', 'Random Input'], selection_mode='single', label_visibility='collapsed')

        if b2 == 'My Input':
            st.switch_page("papers/data_page.py")
        if b2 == 'Random Input':
            st.switch_page("papers/random_page.py")
            
    st.write('\n')
    st.divider()
    with st.container(key="footerlinkedin"):
        st.markdown("""
            <a href="https://www.linkedin.com/in/dileepnaidu/" target="_blank">
                <img src="https://img.icons8.com/?size=500&id=8808&format=png&color=5B5B5B" alt="LinkedIn Profile" width="50" height="50">
            </a>
            """, unsafe_allow_html=True)