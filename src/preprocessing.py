import pandas as pd
from sklearn.model_selection import train_test_split
def preprocess_data(df: pd.DataFrame):
    df = df.dropna()

    X = df.drop(columns=['final_score'])
    y = df['final_score']
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state = 42)
    return X_train, X_test, y_train, y_test
