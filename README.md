# 🩺 Dr. ML – Intelligent Disease Prediction System

## 📌 Overview

Dr. ML is an end-to-end Machine Learning-powered healthcare prediction platform designed to assist in the early detection of **Diabetes** and **Heart Disease**. The project combines Machine Learning, FastAPI, and Streamlit to deliver a seamless experience for generating disease risk predictions based on patient health parameters.

The primary goal of this project is to demonstrate how machine learning models can be transformed into a production-ready application using modern development practices, modular architecture, API integration, and an interactive user interface.

The application is designed to be scalable, maintainable, and easy to extend with additional disease prediction models in the future.

---

## 🎯 Project Objectives

This project was developed with the following objectives:

- Predict the likelihood of Diabetes and Heart Disease using Machine Learning.
- Compare multiple machine learning algorithms and select the best-performing models.
- Build reusable training pipelines for different disease prediction tasks.
- Create a centralized configuration management system.
- Develop an intuitive and responsive web interface.
- Follow industry-standard software engineering practices.
- Prepare the application for cloud deployment.

---

## 📊 Data Collection and Preprocessing

The foundation of any successful machine learning project lies in data quality. The datasets used in this project contain medical records and health-related attributes commonly associated with Diabetes and Heart Disease diagnosis.

### Data Cleaning

The datasets were carefully examined for:

- Missing values
- Invalid values
- Duplicate records
- Inconsistent data formats

### Missing Value Handling

Medical datasets often contain missing or unrealistic values. These issues were addressed through:

- Missing value identification
- Median-based imputation
- Data consistency checks

### Feature Engineering

Relevant features were transformed and prepared for model training using:

- Data transformations
- Statistical normalization
- Feature scaling

### Train-Test Split

To evaluate model performance fairly, the datasets were divided into:

- Training Dataset
- Testing Dataset

This ensures the models can generalize effectively to unseen data.

---

## 🤖 Model Development

Rather than selecting a machine learning model directly, multiple algorithms were trained and evaluated to determine the most effective solution.

Models explored during experimentation included:

- Logistic Regression
- Support Vector Machine (SVM)
- Random Forest
- Additional baseline classification algorithms

Each model was trained under similar conditions and evaluated using consistent metrics to ensure a fair comparison.

---

## 🔍 Hyperparameter Tuning

Once the best-performing models were identified, hyperparameter optimization was performed to further improve predictive performance.

The tuning process focused on:

- Increasing prediction accuracy
- Improving model generalization
- Reducing overfitting
- Enhancing Recall and F1 Score

The optimized hyperparameters were stored in a dedicated YAML configuration file, ensuring reproducibility and easier experimentation.

---

## 🏆 Final Model Selection

After extensive experimentation and evaluation, the final models were selected based on their overall performance.

### Diabetes Prediction Model

A tuned **Support Vector Machine (SVM)** model was selected and integrated with a preprocessing pipeline.

### Heart Disease Prediction Model

A tuned **Random Forest Classifier** was selected due to its ability to capture complex relationships within patient health records.

Both models demonstrated strong performance and were chosen for deployment.

---

## ⚙️ Machine Learning Pipeline

To ensure consistency between training and prediction, complete machine learning pipelines were created.

Each pipeline performs:

### Data Preprocessing

- Missing value handling
- Data transformation
- Feature scaling

### Model Prediction

- Loading trained models
- Processing incoming patient data
- Generating predictions
- Producing confidence scores

This approach guarantees that the same preprocessing steps used during training are also applied during inference.

---

## 💾 Model Serialization

After training, the complete machine learning pipelines were serialized using **Joblib**.

Benefits of model serialization include:

- Faster deployment
- No need for retraining
- Easy portability
- Consistent predictions

The saved models can be loaded instantly whenever prediction requests are received.

---

## 🚀 FastAPI Backend Development

To serve machine learning predictions efficiently, FastAPI was integrated as the backend framework.

The FastAPI layer is responsible for:

### Request Handling

Receiving prediction requests from the frontend.

### Input Validation

Ensuring that incoming data follows the required format.

### Model Inference

Passing validated inputs to the prediction engine.

### Response Generation

Returning structured prediction results in JSON format.

### Why FastAPI?

FastAPI was selected because of its:

- High performance
- Automatic API documentation
- Built-in data validation
- Scalability
- Production readiness

---

## 📋 Data Validation with Pydantic

Input validation is performed using **Pydantic Schemas**.

Pydantic ensures:

- Correct data types
- Required field validation
- Input consistency
- Error prevention

This prevents invalid or incomplete data from reaching the machine learning models.

---

## 🔧 Configuration Management

A centralized configuration system was implemented to manage:

- Dataset locations
- Model paths
- API URLs
- Logging settings
- Training parameters

This improves maintainability and eliminates hardcoded values throughout the codebase.

---

## 🧠 Prediction Service Layer

A dedicated prediction service was created to separate business logic from API logic.

The service layer is responsible for:

- Loading trained models
- Data transformation
- Prediction generation
- Probability calculation
- Error handling

This separation makes the code cleaner, more maintainable, and easier to scale.

---

## 🎨 Streamlit Frontend

The user interface was developed using **Streamlit** to provide a clean and interactive experience.

Users can:

- Enter medical information
- Submit prediction requests
- View prediction results instantly
- Understand risk probabilities

Custom CSS styling was added to improve:

- Visual appearance
- User experience
- Responsiveness
- Professional design

---

## 🌐 Frontend and Backend Integration

The application follows a client-server architecture.

### Workflow

1. User enters medical information through the Streamlit interface.
2. Streamlit creates a structured request payload.
3. FastAPI receives and validates the request.
4. The prediction service loads the appropriate model.
5. The model generates a prediction.
6. FastAPI returns the prediction result.
7. Streamlit displays the outcome and confidence score.

This architecture allows complete separation between the user interface and machine learning logic.

---

## ☁️ Cloud Deployment

The application was prepared for deployment on cloud infrastructure using **AWS EC2**.

Deployment activities included:

- Virtual environment setup
- Dependency installation
- FastAPI server configuration
- Streamlit deployment
- API communication testing
- Production readiness validation

This demonstrates the complete lifecycle of a machine learning project from development to deployment.

---

## 📈 Key Features

✅ Diabetes Risk Prediction

✅ Heart Disease Risk Prediction

✅ Machine Learning Pipelines

✅ Hyperparameter Optimization

✅ FastAPI 

✅ Pydantic Data Validation

✅ Streamlit Frontend

✅ Modular Project Architecture

✅ Configuration Management

✅ Logging System

✅ Cloud Deployment Ready

---

## 🛠️ Technology Stack

### Machine Learning

- Python
- Scikit-Learn
- NumPy
- Pandas
- Joblib

### Backend

- FastAPI
- Pydantic
- Uvicorn

### Frontend

- Streamlit
- HTML
- CSS

### Deployment

- AWS EC2
- Linux
- Git & GitHub

---

## ⚠️ Disclaimer

This application is intended for **educational and informational purposes only**.

Predictions generated by the machine learning models should **not** be interpreted as professional medical advice, diagnosis, or treatment recommendations.

Healthcare decisions should always be made in consultation with qualified medical professionals. The results provided by Dr. ML are probabilistic estimates based on historical medical data and are not a substitute for clinical evaluation.

---

## 👨‍💻 Author

### Kaushal Kumar

B.Tech Computer Science Engineering

Machine Learning & AI Enthusiast

Focused on building practical AI applications that bridge the gap between machine learning research and real-world deployment.

⭐ If you found this project helpful, consider giving it a star on GitHub!
