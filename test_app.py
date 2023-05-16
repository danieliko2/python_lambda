from app2 import app

tester = app.test_client()

def test_app():
    response = tester.get('/')
    assert response.status_code == 200
