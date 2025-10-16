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
import numpy as np

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/run.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
logging.getLogger().addHandler(console_handler)

cfg = load_config()

def visualize_data(data_path):
    df = pd.read_csv(data_path)
    
    # Create subplots for each feature vs target
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    
    # Plot study_hours vs final_score
    if 'study_hours' in df.columns and 'final_score' in df.columns:
        axes[0].scatter(df['study_hours'], df['final_score'], color='blue', alpha=0.7)
        axes[0].set_title('Study Hours vs Final Score')
        axes[0].set_xlabel('Study Hours')
        axes[0].set_ylabel('Final Score')
        axes[0].grid(True)
    
    # Plot attendance vs final_score
    if 'attendance' in df.columns and 'final_score' in df.columns:
        axes[1].scatter(df['attendance'], df['final_score'], color='green', alpha=0.7)
        axes[1].set_title('Attendance vs Final Score')
        axes[1].set_xlabel('Attendance (%)')
        axes[1].set_ylabel('Final Score')
        axes[1].grid(True)
    
    plt.tight_layout()
    plt.show()

def visualize_regression(model_path, data_path):
    model = load(model_path)
    df = pd.read_csv(data_path)
    
    # Get the feature names the model was trained with
    if hasattr(model, 'feature_names_in_'):
        feature_names = model.feature_names_in_
        logging.info(f"Model expects features: {list(feature_names)}")
    else:
        # Assume the model was trained on study_hours and attendance
        feature_names = ['study_hours', 'attendance']
    
    # Check if all required features are present
    missing_features = set(feature_names) - set(df.columns)
    if missing_features:
        logging.error(f"Missing features in data: {missing_features}")
        logging.error("Cannot visualize regression - feature mismatch")
        return
    
    X = df[feature_names]
    y_col = "final_score" if "final_score" in df.columns else df.columns[-1]
    y = df[y_col]
    
    # Create predictions for the actual data points
    y_pred = model.predict(X)
    
    # Create subplots for each feature
    n_features = len(feature_names)
    fig, axes = plt.subplots(1, n_features, figsize=(5*n_features, 5))
    
    if n_features == 1:
        axes = [axes]  # Make it iterable
    
    for i, feature in enumerate(feature_names):
        # Sort by current feature for smooth lines
        sorted_indices = np.argsort(X[feature])
        x_sorted = X[feature].iloc[sorted_indices]
        y_actual_sorted = y.iloc[sorted_indices]
        y_pred_sorted = y_pred[sorted_indices]
        
        axes[i].scatter(x_sorted, y_actual_sorted, color='blue', alpha=0.7, label='Actual')
        axes[i].plot(x_sorted, y_pred_sorted, color='red', linewidth=2, label='Predicted')
        axes[i].set_title(f'Regression: {feature} vs {y_col}')
        axes[i].set_xlabel(feature)
        axes[i].set_ylabel(y_col)
        axes[i].legend()
        axes[i].grid(True)
    
    plt.tight_layout()
    plt.show()
    
    # Print model coefficients for interpretation
    if hasattr(model, 'coef_'):
        logging.info("Model coefficients:")
        for i, feature in enumerate(feature_names):
            logging.info(f"  {feature}: {model.coef_[i]:.4f}")
        logging.info(f"Intercept: {model.intercept_:.4f}")

def save_metrics(metrics: dict):
    os.makedirs("logs", exist_ok=True)
    metrics["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    metrics_file = "logs/training_metrics.csv"

    df = pd.DataFrame([metrics])
    if not os.path.exists(metrics_file):
        df.to_csv(metrics_file, index=False)
    else:
        df.to_csv(metrics_file, mode="a", header=False, index=False)

def main():
    parser = argparse.ArgumentParser(description="Student Marks Prediction ML Pipeline")
    parser.add_argument("--mode", required=True, choices=["train", "predict"], help="Select mode: train or predict")
    parser.add_argument("--file", help="Path to dataset (for training or prediction)")
    parser.add_argument("--plot", action="store_true", help="Enable visualization of data or regression line")
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

        r2 = r2_score(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        logging.info(f"R2 Score: {r2:.4f}")
        logging.info(f"MAE: {mae:.2f}")

        model_path = cfg["paths"]["model_path"]
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
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