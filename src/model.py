from src.data_loader import load_data
from src.preprocessing import preprocess_data
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from joblib import dump
import logging
import argparse


logging.basicConfig(level=logging.INFO)

def train_and_save_model(data_path: str, model_path:str = "models/student_model.joblib"):
    df = load_data(data_path)
    X_train, X_test, y_train, y_test = preprocess_data(df)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    logging.info(f"R² Score: {r2_score(y_test, y_pred):.4f}")
    logging.info(f"MAE: {mean_absolute_error(y_test, y_pred):.2f}")

    dump(model, model_path)
    logging.info(f"Model saved to {model_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="Path to training CSV file")
    args = parser.parse_args()

    train_and_save_model(args.file)    
    