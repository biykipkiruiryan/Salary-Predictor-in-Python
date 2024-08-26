import pickle
import numpy as np
import streamlit as st

# Load the machine learning model from 'model.pkl'
model = pickle.load(open('model.pkl', 'rb'))

# Create 7 columns for layout
col0, col1, col2, col3, col4, col5, col6 = st.columns(7)
with col0:
    st.write('')  # Empty column for spacing
with col1:
    st.write('')  # Empty column for spacing
with col2:
    st.write('')  # Empty column for spacing
with col3:
    st.title("GREY59")  # Centered title
with col4:
    st.write('')  # Empty column for spacing
with col5:
    st.write('')  # Empty column for spacing
with col6:
    st.write('')  # Empty column for spacing

# Create 3 columns for the subtitle
col7, col8, col9 = st.columns(3)
with col7:
    st.write('')  # Empty column for spacing
with col8:
    # Centered subtitle using markdown with HTML for styling
    st.markdown("<h6 style='text-align: center;'>A simple web app to predict annual salary</h6>", unsafe_allow_html=True)
with col9:
    st.write('')  # Empty column for spacing

# Define the lists for user input options
gen_list = ["Female", "Male"]  # Gender options
edu_list = ["Bachelor's", "Master's", "PhD"]  # Education level options
job_list = ["Director of Marketing", "Director of Operations", "Senior Data Scientist", "Senior Financial Analyst", "Senior Software Engineer"]  # Job title options
job_idx = [0, 1, 10, 11, 20]  # Indices corresponding to job titles in the model

# User inputs
gender = st.radio('Pick your gender', gen_list)  # Radio button for gender selection
age = st.slider('Pick your age', 21, 55)  # Slider for age selection (range 21 to 55)
education = st.selectbox('Pick your education level', edu_list)  # Dropdown for education level
job = st.selectbox('Pick your job title', job_list)  # Dropdown for job title
experience = st.slider('Pick your years of experience', 0.0, 25.0, 0.0, 0.5, "%1f")  # Slider for experience (0 to 25 years, step of 0.5)

# Create 5 columns for the Predict button layout
col10, col11, col12, col13, col14 = st.columns(5)
with col10:
    st.write('')  # Empty column for spacing
with col11:
    st.write('')  # Empty column for spacing
with col12:
    predict_btn = st.button('Predict Salary')  # Centered button to trigger the prediction
with col13:
    st.write('')  # Empty column for spacing
with col14:
    st.write('')  # Empty column for spacing

# If the Predict Salary button is pressed
if(predict_btn):
    inp1 = int(age)  # Convert age to integer
    inp2 = float(experience)  # Convert experience to float
    inp3 = int(job_idx[job_list.index(job)])  # Map job title to its corresponding index
    inp4 = int(edu_list.index(education))  # Map education level to its corresponding index
    inp5 = int(gen_list.index(gender))  # Map gender to its corresponding index
    X = [inp1, inp2, inp3, inp4, inp5]  # Create a feature array for prediction
    salary = model.predict([X])  # Predict the salary using the model
    # Display the predicted salary
    col15, col16, col17 = st.columns(3)
    with col15:
        st.write('')  # Empty column for spacing
    with col16:
        st.text(f"Estimated salary: ${int(salary[0])}")  # Display the estimated salary
    with col17:
        st.write('')  # Empty column for spacing
