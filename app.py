import pandas as pd
import pickle as pk
import streamlit as st

model=pk.load(open(r'C:/Users/VAISHNAVI/Downloads/project/House_prediction_model.pkl', 'rb'))
data=pd.read_csv(r'C:/Users/VAISHNAVI/Downloads/project/House_Prediction.csv')
st.header('Boston House Prediction')

# Streamlit inputs with min, max, and mean defaults
crim = st.number_input('Enter the crime rate',
                       min_value=float(data['CRIM'].min()),
                       max_value=float(data['CRIM'].max()),
                       value=float(data['CRIM'].mean()))

zn = st.number_input('Enter ZN',
                     min_value=float(data['ZN'].min()),
                     max_value=float(data['ZN'].max()),
                     value=float(data['ZN'].mean()))

indus = st.number_input('Enter INDUS',
                        min_value=float(data['INDUS'].min()),
                        max_value=float(data['INDUS'].max()),
                        value=float(data['INDUS'].mean()))

chas = st.number_input('Enter CHAS',
                       min_value=float(data['CHAS'].min()),
                       max_value=float(data['CHAS'].max()),
                       value=float(data['CHAS'].mean()))

nox = st.number_input('Enter NOX',
                      min_value=float(data['NOX'].min()),
                      max_value=float(data['NOX'].max()),
                      value=float(data['NOX'].mean()))

rm = st.number_input('Enter RM',
                     min_value=float(data['RM'].min()),
                     max_value=float(data['RM'].max()),
                     value=float(data['RM'].mean()))

age = st.number_input('Enter AGE',
                      min_value=float(data['AGE'].min()),
                      max_value=float(data['AGE'].max()),
                      value=float(data['AGE'].mean()))

dis = st.number_input('Enter DIS',
                      min_value=float(data['DIS'].min()),
                      max_value=float(data['DIS'].max()),
                      value=float(data['DIS'].mean()))

rad = st.number_input('Enter RAD',
                      min_value=float(data['RAD'].min()),
                      max_value=float(data['RAD'].max()),
                      value=float(data['RAD'].mean()))

tax = st.number_input('Enter TAX',
                      min_value=float(data['TAX'].min()),
                      max_value=float(data['TAX'].max()),
                      value=float(data['TAX'].mean()))

ptratio = st.number_input('Enter PTRATIO',
                          min_value=float(data['PTRATIO'].min()),
                          max_value=float(data['PTRATIO'].max()),
                          value=float(data['PTRATIO'].mean()))

b = st.number_input('Enter B',
                    min_value=float(data['B'].min()),
                    max_value=float(data['B'].max()),
                    value=float(data['B'].mean()))

lstat = st.number_input('Enter LSTAT',
                        min_value=float(data['LSTAT'].min()),
                        max_value=float(data['LSTAT'].max()),
                        value=float(data['LSTAT'].mean()))


input=pd.DataFrame([[crim,zn,indus,chas,nox,rm,age,dis,rad,tax,ptratio,b,lstat]],columns=["CRIM","ZN","INDUS","CHAS","NOX","RM","AGE","DIS","RAD","TAX","PTRATIO","B","LSTAT"])

if st.button("Predict Price"):
    output=model.predict(input)
    st.success(f"Predicted House Price: {output[0]*10000:.2f}$")