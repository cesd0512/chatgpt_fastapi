import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from main import app
from schemas.chat_message import ChatMessage as ChatMessageSchema
from services.chat_message import ChatMessageService
from services.user import UserService
from utils.openai_conn import openai_chat_message

client = TestClient(app)


@pytest.fixture
def test_user():
    """Usuario de prueba."""
    return {
        "username": "test_user",
        "id": 1
    }


@pytest.fixture
def test_message():
    """Mensaje de prueba."""
    return "Hola, ¿cómo estás?"


@pytest.fixture
def test_response_openai():
    """Respuesta simulada de OpenAI."""
    return "Estoy bien, gracias por preguntar."


@patch("routers.chat_message.Session")
@patch("routers.chat_message.ChatMessageService")
def test_get_messages_by_user(mock_chat_message_service, mock_session, test_user):
    """Test del endpoint GET /chat_messages/history/{username}."""
    mock_service_instance = MagicMock()
    mock_service_instance.get_messages_by_user.return_value = [
        {"id": "1", "message": "Hola", "response": "Hola, ¿en qué puedo ayudarte?", "user_id": 1}
    ]
    mock_chat_message_service.return_value = mock_service_instance

    client.get(f"/chat_messages/history/{test_user['username']}")


@patch("routers.chat_message.Session")
@patch("routers.chat_message.openai_chat_message")
@patch("routers.chat_message.UserService")
@patch("routers.chat_message.ChatMessageService")
def test_create_message(mock_chat_message_service, mock_user_service, mock_openai_chat_message, mock_session, test_user, test_message, test_response_openai):
    """Test del endpoint POST /chat_messages/ask."""
    mock_user_service_instance = MagicMock()
    mock_user_service_instance.get_user.return_value = MagicMock(id=test_user["id"])
    mock_user_service.return_value = mock_user_service_instance

    # SImulate response openai
    mock_openai_chat_message.return_value = test_response_openai

    #Simulate create message
    mock_chat_message_service_instance = MagicMock()
    mock_chat_message_service_instance.create_message.return_value = "unique_message_id"
    mock_chat_message_service.return_value = mock_chat_message_service_instance

    client.post(
        "/chat_messages/ask",
        json={"username": test_user["username"], "message": test_message},
    )

