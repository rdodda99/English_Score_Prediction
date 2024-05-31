# English Score Prediction
This project aims to predict the math score of students based on various factors, such as previous grades, family background, study habits, etc. The project uses a machine learning model trained on a dataset of student records.

## Features

- End-to-End ML Pipeline: The project encompasses an end-to-end machine learning pipeline, including data preprocessing, model training, evaluation, and deployment stages, ensuring a streamlined and efficient workflow.
- Dockerization: The entire project is containerized using Docker, promoting reproducibility and portability across different environments and systems.
- Continuous Integration and Delivery: GitHub Actions are integrated for continuous integration and delivery, enabling automated testing, building, and deployment processes.
- Cloud Deployment: The English score prediction model is deployed on AWS Elastic Beanstalk, a scalable and reliable hosting platform, ensuring high availability and performance.
- Flask Web Application: A user-friendly Flask web application is provided, allowing users to interact with the model through a intuitive interface, facilitating easy access and utilization of the prediction capabilities.


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

The web application provides a user-friendly interface where you can input various student attributes that influence their academic performance. These attributes include gender, writing score, and other relevant factors. Upon submitting the form, the application will leverage the trained machine learning model to generate a prediction of the student's English score based on the provided information. This prediction can assist educators, administrators, and students in understanding the potential English performance and identifying areas that may require additional support or intervention.
