from sklearn.ensemble import IsolationForest
import joblib

def train_model(data):
    model = IsolationForest(contamination=0.1)
    model.fit(data)
    joblib.dump(model, "models/model.pkl")
    return model

def load_model():
    return joblib.load("models/model.pkl")