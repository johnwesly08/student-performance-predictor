import pandas as pd
import os
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

    if hasattr(model, 'feature_names_in_)'):
        feature_names = model.feature_names_in_
    else:
        feature_names = ['study_hours', 'attendance']
    
    logging.info(f"Model expects features: {list(feature_names)}")
    logging.info(f"Data columns: {df.columns.tolist()}")

    missing_features = set(feature_names) - set(df.columns)
    if missing_features:
        raise ValueError(f"Missing features in input data: {missing_features}")
    
    X = df[feature_names]
    logging.info(f"Using features for prediciton: {X.columns.tolist()}")

    logging.info("Running predictions...")
    predictions = model.predict(X)


    df["predicted_score"] = predictions.round(2)
    logging.info("Prediction completed successfully")
    
    if 'final_score' in df.columns:
        from sklearn.metrics import mean_absolute_error, r2_score
        actual_scores = df['final_score']
        mae = mean_absolute_error(actual_scores, predictions)
        r2 = r2_score(actual_scores, predictions)

        logging.info(f"Model Performance: ")
        logging.info(f"R2 score: {r2:.4f}")
        logging.info(f"MAE: {mae:.2f}")

        df['prediction_error'] = (df["final_score"] - df['predicted_score']).round(2)

    print("\n" + "="*50)
    print("PREDICTION RESULTS")
    print("="*50)

    display_cols = ['study_hours', 'attendance', 'predicted_score']
    if 'final_score' in df.columns:
        display_cols.extend(['final_score', 'prediction_error'])
    
    print(df[display_cols].to_string(index=False))

    if 'final_score' in df.columns:
        print(f"\nModel Performance: ")
        print(f"R2 Score: {r2:.4f}")
        print(f"MAE: {mae:.2f}")

    print("="*50)
    output_path = "data/processed/predicted_output.csv"
    os.makedirs(os.path.dirname(output_path),exist_ok=True)
    df.to_csv(output_path, index=False)
    logging.info(f"Predictions saved to {output_path}")

    return df

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to input CSV file")
    args = parser.parse_args()

    predict_from_file(args.input)
