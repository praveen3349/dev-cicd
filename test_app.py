from app import app

def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200

def test_status():
    response = app.test_client().get('/status')
    assert response.status_code == 200

