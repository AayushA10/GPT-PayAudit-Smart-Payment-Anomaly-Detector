import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(filename: str):
    df = pd.read_csv(f"data/{filename}")

    if "Amount" not in df.columns:
        return {"error": "No 'Amount' column found."}

    model = IsolationForest(contamination=0.05)
    df["anomaly"] = model.fit_predict(df[["Amount"]])

    flagged = df[df["anomaly"] == -1]
    return flagged.to_dict(orient="records")
