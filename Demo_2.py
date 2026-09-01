import streamlit as st
import pandas as pd
st.header('Student Enrollment Form')

st.write('Enter your details : ')

name = st.text_input("Enter your name : ",placeholder='Name')

age = st.number_input("Enter your age :",step=1,min_value=1,max_value=100,placeholder='Age')

date  = st.date_input('Enter your preferred date for enrollment:')

gender = st.radio('Choose your Gender',options=['Male','Female','Others'],horizontal=True)

courses = st.selectbox('Select your course',['AI','ML','CS'])
optional_subjects = st.multiselect('Choose optional subjects',['Python','C','Django'])
photo = st.file_uploader('Upload your photo')

agreed = st.checkbox('I agree to fees details')

submit = st.button('Submit')
if not name:
    st.error('Name is mandatory field!')
if not photo:
    st.error('Photo is mandatory!')
if not agreed:
    st.error('Please agree to our terms to enroll!')
if all([name,gender,agreed]):
    # st.write(f'Hello {name}. You are {age} years old. Your enrollment date is : {date}. Your gender is {gender}.\nYou chose {courses} as major and {",".join(optional_subjects)} as optional subject.')
    df = pd.DataFrame({
        'Name':name,
        'Age':age,
        'Date':date,
        'Gender':[gender],
        'Course':courses
    })

    st.write(df)
    if photo:
        st.image(photo)
