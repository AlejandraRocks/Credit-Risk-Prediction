# Credit Risk Prediction API

This project provides a complete pipeline for training a credit risk prediction model and exposing it via a REST API using FastAPI.

## 🧠 What it does

- Trains a `RandomForestClassifier` to predict credit default based on customer features.
- Evaluates the model and saves it with `joblib`.
- Exposes a prediction endpoint `/predict` using FastAPI.
- Includes preprocessing and evaluation modules for modular reuse.

---

## 📁 Project structure

```
Credit-Risk-Prediction/
├── data/
│   └── default_of_credit_card_clients.csv
├── models/
│   ├── rf_model.joblib
│   └── scaler.joblib
├── src/
│   ├── main.py
│   ├── pipeline.py
│   ├── train.py
│   ├── preprocessing.py
│   └── evaluate.py
├── venv/
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup instructions

### 1. Clone the repository

```bash
git clone https://github.com/tu_usuario/Credit-Risk-Prediction.git
cd Credit-Risk-Prediction
```

### 2. Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install --break-system-packages -r requirements.txt
```

---

## 🚀 Train the model

Run the pipeline to preprocess data, train the model, and save artifacts:

```bash
python3 src/pipeline.py
```

This will generate:

- `models/rf_model.joblib`
- `models/scaler.joblib`

---

## 🌐 Run the FastAPI server

Start the API with:

```bash
uvicorn src.main2:app --reload
```

Then visit:

- Interactive docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- JSON schema: [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)

---

## 📥 Example JSON input for `/predict`

```json
{
  "LIMIT_BAL": 20000,
  "SEX": 2,
  "EDUCATION": 2,
  "MARRIAGE": 1,
  "AGE": 24,
  "PAY_0": 2,
  "PAY_2": 2,
  "PAY_3": -1,
  "PAY_4": -1,
  "PAY_5": -2,
  "PAY_6": -2,
  "BILL_AMT1": 3913,
  "BILL_AMT2": 3102,
  "BILL_AMT3": 689,
  "BILL_AMT4": 0,
  "BILL_AMT5": 0,
  "BILL_AMT6": 0,
  "PAY_AMT1": 0,
  "PAY_AMT2": 689,
  "PAY_AMT3": 0,
  "PAY_AMT4": 0,
  "PAY_AMT5": 0,
  "PAY_AMT6": 0
}
```

The response will be:

```json
{
  "default_prediction": 0
}
```

---

## 📌 Notes

- The dataset comes from [UCI Credit Card Default dataset](https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients).
- The model uses `StandardScaler` for preprocessing.
- Only 24 features are used in the prediction schema.

---

## 👩‍💻 Author

Alejandra Vesga-Ramírez  
[LinkedIn](https://www.linkedin.com/in/alejandravesgaramirez)

---

## 📝 License

MIT License. See `LICENSE` file for details.
