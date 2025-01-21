from jwt import encode, decode

from config.configuration import SECRET_KEY


def create_token(data: dict) -> str:
    """_summary_

    Args:
        data (dict): _description_

    Returns:
        str: _description_
    """
    print(f"data: {data}")
    token: str = encode(payload=data, key=SECRET_KEY, algorithm="HS256")
    return token


def validate_token(token: str) -> dict:
    """Function for validate token jwt.

    Args:
        token (str): token encript.

    Returns:
        dict: _description_
    """
    data: dict = decode(token, key=SECRET_KEY, algorithms=['HS256'])
    return data
