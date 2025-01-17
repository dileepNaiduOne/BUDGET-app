import streamlit as st
import warnings
warnings.filterwarnings("ignore")
import datetime


with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

c1, c2, c3 = st.columns([0.15, 0.7, 0.15])

inputs = []

with c2:
    st.title(":gray[Prediction with Your Inputs]", anchor=False)
    st.caption(":red[*] Providing correct information will ensure precise predictions. :red[Please don't leave any field blank.]")

    st.divider()

    with st.form("prediction_form", enter_to_submit=False, border=False):
        # Age
        age = st.number_input(":red[Age]", min_value=18, max_value=70, placeholder="Enter age between 18 and 70", value=None)
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
        income = st.number_input(":red[Annual Income (₹)]", placeholder="Enter income between 0 and 1,50,000", value=None, min_value=0, max_value=150000)
        inputs.append(income)

        # Number of Dependents
        dependents = st.radio(":red[No. of Dependents]", options=[0, 1, 2, 3, 4], horizontal=True, index=None)
        inputs.append(dependents)

        # Health Score
        health = st.number_input(":red[Health Score]", placeholder="Enter score between 0.00 and 60.00", value=None, min_value=0, max_value=60)
        inputs.append(health)

        # Credit Score
        credit = st.number_input(":red[Credit Score]", placeholder="Enter Score between 300 and 850", value=None, min_value=300, max_value=850)
        inputs.append(credit)

        # -----------------------------------------------------------------------------------------------------------------------------------------------
        st.divider()
        # -----------------------------------------------------------------------------------------------------------------------------------------------


        # Policy Start Date
        policy_start_date = st.date_input(":red[Policy Start Date]", format="DD/MM/YYYY", min_value=datetime.date(2020, 1, 1), max_value=datetime.date(2023, 12, 31))
        inputs.append(policy_start_date)

        # Policy Type
        policy = st.segmented_control(":red[Policy Type]", options=['Basic', 'Comprehensive', 'Premium'], selection_mode="single")
        inputs.append(policy)

        # Insurance Duration
        insurance_duration = st.number_input(":red[Insurance Duration]", min_value=1, max_value=9, placeholder="Enter values between 1 and 9", value=None)
        inputs.append(insurance_duration)

        # Previous Claims
        previous_claims = st.number_input(":red[Previous Claims]", min_value=0, max_value=9, placeholder="Enter values between 0 and 9", value=None)
        inputs.append(previous_claims)

        # Vehicle Age
        vehicle_age = st.number_input(":red[Vehicle Age]", min_value=0, max_value=20, placeholder="Enter values between 0 and 20", value=None)
        inputs.append(vehicle_age)

        
        # -----------------------------------------------------------------------------------------------------------------------------------------------
        st.divider()
        # -----------------------------------------------------------------------------------------------------------------------------------------------
        

        # Customer Feedback
        customer_feedback = st.segmented_control(":red[Customer Feedback]", options=['Poor', 'Average', 'Good'], selection_mode="single")
        inputs.append(customer_feedback)


        st.divider()

        st.write("\n")
        st.write("\n")
        pre = st.form_submit_button(f"# PREDICT", type="primary", icon=":material/currency_rupee:", use_container_width=True)

    b1 = st.button(label="Back to Home", type="primary")
    if b1:
        st.switch_page("papers/home_page.py")
    from make_prediction import make_prediction

    @st.dialog("PREDICTION", width="large")
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

    @st.dialog("ERROR", width="large")
    def tell_error(user_inputs):
        st.title(":red[Found some BLANK fields!]", anchor=False)
        blanks = ", ".join([i[0] for i in user_inputs.items() if i[1]==None])
        st.write(f":gray[Please, Make sure you are filling] :red[{blanks}].", anchor=False)


# ====================================================================================================================
# ====================================================================================================================
# ====================================================================================================================


        

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

        if None in inputs:
            tell_error(send_to_predict)
        else:
            prediction(send_to_predict)
            
