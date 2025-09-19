import pandas as pd
from sklearn.model_selection import train_test_split

def preprocess_data(df: pd.DataFrame):
    """Cleans Data and splits into trains/test."""
    df = df.dropna()

    x = df.drop("final_score",axis=1)
    y = df["final_score"]

    X_train, X_test, y_train, y_test = train_test_split(
        x,y, test_size=0.2, random_state=42
    )

    return X_train,X_test,y_train,y_test
