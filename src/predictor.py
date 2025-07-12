import pandas as pd
from joblib import load
import sys

def predict(input_file):
    model = load("models/student_model.joblib")
    df = pd.read_csv(input_file)
    preds = model.predict(df)
    df["Predicted_Score"] = preds
    print(df)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to input CSV file")
    args = parser.parse_args()
    predict(args.input)
