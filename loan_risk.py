import pandas as pd

# Load historical loan data
data = pd.DataFrame({
    "Credit Score": [580, 620, 750, 680, 520],
    "Loan Amount": [5000, 10000, 15000, 7000, 2000],
    "Income": [2000, 4000, 6000, 3500, 1500],
    "Risk": ["High", "Moderate", "Low", "Moderate", "High"]
})

# Display sample data to the user
print("\n--- Historical Data ---")
print(data)

# Collecting new user data
credit_score = int(input("Enter the credit score (300-850): "))
monthly_income = float(input("Enter the monthly income ($): "))
loan_amount = float(input("Enter the loan amount ($): "))

# Assess risk based on user data
if credit_score < 600:
    risk = "High"
elif credit_score < 700:
    risk = "Moderate"
else:
    risk = "Low"

print("\n--- Risk Assessment ---")
print(f"Based on historical trends, your loan risk is: {risk}")
