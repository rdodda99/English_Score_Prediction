import streamlit as st
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

def main():
    st.title("Student Exam Performance Prediction")

    # Get user inputs
    name = st.text_input("Name")
    gender = st.selectbox("Gender", ["male", "Female"])
    ethnicity = st.selectbox("Race or Ethnicity", ["group A", "Hispanic or Latino", "Asian", "Middle East", "Others"])
    parental_level_of_education = st.selectbox("Parental Level of Education", ["associate's degree", "Bachelor's degree", "High school", "Master's degree", "Some college", "Some high school"])
    lunch = st.selectbox("Fee Type", ["free/reduced", "Standard"])
    test_preparation_course = st.selectbox("attempted Mock Test", ["None", "Completed"])
    reading_score = st.number_input("Reading Score (out of 100)", min_value=0.0, max_value=100.0, step=1.0)
    writing_score = st.number_input("Writing Score (out of 100)", min_value=0.0, max_value=100.0, step=1.0)

    # Create CustomData object
    data = CustomData(
        gender=gender.lower(),
        race_ethnicity=ethnicity,
        parental_level_of_education=parental_level_of_education.lower(),
        lunch=lunch.lower(),
        test_preparation_course=test_preparation_course.lower(),
        reading_score=reading_score,
        writing_score=writing_score
    )

    # Get prediction
    if st.button("Predict"):
        pred_df = data.get_data_as_data_frame()
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        st.success(f"The predicted English score is: {results[0]}")

if __name__ == "__main__":
    main()