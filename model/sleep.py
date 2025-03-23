import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression

# Sample dataset (sleep hours vs. quality)
X = np.array([[4], [5], [6], [7], [8]])  # Hours of sleep
y = np.array([0, 0, 1, 1, 1])  # Poor (0) or Good (1)

# Train Model
model = LogisticRegression()
model.fit(X, y)

# Save Model
def save_model(model, filename="sleep_model.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(model, f)

save_model(model)

# Function to predict sleep quality
def predict_sleep_quality(hours):
    try:
        with open("sleep_model.pkl", "rb") as f:
            model = pickle.load(f)
        if hours < 0:
            raise ValueError("Hours of sleep cannot be negative.")
        prediction = model.predict([[hours]])[0]
        return "Good Sleep" if prediction == 1 else "Poor Sleep"
    except Exception as e:
        return f"Error: {str(e)}"

# Additional function to provide sleep recommendations
def get_sleep_recommendation(hours):
    if hours < 5:
        return "You should sleep more! Aim for at least 7 hours."
    elif 5 <= hours < 7:
        return "Your sleep is decent, but try to get a bit more rest."
    else:
        return "Great job! You're getting enough sleep."

# Optionally update the model with new data (retraining)
def update_model(new_X, new_y, filename="sleep_model.pkl"):
    model = LogisticRegression()
    model.fit(new_X, new_y)
    save_model(model, filename)
    return "Model updated with new data."

# Example of updating the model with new data
# update_model(np.array([[4], [5], [6], [7], [8], [9]]), np.array([0, 0, 1, 1, 1, 1]))
