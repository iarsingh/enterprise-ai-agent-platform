from fastapi.testclient import TestClient
from entagent.main import app

client = TestClient(app)


def test_lists_and_refuses_apply():
    assert "confluence.search" in client.get("/tools").json()["tools"]
    ok = client.post("/call", json={"name": "confluence.search", "arguments": {"q": "status"}}).json()
    assert ok["ok"] is True
    assert ok["applied"] is False
    refused = client.post("/call", json={"name": "jira.get", "arguments": {"cmd": "kubectl apply"}}).json()
    assert refused["ok"] is False
