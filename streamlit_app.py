# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 06:26:10 2023
@author: NEERAJA
"""

# Import necessary libraries
import pickle   # Import the 'pickle' module to load saved models
import streamlit as st   # Import the 'streamlit' library to create a web page
from streamlit_option_menu import option_menu   # Import 'option_menu' to create a sidebar in the web page

# Load saved machine learning models
# 'pickle.load(open('file_path', 'rb'))' loads a saved model from a file specified by 'file_path' in binary read mode ('rb').
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# Create a sidebar for navigation
with st.sidebar:
    # Create an option menu in the sidebar with the title 'Multiple Disease Prediction System'
    # and a list of prediction options.
    # option_menu: This is a function that creates a sidebar menu in Streamlit. It takes the title of the menu, a list of options, icons associated with each option, and a default selection index. It returns the selected option.
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        icons=['activity', 'heart', 'person'],  # Icons for each prediction type - taken from "bootstrap icons" website
        default_index=0  # Default selection
    )
         
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):

    # page title
    # st.title('Title Text'):
    # st.title() is a Streamlit method used to display a title or header on the web page.
    # 'Title Text' is the text that you want to display as the title.
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    # st.columns() is a Streamlit layout function used for organizing and creating columns within a Streamlit app or web page. It allows you to split the page into multiple columns, making it easier to arrange and display content side by side.
    col1, col2, col3 = st.columns(3)

    # The with statements are used to add content to each column. You can place widgets, text, or other content within each column to organize the layout of your Streamlit app.
    with col1:
        # st.text_input('Label Text'):
        # st.text_input() is a Streamlit method that creates an input field for users to enter text or numeric values.
        # 'Label Text' is the label or prompt that appears before the input field, providing context for the user.
        Pregnancies = st.text_input('Number of Pregnancies')
    
    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')

    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction
    # st.button('Button Text'):
    # st.button() is a Streamlit method that creates a clickable button on the web page.
    # 'Button Text' is the text displayed on the button.
    if st.button('Diabetes Test Result'):
        # The double square brackets [[]] are used to create a nested list or 2D array.
        # diabetes_model.predict() expects a 2D array-like input where each element of the outer list represents a sample, and the inner list contains the features or attributes of that sample.
        # Each feature value, such as Pregnancies, Glucose, etc., corresponds to a specific column in the dataset, and the model needs these values to make predictions.
        # Wrapping these feature values in double square brackets [[...]] creates a list of lists, where the outer list contains a single sample, and the inner list contains the feature values for that sample. This format ensures that the input is in the correct shape for the predict() method.
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The Person is DIABETIC'
        else:
          diab_diagnosis = 'The Person is NOT Diabetic'
    # st.success('Success Text'):
    # st.success() is a Streamlit method used to display a success message on the web page.
    # 'Success Text' is the text you want to display as a success message. This message is typically shown in a green-colored box to indicate a successful operation.
    st.success(diab_diagnosis)


# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        # The conversion of variables to integers or floats is done to ensure that the data passed to the heart_disease_model.predict() function is in the correct data type format that matches the expectations of the model. Here's why these conversions are applied:
        # Data Type Consistency: Machine learning models often expect input data to be in a specific data type. By converting the input data to the expected data type, you ensure that the model receives data in a consistent format.
        # Model Requirements: Some models, including many machine learning classifiers, require features to be in numeric format. Converting variables to integers or floats ensures that the data is in a numeric format suitable for the model's calculations.
        # Preventing Errors: In some cases, not providing data in the expected data type can lead to errors or unexpected behavior. Converting the variables to the correct data type helps prevent such issues.
        # Compatibility: Models trained on numeric data may not handle non-numeric data types well. Converting variables to integers or floats ensures compatibility with the model.
        # It's important to note that the specific data type conversions (e.g., int(age), float(oldpeak)) depend on the requirements and expectations of the heart_disease_model. You should consult the model's documentation or implementation to determine the correct data types for input features.
        heart_prediction = heart_disease_model.predict([[int(age), int(sex), int(cp), int(trestbps), int(chol), int(fbs), int(restecg), int(thalach), int(exang), float(oldpeak), int(slope), int(ca), int(thal)]])

        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The Person is having HEART DISEASE'
        else:
          heart_diagnosis = 'The Person does NOT have any Heart Disease'

    st.success(heart_diagnosis)


# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer_dB')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])

        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The Person has PARKINSON'S DISEASE"
        else:
          parkinsons_diagnosis = "The Person does NOT have Parkinson's Disease"

    st.success(parkinsons_diagnosis)
    

# Diabetes Features:
# Glucose Level (Glucose): The level of glucose (sugar) in the person's blood, typically measured in milligrams per deciliter (mg/dL). This is an important indicator in diabetes diagnosis.
# Blood Pressure value (BloodPressure): The person's blood pressure reading, often measured in millimeters of mercury (mm Hg). It includes both systolic and diastolic blood pressure values.
# Skin Thickness value (SkinThickness): The thickness of the skinfold at a specific site on the body, often measured in millimeters. Skin thickness can be relevant in health assessments.
# Insulin Level (Insulin): The level of insulin in the person's blood. Insulin is a hormone that regulates blood sugar levels. Measured in micro-international units per milliliter (µU/ml) or milligrams per deciliter (mg/dL).
# BMI value (BMI): The Body Mass Index (BMI) is a measure of body fat based on height and weight. It's calculated as weight (in kilograms) divided by the square of height (in meters). It's commonly used to assess whether a person is underweight, normal weight, overweight, or obese.
# Diabetes Pedigree Function value (DiabetesPedigreeFunction): A function that represents the likelihood of diabetes based on family history. It quantifies the genetic influence of diabetes on family members. The exact formula for this function can vary.
# Age: The age of the person, typically in years. Age can be a significant factor in assessing the risk of various medical conditions, including diabetes.
      

# Heart Disease Features:    
# Age: The age of the person.
# Sex: The gender of the person (e.g., 0 for female, 1 for male).
# Chest Pain types (cp): The type of chest pain the person is experiencing. This feature typically categorizes chest pain into different types (e.g., 0 for typical angina, 1 for atypical angina, 2 for non-anginal pain, 3 for asymptomatic).
# Resting Blood Pressure (trestbps): The resting blood pressure of the person in mm Hg (millimeters of mercury).
# Serum Cholestoral in mg/dl (chol): The serum cholesterol level of the person in milligrams per deciliter (mg/dL).
# Fasting Blood Sugar > 120 mg/dl (fbs): Indicates whether the fasting blood sugar level of the person is greater than 120 mg/dL (e.g., 0 for false, 1 for true).
# Resting Electrocardiographic results (restecg): The results of the resting electrocardiogram (ECG) test, often categorized into different classes (e.g., 0 for normal, 1 for having ST-T wave abnormality, 2 for showing probable or definite left ventricular hypertrophy by Estes' criteria).
# Maximum Heart Rate achieved (thalach): The maximum heart rate achieved during an exercise test.
# Exercise Induced Angina (exang): Indicates whether the person experienced exercise-induced angina during the exercise test (e.g., 0 for no, 1 for yes).
# ST depression induced by exercise (oldpeak): The ST segment depression induced by exercise relative to rest.
# Slope of the peak exercise ST segment (slope): Describes the slope of the ST segment during peak exercise (e.g., 0 for upsloping, 1 for flat, 2 for downsloping).
# Major vessels colored by fluoroscopy (ca): The number of major blood vessels colored by fluoroscopy during the procedure.
# Thal (thalassemia): A feature related to thalassemia, which is a genetic blood disorder. It is often categorized into different classes (e.g., 0 for normal, 1 for fixed defect, 2 for reversible defect).


# Parkinson's Features:
# MDVP:Fo(Hz) (fo): Represents the fundamental frequency of the voice signal in Hertz (Hz). It's a measure of the basic pitch of the voice.
# MDVP:Fhi(Hz) (fhi): Indicates the highest frequency component in the voice signal in Hertz (Hz). It measures the highest pitch.
# MDVP:Flo(Hz) (flo): Denotes the lowest frequency component in the voice signal in Hertz (Hz). It measures the lowest pitch.
# MDVP:Jitter(%) (Jitter_percent): Jitter is a measure of voice stability. It's represented as a percentage and quantifies the irregularity in pitch between consecutive voice cycles.
# MDVP:Jitter(Abs) (Jitter_Abs): Similar to jitter but represented as an absolute value. It quantifies the absolute difference in pitch between consecutive voice cycles.
# MDVP:RAP (RAP): Represents the relative average perturbation, another measure of voice stability.
# MDVP:PPQ (PPQ): Denotes the five-point period perturbation quotient, which is yet another measure of voice perturbation.
# Jitter:DDP (DDP): The difference between consecutive cycle-to-cycle jitter values.
# MDVP:Shimmer (Shimmer): Shimmer measures variations in amplitude or loudness of the voice signal, which can indicate voice instability.
# MDVP:Shimmer(dB) (Shimmer_dB): Similar to shimmer but represented in decibels (dB).
# Shimmer:APQ3 (APQ3): Amplitude perturbation quotient measured in a 3 ms window.
# Shimmer:APQ5 (APQ5): Amplitude perturbation quotient measured in a 5 ms window.
# MDVP:APQ (APQ): Amplitude perturbation quotient measured across the entire voice signal.
# Shimmer:DDA (DDA): The difference between consecutive cycle-to-cycle shimmer values.
# NHR: Noise-to-Harmonics Ratio, which quantifies the level of noise in the voice signal relative to harmonic components.
# HNR: Harmonic-to-Noise Ratio, a measure of the signal-to-noise ratio in the voice signal.
# RPDE: Recurrence Period Density Entropy, a measure of the complexity of the voice signal.
# DFA: Detrended Fluctuation Analysis, which characterizes the self-similarity or fractal nature of the voice signal.
# spread1 and spread2: These features are not further described in the code snippet, but they likely represent specific attributes related to Parkinson's disease diagnosis.
# D2: A feature related to voice characteristics, likely used for diagnosis.
# PPE: Pitch Period Entropy, a measure of the unpredictability of pitch periods in the voice signal.
