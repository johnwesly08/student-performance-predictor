import pandas as pd
from sklearn.model_selection import train_test_split

def preprocess_data(df):
    # Handle missing
    df = df.dropna()
    
    # Feature/Target split
    X = df.drop("final_score", axis=1)
    y = df["final_score"]
    
    return train_test_split(X, y, test_size=0.2, random_state=42)
