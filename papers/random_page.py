import streamlit as st
import random
from datetime import datetime


with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

c1, c2, c3 = st.columns([0.15, 0.7, 0.15])

inputs = []

with c2:
    st.title(":gray[Prediction with Random Inputs]", anchor=False)
    # st.write(":gray[Click below button for prediction]")

    # st.divider()
    pred = st.empty()

    with st.form("prediction_form", enter_to_submit=False, border=False):
        # Age
        age = random.randint(18, 70)
        inputs.append(age)
        
        # Gender
        gender = random.choice(["Male", "Female"])
        inputs.append(gender)

        # Education Level
        edu = random.choice(["Bachelor's", "Master's", "High School", "PhD"])
        inputs.append(edu)

        # Occupation
        occupation = random.choice(['Self-Employed', 'Employed', 'Unemployed'])
        inputs.append(occupation)

        # Marital Status
        marry = random.choice(['Single', 'Married', 'Divorced'])
        inputs.append(marry)

        # Location
        location = random.choice(['Rural', 'Suburban', 'Urban'])
        inputs.append(location)

        # Property Type
        property_type = random.choice(['House', 'Apartment', 'Condo'])
        inputs.append(property_type)

        # -----------------------------------------------------------------------------------------------------------------------------------------------
        # st.divider()
        # -----------------------------------------------------------------------------------------------------------------------------------------------

        # Smoking Status
        smoking_status = random.choice(["Yes", "No"])
        inputs.append(smoking_status)

        # Exercise Frequency
        exercise_frequency = random.choice(['Daily', 'Weekly', 'Monthly', 'Rarely'])
        inputs.append(exercise_frequency)

        # -----------------------------------------------------------------------------------------------------------------------------------------------
        # st.divider()
        # -----------------------------------------------------------------------------------------------------------------------------------------------

        # Annual Income
        income = random.randint(1, 150000)
        inputs.append(income)

        # Number of Dependents
        dependents = random.choice([0, 1, 2, 3, 4])
        inputs.append(dependents)

        # Health Score
        health = random.randint(1, 58) + random.random()
        inputs.append(health)

        # Credit Score
        credit = random.randint(300, 850)
        inputs.append(credit)

        # -----------------------------------------------------------------------------------------------------------------------------------------------
        # st.divider()
        # -----------------------------------------------------------------------------------------------------------------------------------------------


        # Policy Start Date
        y = random.randint(2020, 2023)
        m = random.randint(1, 12)
        d = random.randint(1, 28)
        policy_start_date = datetime(y, m, d)
        inputs.append(policy_start_date)

        # Policy Type
        policy = random.choice(['Basic', 'Comprehensive', 'Premium'])
        inputs.append(policy)

        # Insurance Duration
        insurance_duration = random.randint(1, 9)
        inputs.append(insurance_duration)

        # Previous Claims
        previous_claims = random.randint(0, 9)
        inputs.append(previous_claims)

        # Vehicle Age
        vehicle_age = random.randint(1, 20)
        inputs.append(vehicle_age)

        
        # -----------------------------------------------------------------------------------------------------------------------------------------------
        # st.divider()
        # -----------------------------------------------------------------------------------------------------------------------------------------------
        

        # Customer Feedback
        customer_feedback = random.choice(['Poor', 'Average', 'Good'])
        inputs.append(customer_feedback)


        # st.divider()

        from make_prediction import make_prediction
        def prediction(user_inputs):
            with st.spinner('Getting your prediction. PLEASE WAIT...'):
                
                p, df = make_prediction(user_inputs)
                st.divider()
                pred = st.title(f":gray[The] Premium Amount :gray[for the below given data is]  :red[₹{p[0]:.2f}]", anchor=False)
                st.divider()
                d1, d2 = st.columns([1, 1], gap="large")
                with d1:
                    st.write(f":red[Data, you generated randomly]", anchor=False)
                    st.write(f":gray[> > >] {len(user_inputs)} :red[fields]", anchor=False)
                    st.dataframe(user_inputs, use_container_width=True)
                with d2:
                    st.write(f":red[Data, sent to ML Model after transformation]", anchor=False)
                    st.write(f":gray[> > >] {len(df)} :red[fields]", anchor=False)
                    st.dataframe(df, use_container_width=True)
            

# ====================================================================================================================
# ====================================================================================================================
# ====================================================================================================================


        st.write("\n")
        st.write("\n")
        pre = st.form_submit_button(f"# PREDICT", type="primary", icon=":material/currency_rupee:", use_container_width=True)
        st.caption(":red[Click above] :gray[button for prediction]")

    st.write("\n")

    b1 = st.button(label="Back to Home", type="primary")
    if b1:
        st.switch_page("papers/home_page.py")

    if pre:

        send_to_predict = {
        "Age"                            : inputs[0],
        "Gender"                         : inputs[1],
        "Annual Income"                  : inputs[9],
        "Marital Status"                 : inputs[4],
        "Number of Dependents"           : inputs[10],
        "Education Level"                : inputs[2],
        "Occupation"                     : inputs[3],
        "Health Score"                   : inputs[11],
        "Location"                       : inputs[5],
        "Policy Type"                    : inputs[14],
        "Previous Claims"                : inputs[16],
        "Vehicle Age"                    : inputs[17],
        "Credit Score"                   : inputs[12],
        "Insurance Duration"             : inputs[15],
        "Policy Start Date"              : inputs[13],
        "Customer Feedback"              : inputs[18],
        "Smoking Status"                 : inputs[7],
        "Exercise Frequency"             : inputs[8],
        "Property Type"                  : inputs[6]
    }

        prediction(send_to_predict)