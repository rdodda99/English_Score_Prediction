# Student Performance Prediction

This project aims to predict the math score of students based on various factors, such as previous grades, family background, study habits, etc. The project uses a machine learning model trained on a dataset of student records.

## Features

- End-to-end ML pipeline that includes data preprocessing, model training, evaluation, and deployment
- Dockerization of the project to ensure reproducibility and portability
- Continuous integration and delivery using GitHub Actions
- Deployment to AWS Elastic Beanstalk for scalable and reliable hosting
- Flask web application that provides a user interface for interacting with the model

Link to access the deployed application - [StudentPerformancePrediction](http://studentperformance-env.eba-gjnxjvpq.eu-north-1.elasticbeanstalk.com/)

## Requirements

- Python 3.8 or higher
- Docker
- AWS account and credentials for deploying (Optional)

## Installation

1. Clone this repository to your local machine
2. Navigate to the project directory and run `docker build -t student-performance .` to build the Docker image
3. Run `docker run -p 8080:8080 student-performance` to start the Flask app
4. Open your browser and go to `http://localhost:8080` to see the app

## Usage

The web app allows you to enter the values of the features that affect the student performance, such as gender, writing score, etc. After submitting the form, the app will display the predicted math score.
