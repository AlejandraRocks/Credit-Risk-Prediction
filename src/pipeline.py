import sys
import os
import pandas as pd

import os
import sys

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)

from src.preprocessing import preprocess
from src.train import train_model
from src.evaluate import evaluate_model


def run_pipeline():
    data_path = os.path.join(project_root, 'data', 'default_of_credit_card_clients.csv')
    data = pd.read_csv(data_path, sep=";", skiprows=1)

    X_train, X_test, y_train, y_test = preprocess(data)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    run_pipeline()

