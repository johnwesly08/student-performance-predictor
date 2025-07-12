from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from joblib import dump
import logging

from src.data_loader import load_data
from src.preprocessing import preprocess_data

logging.basicConfig(level=logging.INFO)

def train_model():
    df = load_data("data/student_data.csv")
    X_train, X_test, y_train, y_test = preprocess_data(df)

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    logging.info(f"MAE: {mean_absolute_error(y_test, y_pred)}")
    logging.info(f"R² Score: {r2_score(y_test, y_pred)}")

    dump(model, "models/student_model.joblib")
    logging.info("Model saved at models/student_model.joblib")

if __name__ == "__main__":
    train_model()
