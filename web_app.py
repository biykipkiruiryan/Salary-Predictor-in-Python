import pickle
import numpy as np
import streamlit as st

# Load the pre-trained machine learning model from a pickle file
model = pickle.load(open('model.pkl', 'rb'))

# Apply custom CSS for a sleek, modern design
st.markdown("""
    <style>
    /* Center alignment for the entire app */
    .centered-content {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        padding: 20px;
        margin-top: 20px;
    }
    /* Modern card style */
    .card {
        background-color: #ffffff;
        padding: 20px;
        margin: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        border-left: 5px solid #1f77b4;
        transition: 0.3s;
    }
    /* Hover effect for the card */
    .card:hover {
        box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.15);
    }
    /* Button style */
    .btn-primary {
        background-color: #1f77b4;
        color: white;
        padding: 10px 30px;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
        border: none;
        transition: 0.3s;
    }
    .btn-primary:hover {
        background-color: #125a82;
    }
    /* Center the title with modern typography */
    .title {
        text-align: center;
        color: #1f77b4;
        font-family: 'Helvetica Neue', sans-serif;
        margin-bottom: 0px;
    }
    /* Subtitle with a sleek, thin font */
    .subtitle {
        text-align: center;
        color: #555555;
        font-family: 'Helvetica Neue', sans-serif;
        margin-top: 0px;
        margin-bottom: 30px;
        font-weight: 300;
    }
    /* Input labels with subtle gray color */
    .stRadio label, .stSlider label, .stSelectbox label {
        color: #333333;
    }
    </style>
""", unsafe_allow_html=True)

# Layout for title and subtitle
st.markdown("<h1 class='title'>Sleek Salary Predictor</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='subtitle'>Powered by Machine Learning</h3>", unsafe_allow_html=True)

# Create a card layout for the input section
with st.container():
    st.markdown("<div class='card centered-content'>", unsafe_allow_html=True)
    
    # Create input widgets for user data with aligned styling
    gender = st.radio('Select Gender', ["Female", "Male"])
    age = st.slider('Select Age', 21, 55)  # Age slider
    education = st.selectbox('Select Education Level', ["Bachelor's", "Master's", "PhD"])
    job = st.selectbox('Select Job Title', ["Director of Marketing", "Director of Operations", "Senior Data Scientist", "Senior Financial Analyst", "Senior Software Engineer"])
    experience = st.slider('Years of Experience', 0.0, 25.0, 0.0, 0.5, "%1f")  # Experience slider

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
