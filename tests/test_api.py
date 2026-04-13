from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "AI Security Log Analyzer Running"}


def test_analyze_log():
    sample_log = """
    Failed password for invalid user admin from 192.168.1.10 port 22 ssh2
    Failed password for root from 192.168.1.10 port 22 ssh2
    """

    response = client.post(
        "/analyze-log",
        files={"file": ("test.log", sample_log)}
    )

    assert response.status_code == 200
    assert "results" in response.json()