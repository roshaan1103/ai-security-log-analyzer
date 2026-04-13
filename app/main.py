from fastapi import FastAPI, UploadFile
from app.parser import parse_log
from app.features import extract_features
from app.model import load_model
from app.detector import analyze

app = FastAPI()

model = load_model()

@app.get("/")
def home():
    return {"message": "AI Security Log Analyzer Running"}

@app.post("/analyze-log")
async def analyze_log(file: UploadFile):
    content = await file.read()
    lines = content.decode().split("\n")

    parsed = [parse_log(line) for line in lines if parse_log(line)]
    features = extract_features(parsed)

    results = analyze(features, model)

    return {"results": results}

@app.get("/summary")
def summary():
    return {
        "message": "System ready for threat detection",
        "supported_attacks": [
            "Brute Force (T1110)",
            "Credential Stuffing (T1110.004)",
            "Anomalous Behavior (T1036)"
        ]
    }