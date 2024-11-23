# loan_risk.py

# Collecting basic user data
print("Welcome to the Loan Risk Assessment Tool!")

# Input data
credit_score = int(input("Enter the credit score (300-850): "))
monthly_income = float(input("Enter the monthly income (SAR): "))
loan_amount = float(input("Enter the loan amount (SAR): "))

# Basic Risk Assessment Logic
if credit_score < 600:
    risk = "High"
elif credit_score < 700:
    risk = "Moderate"
else:
    risk = "Low"

# Output results
print("\n--- Risk Assessment Report ---")
print(f"Credit Score: {credit_score}")
print(f"Monthly Income: ${monthly_income}")
print(f"Loan Amount: ${loan_amount}")
print(f"Loan Default Risk: {risk}")
