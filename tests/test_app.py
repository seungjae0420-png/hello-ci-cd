from app.app import create_app
def test_health_ok():
    app = create_app()
    client = app.test_client()
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json.get("status") == "ok"
def test_index_ok():
    app = create_app()
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    assert b"Hello CI!" in res.data
