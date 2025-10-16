import argparse
from src.utils.config_loader import load_config
import logging
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime
from joblib import load
from src.model import train_and_save_model
from src.predictor import predict_from_file


os.makedirs("logs",exist_ok=True)

logging.basicConfig(
    filename = "logs/run.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
logging.getLogger().addHandler(console_handler)

cfg = load_config()

def visualize_data(data_path):
    df = pd.read_csv(data_path)
    x_col = "Hours" if "Hours" in df.columns else df.columns[0]
    y_col = "Scores" if "Scores" in df.columns else df.columns[-1]

    plt.figure(figsize = (8,5))
    plt.scatter(df[x_col],df[y_col], color = "blue", label = "Actual data")
    plt.title(f"{x_col} vs {y_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True)
    plt.show()


def visualize_regression(model_path, data_path):
    try:
        model = load(model_path)
        df = pd.read_csv(data_path)
        
        print(f"🔍 Data features: {df.columns.tolist()}")
        
        # Get the feature names the model was trained with
        if hasattr(model, 'feature_names_in_'):
            expected_features = model.feature_names_in_
        else:
            # If model doesn't have feature names, use common ones
            expected_features = ['study_hours', 'attendance']
        
        print(f"Model expects: {expected_features}")
        
        # Check if all expected features are present
        missing_features = set(expected_features) - set(df.columns)
        if missing_features:
            print(f"Missing features: {missing_features}")
            print("Available features:", df.columns.tolist())
            
            # Try to use only available features
            available_features = [f for f in expected_features if f in df.columns]
            if not available_features:
                print("No common features found. Cannot visualize.")
                return
            
            print(f"Using available features: {available_features}")
            X = df[available_features]
            x_col = available_features[0]
        else:
            X = df[expected_features]
            x_col = expected_features[0]
        
        y_col = "final_score" if "final_score" in df.columns else df.columns[-1]
        
        if y_col not in df.columns:
            print(f"Target column '{y_col}' not found in data")
            return
        
        y = df[y_col]
        
        # Sort for smooth plotting
        X_sorted = X.sort_values(by=x_col)
        line = model.predict(X_sorted)
        
        # Create visualization
        plt.figure(figsize=(10, 6))
        plt.scatter(X[x_col], y, color='blue', alpha=0.7, label='Actual Data')
        plt.plot(X_sorted[x_col], line, color='red', linewidth=2, label='Regression Line')
        plt.title(f'Regression: {x_col} vs {y_col}')
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
        
        print("Visualization completed successfully")
        
    except Exception as e:
        print(f"Visualization failed: {str(e)}")
        logging.error(f"Visualization error: {str(e)}")

def save_metrics(metrics: dict):
    os.makedirs("logs", exist_ok=True)
    metrics["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    metrics_file = "logs/training_metrics.csv"

    df = pd.DataFrame([metrics])
    if not os.path.exists(metrics_file):
        df.to_csv(metrics_file, index=False)
    else:
        df.to_csv(metrics_file, mode="a", header=False, index =False)


def debug_data_issue():
    train_path = cfg["paths"]["raw_data"]
    if os.path.exists(train_path):
        train_df = pd.read_csv(train_path)
        print(f"Training data features: {train_df.columns.tolist()}")
        print(f"Training data shape: {train_df.shape}")
        print(f"Dirst few rows: {train_df.head()}")

    model_path = cfg["paths"]["model_path"]
    if os.path.exists(model_path):
        model = load(model_path)
        if hasattr(model, 'feature_names_in_'):
            print(f"Model expects features: {model.feature_names_in_}")
        else:
            print("Model has no feature names stored")


def main():
    parser = argparse.ArgumentParser(description="Student Marks Prediction ML Pipeline")
    parser.add_argument("--mode", required = True, choices = ["train", "predict"], help = "Select mode: train or predict")
    parser.add_argument("--file", help="Path to dataset (for training or prediction)")
    parser.add_argument("--plot", action = "store_true", help = "Enable visualization of data or regression line")
    args = parser.parse_args()

    if args.mode == "train":
        data_path = args.file if args.file else cfg["paths"]["raw_data"]
        logging.info("Starting training pipeline...")

        if args.plot:
            visualize_data(data_path)
        
        from sklearn.metrics import mean_absolute_error, r2_score
        from src.data_loader import load_data
        from src.preprocessing import preprocess_data
        from sklearn.linear_model import LinearRegression
        from joblib import dump

        df = load_data(data_path)
        X_train, X_test, y_train, y_test = preprocess_data(df)
        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        r2 = r2_score(y_test,y_pred)
        mae = mean_absolute_error(y_test,y_pred)
        logging.info(f"R2 Score: {r2:.4f}")
        logging.info(f" MAE: {mae:.2f}")

        model_path =  cfg["paths"]["model_path"]
        os.makedirs(os.path.dirname(model_path), exist_ok = True)
        dump(model, model_path)
        logging.info(f"Model saved to {model_path}")

        save_metrics({"r2 score": r2, "mae": mae})

        if args.plot:
            visualize_regression(model_path, data_path)

        logging.info("Training completed successfully")

    elif args.mode == "predict":
        input_path = args.file if args.file else cfg["paths"]["test_data"]
        logging.info("Starting prediction pipeline...")
        predict_from_file(input_path)
        logging.info("Prediction completed successfully")

if __name__ == "__main__":
    main()