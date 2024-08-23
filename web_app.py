import pickle
import numpy as np
import streamlit as st

# Load the pre-trained machine learning model from a pickle file
model = pickle.load(open('model.pkl', 'rb'))

# Apply custom CSS for Bootstrap-like styling
st.markdown("""
    <style>
    /* Center alignment for the entire app */
    .centered-content {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    /* Bootstrap-like card style */
    .card {
        padding: 20px;
        margin: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        transition: 0.3s;
        background-color: #f8f9fa;
    }
    /* Hover effect for the card */
    .card:hover {
        box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
    }
    /* Button style */
    .btn-primary {
        background-color: #007bff;
        border-color: #007bff;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
    }
    .btn-primary:hover {
        background-color: #0056b3;
    }
    /* Center the title */
    .title {
        text-align: center;
        color: #343a40;
    }
    /* Center the subtitle */
    .subtitle {
        text-align: center;
        color: #6c757d;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Layout for title and subtitle
st.markdown("<h1 class='title'>GREY59</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='subtitle'>Machine Learning Salary Predictor</h3>", unsafe_allow_html=True)

# Create a card layout for the input section
with st.container():
    st.markdown("<div class='card centered-content'>", unsafe_allow_html=True)
    
    # Create input widgets for user data
    gender = st.radio('Pick your gender', ["Female", "Male"])
    age = st.slider('Pick your age', 21, 55)  # Age slider
    education = st.selectbox('Pick your education level', ["Bachelor's", "Master's", "PhD"])
    job = st.selectbox('Pick your job title', ["Director of Marketing", "Director of Operations", "Senior Data Scientist", "Senior Financial Analyst", "Senior Software Engineer"])
    experience = st.slider('Pick your years of experience', 0.0, 25.0, 0.0, 0.5, "%1f")  # Experience slider

    # Button to trigger the salary prediction
    predict_btn = st.markdown('<button class="btn-primary">Predict Salary</button>', unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Check if the prediction button was clicked
if st.button('Predict Salary'):
    # Convert user inputs into the format expected by the model
    inp1 = int(age)  # Convert age to integer
    inp2 = float(experience)  # Convert experience to float
    inp3 = int(["Director of Marketing", "Director of Operations", "Senior Data Scientist", "Senior Financial Analyst", "Senior Software Engineer"].index(job))  # Convert job title to corresponding index
    inp4 = int(["Bachelor's", "Master's", "PhD"].index(education))  # Convert education level to corresponding index
    inp5 = int(["Female", "Male"].index(gender))  # Convert gender to corresponding index
    
    # Create input feature vector for prediction
    X = [inp1, inp2, inp3, inp4, inp5]
    
    # Predict salary using the loaded model
    salary = model.predict([X])
    
    # Display the estimated salary
    st.markdown(f"<div class='card centered-content'><h4>Estimated Salary: ${int(salary[0]):,}</h4></div>", unsafe_allow_html=True)
