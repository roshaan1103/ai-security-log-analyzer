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