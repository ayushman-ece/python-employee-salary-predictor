from salary_predictor import SalaryPredictor

predictor = SalaryPredictor("employees.csv")

predictor.train_model()

try:
    age = int(input("\nEnter employee age: "))

    if age <= 0:
        print("Age must be greater than 0.")
        exit()

except ValueError:
    print("Invalid age. Please enter a number.")
    exit()


department = input("Enter department (IT/HR/Sales): ").strip()

valid_departments = ["IT", "HR", "Sales"]

if department not in valid_departments:
    print("Invalid department. Choose IT, HR, or Sales.")
    exit()


try:
    experience = int(input("Enter years of experience: "))

    if experience < 0:
        print("Experience cannot be negative.")
        exit()

except ValueError:
    print("Invalid experience. Please enter a number.")
    exit()


predictor.predict_salary(
    age,
    department,
    experience
)