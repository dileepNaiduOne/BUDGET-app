import streamlit as st


with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

c1, c2, c3 = st.columns([2, 3, 2])

inputs = []

with c2:
    st.title(":gray[Prediction Form]", anchor=False)
    st.caption(":red[*] Providing correct information will ensure precise predictions")

    st.divider()

    with st.form("prediction_form", enter_to_submit=False, border=False):
        # Age
        age = st.number_input(":red[Age]", min_value=0, max_value=100, placeholder="Enter values between 0 and 100", value=None)
        inputs.append(age)
        
        # Gender
        gender = st.segmented_control(":red[Gender]", options=["Male - :material/male:", "Female - :material/female:"], selection_mode="single")
        inputs.append(gender)

        # Education Level
        edu = st.segmented_control(label=":red[Education Level]", options=["Bachelor's", "Master's", "High School", "PhD"], selection_mode="single",)
        inputs.append(edu)

        # Occupation
        occupation = st.segmented_control(label=":red[Occupation]", options=['Self-Employed', 'Employed', 'Unemployed'], selection_mode="single")
        inputs.append(occupation)

        # Marital Status
        marry = st.segmented_control(":red[Marital Status]", options=['Single - :material/man_4:', 'Married - :material/wc:', 'Divorced - :material/taunt:'], selection_mode="single")
        inputs.append(marry)

        # Location
        location = st.segmented_control(":red[Location]", options=['Rural', 'Suburban', 'Urban'], selection_mode="single")
        inputs.append(location)

        # Property Type
        property_type = st.segmented_control(":red[Property Type]", options=['House', 'Apartment', 'Condo'], selection_mode="single")
        inputs.append(property_type)

        # -----------------------------------------------------------------------------------------------------------------------------------------------
        st.divider()
        # -----------------------------------------------------------------------------------------------------------------------------------------------

        # Smoking Status
        smoking_status = st.radio(label=":red[Smoking Status]", options=["Yes", "No"], horizontal=True, index=None)
        inputs.append(smoking_status)

        # Exercise Frequency
        exercise_frequency = st.segmented_control(":red[Exercise Frequency]", options=['Daily', 'Weekly', 'Monthly', 'Rarely'], selection_mode="single")
        inputs.append(exercise_frequency)

        # -----------------------------------------------------------------------------------------------------------------------------------------------
        st.divider()
        # -----------------------------------------------------------------------------------------------------------------------------------------------

        # Annual Income
        income = st.number_input(":red[Annual Income (₹)]", format="%.2f", placeholder="Enter values greater than 0", value=None, min_value=0.00)
        inputs.append(income)

        # Number of Dependents
        dependents = st.radio(":red[No. of Dependents]", options=[0, 1, 2, 3, 4], horizontal=True, index=None)
        inputs.append(dependents)

        # Health Score
        health = st.number_input(":red[Health Score]", placeholder="Enter values between 0 and 1000", value=None, min_value=0)
        inputs.append(health)

        # Credit Score
        credit = st.number_input(":red[Credit Score]", placeholder="Enter values between 0 and 1000", value=None, min_value=0)
        inputs.append(credit)

        # -----------------------------------------------------------------------------------------------------------------------------------------------
        st.divider()
        # -----------------------------------------------------------------------------------------------------------------------------------------------


        # Policy Start Date
        policy_start_date = st.date_input(":red[Policy Start Date]", format="DD/MM/YYYY")
        inputs.append(policy_start_date)

        # Policy Type
        policy = st.segmented_control(":red[Policy Type]", options=['Basic', 'Comprehensive', 'Premium'], selection_mode="single")
        inputs.append(policy)

        # Insurance Duration
        insurance_duration = st.number_input(":red[Insurance Duration]", min_value=0, max_value=10, placeholder="Enter values between 0 and 10", value=None)
        inputs.append(insurance_duration)

        # Previous Claims
        previous_claims = st.number_input(":red[Previous Claims]", min_value=0, max_value=10, placeholder="Enter values between 0 and 10", value=None)
        inputs.append(previous_claims)

        # Vehicle Age
        vehicle_age = st.number_input(":red[Vehicle Age]", min_value=0, max_value=30, placeholder="Enter values between 0 and 30", value=None)
        inputs.append(vehicle_age)

        
        # -----------------------------------------------------------------------------------------------------------------------------------------------
        st.divider()
        # -----------------------------------------------------------------------------------------------------------------------------------------------
        

        # Customer Feedback
        customer_feedback = st.segmented_control(":red[Customer Feedback]", options=['Poor', 'Average', 'Good'], selection_mode="single")
        inputs.append(customer_feedback)


        st.divider()


        @st.dialog("PREDICTION", width="large")
        def prediction(inputs):
            st.write(inputs)
            # Sample output - [21,"Male - :material/male:","Master's","Unemployed","Single - :material/man_4:","Urban","House","No","Weekly",5124,3,784,7844.99,"datetime.date(2022, 8, 17)","Basic",8,2,8,"Good"]

        st.write("\n")
        st.write("\n")
        pre = st.form_submit_button(f"# PREDICT", type="primary", icon=":material/currency_rupee:", use_container_width=True)

        if pre:

            prediction(inputs)