import pandas as pd
import pickle as pk
import streamlit as st

model=pk.load(open(r'House_prediction_model.pkl', 'rb'))
data=pd.read_csv(r'House_Prediction.csv')
st.header('Boston House Prediction')

# Streamlit inputs with min, max, and mean defaults
# Convert values into percentages (0–100 scale)
crim = st.number_input('Crime rate (%)',
                       min_value=0.0,
                       value=0.0)

zn = st.number_input('Residential land zoned (%)',
                     min_value=0.0,
                     value=0.0)

indus = st.number_input('Industry proportion (%)',
                        min_value=0.0,
                        value=0.0)

chas = st.radio('Near Charles River?',("No","Yes"))
chas=1 if chas =="Yes" else 0
                      

nox = st.number_input('Air pollution (NOX %) ',
                      min_value=0.0,
                      value=0.0)

rm = st.number_input('Average rooms (%)',
                     min_value=0.0,
                     value=0.0)

age = st.number_input('Older houses (%)',
                      min_value=0.0,
                      value=0.0)

dis = st.number_input('Distance to employment centres (%)',
                      min_value=0.0,
                      value=0.0)

rad = st.number_input('Highway accessibility (%)',
                      min_value=0.0,
                      value=0.0)

tax = st.number_input('Property tax (%)',
                      min_value=0.0,
                      value=0.0)

ptratio = st.number_input('Student–teacher ratio (%)',
                          min_value=0.0,
                          value=0.0)

b = st.number_input('Demographic index (B value %) ',
                    min_value=0.0,
                    value=0.0)

lstat = st.number_input('Lower status population (%)',
                        min_value=0.0,
                        value=0.0)                    
       


input=pd.DataFrame([[crim,zn,indus,chas,nox,rm,age,dis,rad,tax,ptratio,b,lstat]],columns=["CRIM","ZN","INDUS","CHAS","NOX","RM","AGE","DIS","RAD","TAX","PTRATIO","B","LSTAT"])

if st.button("Predict Price"):
    output=model.predict(input)
    st.success(f"Predicted House Price: {output[0]*1000:.2f}$")