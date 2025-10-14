import pandas as pd
from joblib import load
from src.utils.config_loader import load_config
import argparse
import logging

logging.basicConfig(level = logging.INFO)
cfg = load_config()
  
def predict_from_file(input_file: str, model_path: str = None):
    if model_path is None:
        model_path = cfg["paths"]["model_path"]

    logging.info(f"Loading trained model from {model_path}...")
    model = load(model_path)

    logging.info(f"Loading input data from {input_file}...")
    df = pd.read_csv(input_file)
    
    logging.info("Running predictions...")
    predictions = model.predict(df)


    df["predicted_score"] = predictions
    logging.info("Prediction completed successfully")

    print(df)
    output_path = "data/processed/predicted_output.csv"
    df.to_csv(output_path, index=False)
    logging.info(f"Predictions saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to input CSV file")
    args = parser.parse_args()

    predict_from_file(args.input)
