import streamlit as st
import random
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import plotly.express as px



with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

c1, c2, c3 = st.columns([0.15, 0.7, 0.15])

with c2:
    st.title(":gray[Metrics to check] Model's Performance", anchor=False)
    st.write('\n')
    c21, c22, c23, c24 = st.columns([1,1,1,1])
    with c21:
        st.metric(":red[RMSE] :gray[: Test]", 1393.72, delta="Train 1396.74", delta_color="off")
    with c22:
        st.metric(":red[RMSLE] :gray[: Test]", 4.696, delta="Train 4.692", delta_color="off")
    with c23:
        st.metric(":red[MAPE] :gray[: Test]", 0.978, delta="Train 0.978", delta_color="off")
    with c24:
        st.metric(":gray[Adjusted R² : Test]", -1.617, delta="Train -1.602", delta_color="off")

    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------

    st.write('\n')
    st.write('\n')
    st.divider()
    st.write('\n')
    st.write('\n')

    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------

    st.title("Top Feature :gray[wich are important for prediction]", anchor=False)

    top = pd.read_csv("featuer_importance.csv")

    top["Percentage of Importance"] = (top["Importance"]/top["Importance"].sum())*100

    top10 = top.head(10)

    fig = px.bar(
        top10,
        y="Percentage of Importance",
        x="Cleaned Features",
        orientation="v",
        labels={"Percentage of Importance": "Percentage of Importance", "Cleaned Features": "Features"},
        text="Percentage of Importance"
    )

    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",  
        paper_bgcolor="rgba(0,0,0,0)",  
        xaxis=dict(
        showticklabels=False,  
        showgrid=False,        
        zeroline=False         
        ),
        yaxis=dict(
            showticklabels=False,  
            showgrid=False,        
            zeroline=False         
        )
    )

    fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside', marker_color=["#f3626f"]*3+["gray"]*7)

    st.plotly_chart(fig)

    with st.expander(" - See All Features Importance", icon="🚨"):
        st.write(top)

    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------

    st.write('\n')
    st.write('\n')
    st.divider()
    st.write('\n')
    st.write('\n')

    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------

    b1 = st.button(label="Back to Home", type="primary")
    if b1:
        st.switch_page("papers/home_page.py")