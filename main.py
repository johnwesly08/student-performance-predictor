import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

#Loading the required data

data = {
    "Hours" : [1.0,2.0,3.5,5.0,7.5],
    "Scores" : [35,50,75,82,95]
}
df = pd.DataFrame(data)

# Visualizing the data

plt.figure(figsize=(8,5))
plt.scatter(df["Hours"],df["Scores"],color='blue',label="Actual Data")
plt.title("Study Hours Vs Score")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.grid(True)
plt.legend()
plt.show()


# Split Data
X = df[["Hours"]]
y = df[["Scores"]]

# Train the model

model = LinearRegression()
model.fit(X,y)

#Predict the model

hours_to_predict = [[4.0]]
predicted_score =model.predict(hours_to_predict)
print(f" Prediction: If a student studies for a {hours_to_predict[0][0]} hours, they may score: {predicted_score[0]:.2f}")

#Visualize the Regression line

line = model.coef_ * X + model.intercept_
plt.scatter(X,y, color = 'green', label = "Training Data")
plt.plot(X,line, color = 'red', label="Regression Line")
plt.title("Linear Regression Fit")
plt.xlabel("Hours Studied")
plt.ylabel("Scores")
plt.legend()
plt.show()

#Evaluate the model
y_pred = model.predict()
mse = mean_squared_error(y,y_pred)
r2 = r2_score(y,y_pred)

print(f"Mean Square Error: {mse:.2f}")
print(f"R2 Score: {r2:.2f}")

#Save the model

joblib.model(model, "Student_score_predictor.pkl")
print("Model saved as the Student_score_predictor.pkl")