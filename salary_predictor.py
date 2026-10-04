import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

class SalaryPredictor:

    def __init__(self, file_name):
        self.data = pd.read_csv(file_name)
        
    
    def prepare_data(self):
        X = self.data[["Age", "Department", "Experience"]]
        y = self.data["Salary"]

        X = pd.get_dummies(
            X,
            columns=["Department"],
            dtype=int
        )

        self.feature_columns = X.columns

        return X, y
            
    def split_data(self):
        X, y = self.prepare_data()

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        print("\n===== TRAIN/TEST SPLIT =====")
        print(f"Training samples : {len(X_train)}")
        print(f"Testing samples  : {len(X_test)}")
                
            
            
    
    def train_model(self):
        X, y = self.prepare_data()

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        self.model = LinearRegression()

        self.model.fit(X_train, y_train)

        print("\n===== MODEL TRAINED =====")
        print("Linear Regression model trained successfully. ✅")
        
    
        predictions = self.model.predict(X_test)

        mae = mean_absolute_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)

        print("\n===== MODEL EVALUATION =====")
        print(f"Mean Absolute Error : ₹{mae:.2f}")
        print(f"R2 Score            : {r2:.4f}")
        
    
    def predict_salary(self, age, department, experience):
        new_employee = pd.DataFrame({
            "Age": [age],
            "Department": [department],
            "Experience": [experience]
        })

        new_employee = pd.get_dummies(
            new_employee,
            columns=["Department"],
            dtype=int
        )

        new_employee = new_employee.reindex(
            columns=self.feature_columns,
            fill_value=0
        )

        prediction = self.model.predict(new_employee)

        print("\n===== SALARY PREDICTION =====")
        print(f"Age        : {age}")
        print(f"Department : {department}")
        print(f"Experience : {experience} years")
        print(f"Predicted Salary : ₹{prediction[0]:.2f}")