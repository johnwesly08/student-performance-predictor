import pandas as pd
from joblib import load
import argparse

def predict_from_file(model_path: str, input_csv: str):
    model = load(model_path)
    df = pd.read_csv(input_csv)
    
    predictions = model.predict(df)
    df["predicted_score"] = predictions

    print(df[["predicted_score"]])
    return df

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=False, default="models/student_model.joblib")
    parser.add_argument("--input", required=True, help="Path to input CSV file")
    args = parser.parse_args()

    predict_from_file(args.model, args.input)
