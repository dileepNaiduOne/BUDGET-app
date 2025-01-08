import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import *
import xgboost as xgb
import math

from sklearn.preprocessing import PowerTransformer
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer
from sklearn.preprocessing import RobustScaler, MinMaxScaler, StandardScaler

from sklearn.model_selection import train_test_split
import datetime


import warnings
warnings.filterwarnings("ignore")
pd.set_option("display.max_columns", None)

def make_prediction(output):
    output["IsNull_Age"] = 0
    output["IsNull_Annual Income"] = 0
    output["IsNull_Marital Status"] = 0
    output["IsNull_Number of Dependents"] = 0
    output["IsNull_Occupation"] = 0
    output["IsNull_Health Score"] = 0
    output["IsNull_Previous Claims"] = 0
    output["IsNull_Vehicle Age"] = 0
    output["IsNull_Credit Score"] = 0
    output["IsNull_Insurance Duration"] = 0
    output["IsNull_Customer Feedback"] = 0

    output["Gender"] = output["Gender"].split(" - ")[0]
    output["Marital Status"] = output["Marital Status"].split(" - ")[0]

    df = pd.DataFrame(output, index=[0])

    smoke = df["Smoking Status"].replace({"Yes" : 0, "No" : 1})

    ex = df["Exercise Frequency"].replace({"Rarely" : 0, "Monthly" : 1, "Weekly" : 2, "Daily" : 3})


    bins = [0, 30, 53, float('inf')]
    labels = [0, 1, 2]
    age = pd.cut(df['Age'], bins=bins, labels=labels, right=False)


    bins = [0, 16.285503904803008, 33.959695457149195, float('inf')]
    labels = [0, 1, 2]
    health = pd.cut(df['Health Score'], bins=bins, labels=labels, right=False)

    # ==============================================================================

    df["Health Conscious Level"] = smoke + ex + age.astype('int') + health.astype('int')

    # ==============================================================================

    smoke = df["Smoking Status"].replace({"Yes" : 2, "No" : 4})


    ex = df["Exercise Frequency"].replace({"Rarely" : 2, "Monthly" : 4, "Weekly" : 8, "Daily" : 16})


    age = df['Age']


    health = df['Health Score']

    # ==============================================================================

    df["Health Conscious Level1"] = smoke * ex * age * health

    # ==============================================================================

    df["Money Per Head"] = df["Annual Income"] / df["Number of Dependents"].where(df["Number of Dependents"] != 0, 1)

    # ==============================================================================

    df["Money Handling Level"] = df["Annual Income"] * df["Credit Score"]

    # ==============================================================================

    df["Money Handling Level1"] = df["Annual Income"] / df["Credit Score"]

    # ==============================================================================

    df["Growth"] = df["Education Level"].replace({"High School" : 1, "Bachelor's" : 2, "Master's" : 3, "PhD" : 4}) * df["Annual Income"]

    # ==============================================================================

    df["Growth1"] = df["Annual Income"] / df["Education Level"].replace({"High School" : 1, "Bachelor's" : 2, "Master's" : 3, "PhD" : 4})

    # ==============================================================================

    df["Determinstic"] = df["Annual Income"] * (1 / df["Age"])

    # ==============================================================================

    df["Day_Name"] = df["Policy Start Date"][0].strftime("%A")

    # ==============================================================================

    df["Credit by Score"] = df["Credit Score"]/df["Previous Claims"].where(df["Previous Claims"] != 0, 1)

    # ==============================================================================

    df['CreditInsurance'] = df['Credit Score'] * df['Insurance Duration']

    # ==============================================================================

    df['Health_Risk_Score'] = df['Smoking Status'].apply(lambda x: 1 if x == 'Smoker' else 0) + df['Exercise Frequency'].apply(lambda x: 1 if x == 'Low' else (0.5 if x == 'Medium' else 0)) + (100 - df['Health Score']) / 20

    # ==============================================================================

    df['Credit_Health_Score'] = df['Credit Score'] * df['Health Score']

    # ==============================================================================

    df['Health_Age_Interaction'] = df['Health Score'] * df['Age']

    # ==============================================================================

    df["Feedback1"] = df["Annual Income"] * df["Customer Feedback"].replace({"Poor" : 2, "Average" : 4, "Good" : 8})

    # ==============================================================================

    df["Feedback2"] = df["Credit Score"] * df["Customer Feedback"].replace({"Poor" : 2, "Average" : 4, "Good" : 8})

    # ==============================================================================

    df["Feedback3"] = df["Previous Claims"] * df["Customer Feedback"].replace({"Poor" : 2, "Average" : 4, "Good" : 8})

    # ==============================================================================

    df["Feedback4"] = df["Health Score"] * df["Customer Feedback"].replace({"Poor" : 2, "Average" : 4, "Good" : 8})

    # ==============================================================================

    df['Total Nulls'] = 0

    df["Policy Start Date - Day"] = df["Policy Start Date"][0].day
    df["Policy Start Date - Month"] = df["Policy Start Date"][0].month
    df["Policy Start Date - Year"] = df["Policy Start Date"][0].year

    df["Policy Start Date - Quarter"] = str(df["Policy Start Date"][0].year) + " Q" + str(math.ceil(df["Policy Start Date"][0].month/3))

    df["Sin_Year"] = np.sin(2 * np.pi * df["Policy Start Date - Year"].astype('int64'))
    df["Cos_Year"] = np.cos(2 * np.pi * df["Policy Start Date - Year"].astype('int64'))

    df["Sin_Month"] = np.sin(2 * np.pi * df["Policy Start Date - Month"].astype('int64'))
    df["Cos_Month"] = np.cos(2 * np.pi * df["Policy Start Date - Month"].astype('int64'))

    df.drop(columns="Policy Start Date", inplace=True)

    df["Health Conscious Level"] = df["Health Conscious Level"].astype("O")

    magics = [
        "Number of Dependents_MIN_Premium Amount", 
        "Number of Dependents_MEAN_Premium Amount",
        "Number of Dependents_Q1_Premium Amount",               
        "Number of Dependents_MEDIAN_Premium Amount",           
        "Number of Dependents_Q3_Premium Amount",               
        "Number of Dependents_STD_Premium Amount",              
        "Number of Dependents_MAX_Premium Amount",              
        "Occupation_MIN_Premium Amount",                        
        "Occupation_MEAN_Premium Amount",                       
        "Occupation_Q1_Premium Amount",                         
        "Occupation_MEDIAN_Premium Amount",                     
        "Occupation_Q3_Premium Amount",                         
        "Occupation_STD_Premium Amount",                        
        "Occupation_MAX_Premium Amount",                        
        "Education Level_MIN_Premium Amount",                   
        "Education Level_MEAN_Premium Amount",                  
        "Education Level_Q1_Premium Amount",                    
        "Education Level_MEDIAN_Premium Amount",                
        "Education Level_Q3_Premium Amount",                    
        "Education Level_STD_Premium Amount",                   
        "Education Level_MAX_Premium Amount",                   
        "Previous Claims_MIN_Premium Amount",                   
        "Previous Claims_MEAN_Premium Amount",                  
        "Previous Claims_Q1_Premium Amount",                    
        "Previous Claims_MEDIAN_Premium Amount",                
        "Previous Claims_Q3_Premium Amount",                    
        "Previous Claims_STD_Premium Amount",                   
        "Previous Claims_MAX_Premium Amount",                   
        "Health Conscious Level_MIN_Premium Amount",            
        "Health Conscious Level_MEAN_Premium Amount",           
        "Health Conscious Level_Q1_Premium Amount",             
        "Health Conscious Level_MEDIAN_Premium Amount",         
        "Health Conscious Level_Q3_Premium Amount",             
        "Health Conscious Level_STD_Premium Amount",            
        "Health Conscious Level_MAX_Premium Amount",            
        "Insurance Duration_MIN_Premium Amount",                
        "Insurance Duration_MEAN_Premium Amount",               
        "Insurance Duration_Q1_Premium Amount",                 
        "Insurance Duration_MEDIAN_Premium Amount",             
        "Insurance Duration_Q3_Premium Amount",                 
        "Insurance Duration_STD_Premium Amount",                
        "Insurance Duration_MAX_Premium Amount"   
]

    for i in magics:
        column, operation, target = i.split("_")
        dummy = pd.read_csv(f"do_magics/{i}.csv")
        df[i] = dummy[dummy[column] == df[column][0]][target].values[0]

    import gzip
    import pickle

    def unpack_pickle(foldername, filename, columnname):
        with gzip.open(f"{foldername}/{filename}.pkl.gz", 'rb') as f:
            model = pickle.load(f)
            return model.transform(df[[columnname]]).flatten()
        
    df["Policy Start Date - Year"] = df["Policy Start Date - Year"].astype("O")
    ############################################
    df["ENCODED_Policy Start Date - Year"] = unpack_pickle(foldername="do_encodings", filename="ENCODED_Policy Start Date - Year", columnname="Policy Start Date - Year")
    df.drop(columns="Policy Start Date - Year", inplace=True)

    ############################################
    df["ENCODED_Policy Start Date - Quarter"] = unpack_pickle(foldername="do_encodings", filename="ENCODED_Policy Start Date - Quarter", columnname="Policy Start Date - Quarter")
    df.drop(columns="Policy Start Date - Quarter", inplace=True)

    ############################################
    df["ENCODED_Customer Feedback"] = unpack_pickle(foldername="do_encodings", filename="ENCODED_Customer Feedback", columnname="Customer Feedback")
    df.drop(columns="Customer Feedback", inplace=True)

    with gzip.open("do_encodings/ENCODED_Occupation.pkl.gz", 'rb') as f:
        model = pickle.load(f)

    b = pd.DataFrame(
            model.transform(df[["Occupation"]]),
            columns="ENCODED_" + model.get_feature_names_out()
        )

    df = pd.concat([df, b], axis=1)
    df.drop(columns="Occupation", inplace=True)


    with gzip.open("do_encodings/ENCODED_Marital Status.pkl.gz", 'rb') as f:
        model = pickle.load(f)

    b = pd.DataFrame(
            model.transform(df[["Marital Status"]]),
            columns="ENCODED_" + model.get_feature_names_out()
        )

    df = pd.concat([df, b], axis=1)
    df.drop(columns="Marital Status", inplace=True)

    df = df[[
         'Annual Income',
         'Credit Score',
         'IsNull_Annual Income',
         'Money Handling Level',
         'Money Handling Level1',
         'Money Per Head',
         'Growth',
         'Credit by Score',
         'Determinstic',
         'Growth1',
         'Feedback1',
         'Previous Claims_MEDIAN_Premium Amount',
         'IsNull_Health Score',
         'Previous Claims_MEAN_Premium Amount',
         'Previous Claims',
         'Previous Claims_STD_Premium Amount',
         'Previous Claims_Q3_Premium Amount',
         'Previous Claims_Q1_Premium Amount',
         'IsNull_Customer Feedback',
         'Previous Claims_MAX_Premium Amount',
         'Feedback3',
         'IsNull_Previous Claims',
         'IsNull_Marital Status',
         'Health Score',
         'Health_Risk_Score',
         'Feedback2',
         'CreditInsurance',
         'Sin_Year',
         'IsNull_Credit Score',
         'Health_Age_Interaction',
         'Total Nulls',
         'ENCODED_Policy Start Date - Year',
         'ENCODED_Policy Start Date - Quarter',
         'Feedback4',
         'IsNull_Number of Dependents',
         'IsNull_Occupation',
         'Health Conscious Level1',
         'Sin_Month',
         'Policy Start Date - Month',
         'Health Conscious Level',
         'Health Conscious Level_Q1_Premium Amount',
         'Health Conscious Level_MEAN_Premium Amount',
         'Health Conscious Level_MEDIAN_Premium Amount',
         'Number of Dependents_MEAN_Premium Amount',
         'Number of Dependents_MEDIAN_Premium Amount',
         'Number of Dependents_Q1_Premium Amount',
         'Number of Dependents_Q3_Premium Amount',
         'Number of Dependents_STD_Premium Amount',
         'Health Conscious Level_Q3_Premium Amount',
         'Insurance Duration_MEAN_Premium Amount',
         'Insurance Duration_MEDIAN_Premium Amount',
         'Insurance Duration_Q1_Premium Amount',
         'Insurance Duration_Q3_Premium Amount',
         'Health Conscious Level_MAX_Premium Amount',
         'Credit_Health_Score',
         'Occupation_Q3_Premium Amount',
         'Occupation_MEAN_Premium Amount',
         'Occupation_MAX_Premium Amount',
         'Occupation_MEDIAN_Premium Amount',
         'Occupation_Q1_Premium Amount',
         'Previous Claims_MIN_Premium Amount',
         'Insurance Duration_MAX_Premium Amount',
         'ENCODED_Occupation_Self-Employed',
         'Age',
         'Insurance Duration_STD_Premium Amount',
         'Occupation_STD_Premium Amount'
   ]]
    
    for i in df.columns:
        with gzip.open(f"do_scalings/SCALER_{i}.pkl.gz", 'rb') as f:
                model = pickle.load(f)

        df[f"SCALER_{i}"] = model.transform(df[[i]]).flatten()
        df.drop(columns=i, inplace=True)

    new_cols = ['SCALER_Annual_Income', 'SCALER_Credit_Score', 'SCALER_IsNull_Annual_Income', 'SCALER_Money_Handling_Level', 'SCALER_Money_Handling_Level1', 'SCALER_Money_Per_Head', 'SCALER_Growth', 'SCALER_Credit_by_Score', 'SCALER_Determinstic', 'SCALER_Growth1', 'SCALER_Feedback1', 'SCALER_Previous_Claims_MEDIAN_Premium_Amount', 'SCALER_IsNull_Health_Score', 'SCALER_Previous_Claims_MEAN_Premium_Amount', 'SCALER_Previous_Claims', 'SCALER_Previous_Claims_STD_Premium_Amount', 'SCALER_Previous_Claims_Q3_Premium_Amount', 'SCALER_Previous_Claims_Q1_Premium_Amount', 'SCALER_IsNull_Customer_Feedback', 'SCALER_Previous_Claims_MAX_Premium_Amount', 'SCALER_Feedback3', 'SCALER_IsNull_Previous_Claims', 'SCALER_IsNull_Marital_Status', 'SCALER_Health_Score', 'SCALER_Health_Risk_Score', 'SCALER_Feedback2', 'SCALER_CreditInsurance', 'SCALER_Sin_Year', 'SCALER_IsNull_Credit_Score', 'SCALER_Health_Age_Interaction', 'SCALER_Total_Nulls', 'SCALER_ENCODED_Policy_Start_Date_-_Year', 'SCALER_ENCODED_Policy_Start_Date_-_Quarter', 'SCALER_Feedback4', 'SCALER_IsNull_Number_of_Dependents', 'SCALER_IsNull_Occupation', 'SCALER_Health_Conscious_Level1', 'SCALER_Sin_Month', 'SCALER_Policy_Start_Date_-_Month', 'SCALER_Health_Conscious_Level', 'SCALER_Health_Conscious_Level_Q1_Premium_Amount', 'SCALER_Health_Conscious_Level_MEAN_Premium_Amount', 'SCALER_Health_Conscious_Level_MEDIAN_Premium_Amount', 'SCALER_Number_of_Dependents_MEAN_Premium_Amount', 'SCALER_Number_of_Dependents_MEDIAN_Premium_Amount', 'SCALER_Number_of_Dependents_Q1_Premium_Amount', 'SCALER_Number_of_Dependents_Q3_Premium_Amount', 'SCALER_Number_of_Dependents_STD_Premium_Amount', 'SCALER_Health_Conscious_Level_Q3_Premium_Amount', 'SCALER_Insurance_Duration_MEAN_Premium_Amount', 'SCALER_Insurance_Duration_MEDIAN_Premium_Amount', 'SCALER_Insurance_Duration_Q1_Premium_Amount', 'SCALER_Insurance_Duration_Q3_Premium_Amount', 'SCALER_Health_Conscious_Level_MAX_Premium_Amount', 'SCALER_Credit_Health_Score', 'SCALER_Occupation_Q3_Premium_Amount', 'SCALER_Occupation_MEAN_Premium_Amount', 'SCALER_Occupation_MAX_Premium_Amount', 'SCALER_Occupation_MEDIAN_Premium_Amount', 'SCALER_Occupation_Q1_Premium_Amount', 'SCALER_Previous_Claims_MIN_Premium_Amount', 'SCALER_Insurance_Duration_MAX_Premium_Amount', 'SCALER_ENCODED_Occupation_Self-Employed', 'SCALER_Age', 'SCALER_Insurance_Duration_STD_Premium_Amount', 'SCALER_Occupation_STD_Premium_Amount']
    old_cols = ['SCALER_Annual Income', 'SCALER_Credit Score', 'SCALER_IsNull_Annual Income', 'SCALER_Money Handling Level', 'SCALER_Money Handling Level1', 'SCALER_Money Per Head', 'SCALER_Growth', 'SCALER_Credit by Score', 'SCALER_Determinstic', 'SCALER_Growth1', 'SCALER_Feedback1', 'SCALER_Previous Claims_MEDIAN_Premium Amount', 'SCALER_IsNull_Health Score', 'SCALER_Previous Claims_MEAN_Premium Amount', 'SCALER_Previous Claims', 'SCALER_Previous Claims_STD_Premium Amount', 'SCALER_Previous Claims_Q3_Premium Amount', 'SCALER_Previous Claims_Q1_Premium Amount', 'SCALER_IsNull_Customer Feedback', 'SCALER_Previous Claims_MAX_Premium Amount', 'SCALER_Feedback3', 'SCALER_IsNull_Previous Claims', 'SCALER_IsNull_Marital Status', 'SCALER_Health Score', 'SCALER_Health_Risk_Score', 'SCALER_Feedback2', 'SCALER_CreditInsurance', 'SCALER_Sin_Year', 'SCALER_IsNull_Credit Score', 'SCALER_Health_Age_Interaction', 'SCALER_Total Nulls', 'SCALER_ENCODED_Policy Start Date - Year', 'SCALER_ENCODED_Policy Start Date - Quarter', 'SCALER_Feedback4', 'SCALER_IsNull_Number of Dependents', 'SCALER_IsNull_Occupation', 'SCALER_Health Conscious Level1', 'SCALER_Sin_Month', 'SCALER_Policy Start Date - Month', 'SCALER_Health Conscious Level', 'SCALER_Health Conscious Level_Q1_Premium Amount', 'SCALER_Health Conscious Level_MEAN_Premium Amount', 'SCALER_Health Conscious Level_MEDIAN_Premium Amount', 'SCALER_Number of Dependents_MEAN_Premium Amount', 'SCALER_Number of Dependents_MEDIAN_Premium Amount', 'SCALER_Number of Dependents_Q1_Premium Amount', 'SCALER_Number of Dependents_Q3_Premium Amount', 'SCALER_Number of Dependents_STD_Premium Amount', 'SCALER_Health Conscious Level_Q3_Premium Amount', 'SCALER_Insurance Duration_MEAN_Premium Amount', 'SCALER_Insurance Duration_MEDIAN_Premium Amount', 'SCALER_Insurance Duration_Q1_Premium Amount', 'SCALER_Insurance Duration_Q3_Premium Amount', 'SCALER_Health Conscious Level_MAX_Premium Amount', 'SCALER_Credit_Health_Score', 'SCALER_Occupation_Q3_Premium Amount', 'SCALER_Occupation_MEAN_Premium Amount', 'SCALER_Occupation_MAX_Premium Amount', 'SCALER_Occupation_MEDIAN_Premium Amount', 'SCALER_Occupation_Q1_Premium Amount', 'SCALER_Previous Claims_MIN_Premium Amount', 'SCALER_Insurance Duration_MAX_Premium Amount', 'SCALER_ENCODED_Occupation_Self-Employed', 'SCALER_Age', 'SCALER_Insurance Duration_STD_Premium Amount', 'SCALER_Occupation_STD_Premium Amount']

    df.rename(columns={old : new for old, new in zip(old_cols, new_cols)}, inplace=True)

    with gzip.open('models.pkl.gz', 'rb') as f:
        ml_model = pickle.load(f)

    avg_error = 0
    for model in ml_model:
        avg_error += model.predict(df)

    avg_error /= len(ml_model)
    avg_error
    ddf = df.T
    return np.expm1(avg_error), ddf.rename(columns={0 :"value"})