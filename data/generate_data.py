import pandas as pd
import os

def generate_datasets():
    # Ensure data directories exist
    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)

    # Mock training dataset (raw)
    train_data = {
        "study_hours": [5, 8, 2, 7, 10, 4, 6, 9, 3, 1],
        "attendance": [80, 90, 60, 85, 95, 75, 82, 92, 70, 50],
        "final_score": [75, 88, 50, 82, 92, 68, 73, 89, 55, 40],
    }
    train_df = pd.DataFrame(train_data)
    train_df.to_csv("data/raw/student_data.csv", index=False)

    # Test input dataset (no target column)
    test_data = {
        "study_hours": [6, 9, 3, 8],
        "attendance": [80, 92, 70, 88],
    }
    test_df = pd.DataFrame(test_data)
    test_df.to_csv("data/raw/student_test_input.csv", index=False)

    print("✅ Raw datasets created: data/raw/student_data.csv & data/raw/student_test_input.csv")

if __name__ == "__main__":
    generate_datasets()
