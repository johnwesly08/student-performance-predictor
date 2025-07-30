from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from joblib import dump
from src.data_loader import load_data
from src.preprocessing import preprocess_data

logging.basicConfig(level=logging.INFO)

def train_model(file_path):
    df = load_data(file_path)
    X_train, X_test, y_train, y_test = preprocess_data(df)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict.x_test
    logging.info(f"R2 score : {r2_score(y_test, y_pred)} MSE : {mean_sqaured_error(y_test, y_pred)}")
    dump(model, 'models/student_model.joblib')
    logging.info)