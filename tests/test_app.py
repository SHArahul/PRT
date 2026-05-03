# tests/test_app.py

from FlaskService import app


def setup_module(module):
    """
    Configure Flask app for testing mode.
    """
    app.config['TESTING'] = True


def test_home():
    """
    Test root endpoint (/)
    Ensures:
    - Status code is 200
    - Correct response message
    """
    with app.test_client() as client:
        response = client.get('/')

        assert response.status_code == 200
        assert b"Flask deployment service is running!" in response.data


def test_health():
    """
    Test health endpoint (/health)
    Ensures:
    - Status code is 200
    - JSON response contains healthy status
    """
    with app.test_client() as client:
        response = client.get('/health')

        assert response.status_code == 200
        json_data = response.get_json()

        assert json_data is not None
        assert json_data["status"] == "healthy"


def test_invalid_route():
    """
    Test unknown endpoint
    Ensures:
    - Status code is 404
    """
    with app.test_client() as client:
        response = client.get('/invalid-route')

        assert response.status_code == 404