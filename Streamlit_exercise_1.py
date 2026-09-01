import streamlit as st
import pandas as pd
st.title('Bank Account Opening Form')

st.header('Account Details')

fN = st.text_input('First Name')
mN = st.text_input('Middle Name')
lN = st.text_input('Last Name')

address = st.text_input('Address')

email = st.text_input('Email')

dob = st.date_input('Date of Birth')

pN = st.text_input('Phone Number')

accType = st.selectbox('Account Type',['Savings','Current','Fixed Deposit'])

terms = st.checkbox('I agree to the terms and conditions.')

submit = st.button(label='Submit')

if submit:
    st.text('Form submitted successfully.✅')

    st.subheader('Your Data')
    df = st.dataframe({
        'First Name':fN,
        'Middle Name':mN,
        'Last Name':lN,
        'Address':[address],
        'Email':email,
        'Date of Birth':dob,
        'Account Type':accType,
        'Contact Info':pN
    })
if not fN:
    st.error('First name is mandatory!')
if not lN:
    st.error('Last name is mandatory!')
if not terms:
    st.error('Please accept the terms and conditions.')
if not all([address,email,dob,pN,accType]):
    st.error('All fields are mandatory.')
