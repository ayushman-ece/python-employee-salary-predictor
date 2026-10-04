# 💰 Employee Salary Predictor

A beginner-friendly Machine Learning project that predicts an employee's salary using **Linear Regression** based on age, department, and years of experience.

This project is part of my Python → Data Science → Machine Learning learning journey.

---

## 🚀 Project Overview

The **Employee Salary Predictor** takes employee information such as:

- Age
- Department
- Years of Experience

and uses a trained **Linear Regression** model to predict the employee's salary.

The project demonstrates a complete basic Machine Learning workflow:

```text
Dataset
   ↓
Feature Selection
   ↓
Data Preprocessing
   ↓
One-Hot Encoding
   ↓
Train/Test Split
   ↓
Model Training
   ↓
Model Evaluation
   ↓
New Employee Input
   ↓
Salary Prediction
```

---

## 🎯 Objective

The main objective of this project is to understand how a real Machine Learning pipeline works from beginning to end.

The project focuses on learning:

- Features and target variables
- Categorical data encoding
- Train/test splitting
- Linear Regression
- Model training
- Model prediction
- Model evaluation
- MAE
- R² Score
- Input validation
- Preparing new data for prediction

---

## 🧠 Machine Learning Concepts

### 1. Features and Target

The input features are:

```text
Age
Department
Experience
```

The target variable is:

```text
Salary
```

In Machine Learning:

```text
X → Features
y → Target
```

The model learns the relationship between employee information and salary.

---

### 2. One-Hot Encoding

The `Department` column contains categorical values:

```text
IT
HR
Sales
```

Linear Regression requires numerical input, so categorical values are converted into numerical columns using:

```python
pd.get_dummies()
```

For example:

```text
Department    →    Department_HR    Department_IT    Department_Sales

IT                     0                  1                  0
HR                     1                  0                  0
Sales                  0                  0                  1
```

---

### 3. Train/Test Split

The dataset is divided into:

```text
80% → Training Data
20% → Testing Data
```

Training data is used to teach the model.

Testing data is used to evaluate how well the model performs on unseen data.

The split uses:

```python
random_state=42
```

so that the same random split can be reproduced.

---

### 4. Linear Regression

The project uses:

```python
LinearRegression()
```

The model learns a relationship between the input features and salary.

The trained model can then generate salary predictions for new employees.

---

### 5. Model Evaluation

Two evaluation metrics are used.

#### Mean Absolute Error (MAE)

MAE measures the average absolute difference between actual and predicted salary.

For example:

```text
MAE = ₹5,000
```

means the model's predictions are, on average, ₹5,000 away from the actual values.

#### R² Score

R² measures how well the model explains the variation in the target variable.

A higher R² generally indicates a better fit.

---

## 📊 Dataset

The project uses a small sample employee dataset.

```csv
Name,Age,Department,Salary,Experience
Rahul,21,IT,50000,1
Aman,22,HR,42000,1
Priya,23,IT,65000,2
Neha,21,Sales,48000,1
Arjun,24,IT,58000,3
Simran,22,HR,45000,2
Riya,23,Sales,52000,2
Karan,25,IT,72000,4
Pooja,24,HR,55000,3
Vikas,26,Sales,60000,5
```

> **Note:** This dataset contains only 10 records, so the model is intended for learning and demonstration rather than real-world salary prediction.

---

## 🗂️ Project Structure

```text
python-employee-salary-predictor/
│
├── main.py
├── salary_predictor.py
├── employees.csv
├── requirements.txt
├── .gitignore
└── REMEAD.md
```

### `main.py`

Handles:

- Starting the predictor
- Training the model
- Taking employee input
- Validating input
- Calling the prediction method

### `salary_predictor.py`

Contains the main Machine Learning logic:

- Loading the dataset
- Preparing features
- One-hot encoding
- Train/test splitting
- Training Linear Regression
- Evaluating the model
- Predicting salary

### `employees.csv`

Contains the employee training dataset.

### `requirements.txt`

Contains the Python dependencies required to run the project.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/ayushman-ece/python-employee-salary-predictor.git
```

Move into the project directory:

```bash
cd python-employee-salary-predictor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

Run:

```bash
python main.py
```

The program will first train and evaluate the model.

Then it will ask for information about a new employee.

Example:

```text
Enter employee age: 24
Enter department (IT/HR/Sales): IT
Enter years of experience: 3
```

The program then produces a predicted salary.

Example:

```text
===== SALARY PREDICTION =====
Age        : 24
Department : IT
Experience : 3 years
Predicted Salary : ₹...
```

---

## 🛡️ Input Validation

The program validates user input.

### Age

The program checks that:

- Age is a number
- Age is greater than 0

### Department

Only these departments are accepted:

```text
IT
HR
Sales
```

### Experience

The program checks that:

- Experience is a number
- Experience is not negative

---

## 🔄 Prediction Pipeline

When a new employee is entered:

```text
User Input
    ↓
Create DataFrame
    ↓
One-Hot Encode Department
    ↓
Match Training Feature Columns
    ↓
Send Data to Trained Model
    ↓
Generate Salary Prediction
```

The project uses:

```python
reindex()
```

to ensure the new employee's feature columns match the columns used during training.

---

## 🧰 Technologies Used

- Python
- Pandas
- Scikit-learn
- Linear Regression
- CSV
- Data Preprocessing
- Machine Learning

---

## 📦 Requirements

The project requires:

```text
pandas
scikit-learn
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## 📚 What I Learned

Through this project, I learned how to:

1. Load a dataset using Pandas
2. Separate features and target
3. Encode categorical data
4. Split data into training and testing sets
5. Train a Linear Regression model
6. Generate predictions
7. Evaluate a Machine Learning model
8. Understand MAE and R²
9. Store a trained model using `self.model`
10. Prepare new data for prediction
11. Match prediction features with training features
12. Validate user input
13. Build a complete beginner Machine Learning application

---

## ⚠️ Limitations

This project uses only 10 employee records.

Therefore:

- The dataset is too small for reliable real-world predictions.
- Model evaluation scores may change significantly with different datasets.
- Salary depends on many factors that are not included here.
- Department is represented using a simple categorical encoding.

This project is primarily designed for **learning Machine Learning fundamentals**.

---

## 🔮 Future Improvements

Possible improvements include:

- Use a much larger dataset
- Add education level
- Add job role
- Add location
- Add company size
- Add more years of experience
- Compare multiple ML algorithms
- Add Random Forest Regression
- Add Decision Tree Regression
- Improve model evaluation
- Add data visualization
- Build a GUI
- Build a Streamlit web application
- Save the trained model using Joblib
- Deploy the model as an API

---

## 👨‍💻 Author

**Ayushman Tiwari**

GitHub:  
https://github.com/ayushman-ece

---

## ⭐ Learning Journey

This project is part of my long-term journey from:

```text
Python
   ↓
Data Analysis
   ↓
Data Science
   ↓
Machine Learning
   ↓
Deep Learning
   ↓
NLP
   ↓
LLMs
   ↓
RAG
   ↓
Agentic AI
```

The goal is to build practical projects while learning the underlying concepts step-by-step.