import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from main import app


client = TestClient(app)


@patch("routers.health.engine.connect")
def test_health_success(mock_engine_connect):
    """Test del endpoint /health cuando la conexión a la base de datos es exitosa."""
    # SImulate connections
    mock_connection = MagicMock()
    mock_connection.execute.return_value = None
    mock_engine_connect.return_value.__enter__.return_value = mock_connection

    response = client.get("/health")

    assert response.status_code == 200
    response_data = response.json()
    assert response_data["msg"] == "Connection successful."
    assert response_data["status"] == "ok"
