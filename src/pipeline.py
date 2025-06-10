import pandas as pd
from src.preprocessing import preprocess
from src.train import train_model
from src.evaluate import evaluate_model

def run_pipeline():
    data = pd.read_csv("data/default_of_credit_card_clients.csv", skiprows=1)
    X_train, X_test, y_train, y_test = preprocess(data)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)
