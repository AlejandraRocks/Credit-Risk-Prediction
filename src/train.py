# 1. Importar librerías
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib

# Cargar el archivo con separador ; y saltar la primera fila
df = pd.read_csv("../data/default_of_credit_card_clients.csv", sep=";", header=1)
df.rename(columns={"default payment next month": "default"}, inplace=True)

# 3. Separar features y target
X = df.drop(columns=["ID", "default"])
y = df["default"]

# 4. Dividir en entrenamiento y testeo
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Escalar los datos
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 6. Entrenar el modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# 7. Evaluar el modelo
y_pred = model.predict(X_test_scaled)
print("Matriz de Confusión:")
print(confusion_matrix(y_test, y_pred))
print("\nReporte de Clasificación:")
print(classification_report(y_test, y_pred))
import os
import joblib

# Crear ruta al directorio 'models' desde la ubicación del script
models_dir = os.path.join(os.path.dirname(__file__), '..', 'models')

# Crear el directorio si no existe
os.makedirs(models_dir, exist_ok=True)

# Guardar modelo y scaler
joblib.dump(model, os.path.join(models_dir, 'rf_model.joblib'))
joblib.dump(scaler, os.path.join(models_dir, 'scaler.joblib'))
