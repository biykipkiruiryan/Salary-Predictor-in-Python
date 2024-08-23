import pickle
import numpy as np
import streamlit as st

# Load the pre-trained machine learning model from a pickle file
model = pickle.load(open('model.pkl', 'rb'))

# Create columns for layout
col0, col1, col2, col3, col4, col5, col6 = st.columns(7)

# Define each column's content (for spacing or layout purposes)
with col0:
    st.write('')  # Empty column for spacing
with col1:
    st.write('')  # Empty column for spacing
with col2:
    st.write('')  # Empty column for spacing
with col3:
    st.title("GREY59")  # Title for the application
with col4:
    st.write('')  # Empty column for spacing
with col5:
    st.write('')  # Empty column for spacing
with col6:
    st.write('')  # Empty column for spacing

# Create another row of columns for additional layout
col7, col8, col9 = st.columns(3)

# Define each column's content
with col7:
    st.write('')  # Empty column for spacing
with col8:
    # Display the subtitle with custom HTML styling
    st.markdown("<h3 style='text-align: center;'>Machine Learning Salary Predictor</h3>", unsafe_allow_html=True)
with col9:
    st.write('')  # Empty column for spacing

# Define lists for user input options
gen_list = ["Female", "Male"]
edu_list = ["Bachelor's", "Master's", "PhD"]
job_list = ["Director of Marketing", "Director of Operations", "Senior Data Scientist", "Senior Financial Analyst", "Senior Software Engineer"]
job_idx = [0, 1, 10, 11, 20]  # Corresponding indices for job titles

# Create input widgets for user data
gender = st.radio('Pick your gender', gen_list)
age = st.slider('Pick your age', 21, 55)  # Age slider
education = st.selectbox('Pick your education level', edu_list)
job = st.selectbox('Pick your job title', job_list)
experience = st.slider('Pick your years of experience', 0.0, 25.0, 0.0, 0.5, "%1f")  # Experience slider

# Create a final row of columns for the prediction button
col10, col11, col12, col13, col14 = st.columns(5)
with col10:
    st.write('')  # Empty column for spacing
with col11:
    st.write('')  # Empty column for spacing
with col12:
    # Button to trigger the salary prediction
    predict_btn = st.button('Predict Salary')
with col13:
    st.write('')  # Empty column for spacing
with col14:
    st.write('')  # Empty column for spacing

# Check if the prediction button was clicked
if predict_btn:
    # Convert user inputs into the format expected by the model
    inp1 = int(age)  # Convert age to integer
    inp2 = float(experience)  # Convert experience to float
    inp3 = int(job_idx[job_list.index(job)])  # Convert job title to corresponding index
    inp4 = int(edu_list.index(education))  # Convert education level to corresponding index
    inp5 = int(gen_list.index(gender))  # Convert gender to corresponding index
    
    # Create input feature vector for prediction
    X = [inp1, inp2, inp3, inp4, inp5]
    
    # Predict salary using the loaded model
    salary = model.predict([X])
    
    # Create columns for displaying the prediction result
    col15, col16, col17 = st.columns(3)
    with col15:
        st.write('')  # Empty column for spacing
    with col16:
        # Display the estimated salary
        st.text(f"Estimated salary: ${int(salary[0])}")
    with col17:
        st.write('')  # Empty column for spacing
