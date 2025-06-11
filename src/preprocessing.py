import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def preprocess(df):
    df.rename(columns={"default payment next month": "default"}, inplace=True)
    X = df.drop(columns=["ID", "default"])
    y = df["default"]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return train_test_split(X_scaled, y, test_size=0.2, random_state=42)
