import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Sample dataset
data = {
    'Credit_Score': [650, 700, 550, 620, 750],
    'Income': [4000, 5000, 2000, 3500, 6000],
    'Loan_Amount': [10000, 12000, 5000, 8000, 15000],
    'Review_Sentiment': [0.8, 0.9, 0.6, 0.7, 0.95],  # Proxy from text analysis
    'Appointment_Bookings': [80, 90, 60, 70, 90], # from Salon 
    'Default': [0, 0, 1, 0, 0]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Display sample data to the user
print("\n--- Historical Data ---")
print(df)


# Features and target
X = df[['Credit_Score', 'Income', 'Loan_Amount', 'Review_Sentiment', 'Appointment_Bookings']]
y = df['Default']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))


# Take user input for classification
while True:
    user_choice = input("\nDo you want to classify a new data point? (yes/no): ").strip().lower()
    if user_choice != 'yes':
        print("Exiting the program.")
        break

    try:
        # Get user input for features
        credit_score = float(input("Enter Credit Score: "))
        income = float(input("Enter Income: "))
        loan_amount = float(input("Enter Loan Amount: "))
        review_sentiment = float(input("Enter Review Sentiment (0 to 1): "))
        appointment_booking = float(input("Enter Appointment Bookings: "))

        # Create a DataFrame for the new data
        new_data = pd.DataFrame([{
            'Credit_Score': credit_score,
            'Income': income,
            'Loan_Amount': loan_amount,
            'Review_Sentiment': review_sentiment,
            'Appointment_Bookings' : appointment_booking
        }])

        # Predict using the trained model
        prediction = model.predict(new_data)[0]
        print(f"Prediction: {'Default' if prediction == 1 else 'No Default'}")

    except ValueError as e:
        print(f"Invalid input. Please try again. Error: {e}")