
# Chat GPT API v1.0.0

- [Chat GPT API v1.0.0](#chat-gpt-api-v100)
  - [Introduction](#introduction)
  - [Create virtual environment](#create-virtual-environment)
  - [Prerequisites](#prerequisites)
  - [Unit Testing](#unit-testing)
  - [Create Environment Varibles.](#create-environment-varibles)
  - [Run Project](#run-project)
- [API Reference](#api-reference)
  - [Authentication](#authentication)
  - [Get Chat Messages By User](#get-chat-messages-by-user)
  - [Create Message](#create-message)
  - [Login](#login)
  - [Init User](#init-user)
  - [Health](#health)
  - [Schemas](#schemas)
    - [Properties](#properties)
    - [Properties](#properties-1)



## Introduction

This project implements a REST API developed with FastAPI and executed using Uvicorn. Its main functionality is the management of users with roles and the ability to ask questions related to occupational health topics. These questions are processed using the OpenAI Chat Completions API, which generates accurate and relevant answers.
The application uses a SQLite database, which is automatically initialized at system startup, facilitating a fast and hassle-free testing environment.


## Create virtual environment

Command to create virtual environment.

```bash
python3 -m venv .venv
```


## Prerequisites

Before starting the deployment, you must have the virtual environment installed, and install the following dependencies:

```bash
anyio==3.6.2
click==8.1.3
colorama==0.4.6
fastapi==0.85.2
greenlet==2.0.0
h11==0.14.0
idna==3.4
pydantic==1.10.2
PyJWT==2.6.0
sniffio==1.3.0
SQLAlchemy==1.4.42
starlette==0.20.4
typing_extensions==4.4.0
uvicorn==0.19.0
sqlmodel==0.0.11
tortoise-orm==0.23.0
python-dotenv==1.0.0
passlib[bcrypt]==1.7.4
openai==0.28.1
pytest==8.3.4
httpx==0.28.1
coverage==7.6.10
```

For installation you can also run the following command:

```bash
pip install -r requirements.txt
```

## Unit Testing

To run unit tests the following libraries are required:

- pytest
- coverage

To run unit tests follow the following commands within the virtual environment:

```bash
# Validar Pruebas unitarias con pytest
coverage run -m pytest -v
# Generar reporte de pytest
coverage report -m
# Generar xml coverage con el reporte
coverage xml
```

## Create Environment Varibles.

For correct operation, the following environment variables must be created:

```bash
SECRET_KEY: Secret for hashing passwords.

PWD_ADMIN: Password for user admin.

OPENAI_API_KEY: Api key for connect OpenAI API.
```

## Run Project

Command to run the project within the virtual environment:
```bash
uvicorn main:app --reload --port 5000
```

# API Reference

## Authentication

- HTTP Authentication, scheme: bearer 

<h1 id="chat-gpt-api-messages">messages</h1>

## Get Chat Messages By User

<a id="opIdget_chat_messages_by_user_chat_messages_history__username__get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.get('/chat_messages/history/{username}', headers = headers)

print(r.json())

```

`GET /chat_messages/history/{username}`

Endpoint for get messages's user.

<h3 id="get-chat-messages-by-user-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|username|path|string|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="get-chat-messages-by-user-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="get-chat-messages-by-user-responseschema">Response Schema</h3>

Status Code **200**

*Response Get Chat Messages By User Chat Messages History  Username  Get*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
JWTBearer
</aside>

## Create Message

<a id="opIdcreate_message_chat_messages_ask_post"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('/chat_messages/ask', params={
  'username': 'string',  'message': 'string'
}, headers = headers)

print(r.json())

```

`POST /chat_messages/ask`

Endpoint for create and save message.

<h3 id="create-message-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|username|query|string|true|none|
|message|query|string|true|none|

> Example responses

> 201 Response

```json
{}
```

<h3 id="create-message-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="create-message-responseschema">Response Schema</h3>

Status Code **201**

*Response Create Message Chat Messages Ask Post*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
JWTBearer
</aside>

<h1 id="chat-gpt-api-auth">auth</h1>

## Login

<a id="opIdlogin_login_post"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/login', headers = headers)

print(r.json())

```

`POST /login`

Start session with user.

> Body parameter

```json
{
  "username": "Chat gpt saludo.",
  "password": "Chat gpt saludo."
}
```

<h3 id="login-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[User](#schemauser)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="login-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="login-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## Init User

<a id="opIdinit_user_init_user_post"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/init_user', headers = headers)

print(r.json())

```

`POST /init_user`

Register new user in database.

> Body parameter

```json
{
  "username": "Chat gpt saludo.",
  "password": "Chat gpt saludo."
}
```

<h3 id="init-user-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[User](#schemauser)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="init-user-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="init-user-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="chat-gpt-api-health">health</h1>

## Health

<a id="opIdhealth_health_get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/health', headers = headers)

print(r.json())

```

`GET /health`

Validates service status and connection to database.

> Example responses

> 200 Response

```json
null
```

<h3 id="health-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="health-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## Schemas

<h2 id="tocS_HTTPValidationError">HTTPValidationError</h2>
<!-- backwards compatibility -->
<a id="schemahttpvalidationerror"></a>
<a id="schema_HTTPValidationError"></a>
<a id="tocShttpvalidationerror"></a>
<a id="tocshttpvalidationerror"></a>

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

```

HTTPValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|[[ValidationError](#schemavalidationerror)]|false|none|none|

<h2 id="tocS_User">User</h2>
<!-- backwards compatibility -->
<a id="schemauser"></a>
<a id="schema_User"></a>
<a id="tocSuser"></a>
<a id="tocsuser"></a>

```json
{
  "username": "Chat gpt saludo.",
  "password": "Chat gpt saludo."
}

```

User

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|false|none|none|
|username|string|true|none|none|
|password|string|true|none|none|
|rol_id|integer|false|none|none|

<h2 id="tocS_ValidationError">ValidationError</h2>
<!-- backwards compatibility -->
<a id="schemavalidationerror"></a>
<a id="schema_ValidationError"></a>
<a id="tocSvalidationerror"></a>
<a id="tocsvalidationerror"></a>

```json
{
  "loc": [
    "string"
  ],
  "msg": "string",
  "type": "string"
}

```
