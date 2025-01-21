import openai
from config.configuration import OPENAI_API_KEY


openai.api_key = OPENAI_API_KEY


def openai_chat_message(message: str) -> str:
    """Function for send request to openai chat completions."""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=2000,
        temperature=0.3,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant expert in occupational risk assessment. Answer the questions in the user's language. Only answer questions related to the topic. Avoid answering questions on topics other than occupational hazards."
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )
    # Extraer la respuesta del asistente
    return response['choices'][0]['message']['content'] # type: ignore
