
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))) # tenho duvidas se é a melhor forma, porem não sei se vão rodar esse teste no linux ou windows então fiz assim
from app.main import app
from fastapi.testclient import TestClient
client = TestClient(app)


def test_interval_awards_response_structure():
    response = client.get("/producers/interval-awards")
    assert response.status_code == 200

    data = response.json()

    assert "min" in data
    assert "max" in data

    for entry in data["min"] + data["max"]:
        assert "producer" in entry
        assert "interval" in entry
        assert "previousWin" in entry
        assert "followingWin" in entry

        assert isinstance(entry["producer"], str)
        assert isinstance(entry["interval"], int)
        assert isinstance(entry["previousWin"], int)
        assert isinstance(entry["followingWin"], int)
