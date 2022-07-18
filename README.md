# Documentação da API

## Tabela de Conteúdos

- [1. Visão Geral](#1-visão-geral)
- [2. Diagrama ER](#2-diagrama-er)
- [3. Configuração inicial](#3-configuração-inicial)
  - [3.1 Instalando Dependências](#31-instalando-dependências)
  - [3.2 Entrando na variavel de ambiente](#32-entrando-na-variavel-de-ambiente)
  - [3.3 Subindo banco com docker](#33-subindo-banco-com-docker)
  - [3.4 Executando as migrações](#34-executando-as-migrações)
  - [3.5 Iniciando o servidor](#35-iniciando-o-servidor)
- [4. Autenticação](#4-autenticação)
- [5. Endpoints](#5-endpoints)
  - [Índice](#índice)
  - [1. Users](#1-users)
      - [Endpoints](#endpoints)
      - [1.1 Criação de usuário](#11-criação-de-usuário)
      - [1.2 Login de usuário](#12-login-de-usuário)
      - [1.3 Listagem de Usuários](#13-listagem-de-usuários)
      - [1.4 Listando usuário por ID](#14-listando-usuário-por-id)
      - [1.5 Listando usuários mais recentes por quantia](#15-listando-usuários-mais-recentes-por-quantia)

## 1. Visão Geral

Visão geral do projeto, um pouco sobre das tecnologias usadas.

A URL base da aplicação:
https://rent-play.herokuapp.com/

## 2. Diagrama ER

[ Voltar ao topo ](#tabela-de-conteúdos)

Diagrama ER da API definindo bem as relações entre as tabelas do banco de dados.

![DER](DER%20Capstone%20M5.svg)

## 3. Configuração inicial

[ Voltar ao topo ](#tabela-de-conteúdos)

### 3.1 Instalando Dependências

Execute o seguinte comando para instalar as dependências do projeto

```shell
$ pip install -r requirements.txt
```

### 3.2 Entrando na variavel de ambiente

Em seguida entre nas variáveis de ambiente

```powershell
$ source venv/bin/activate
```

### 3.3 Subindo banco com docker

```powershell
$ docker-compose up -d
```

### 3.4 Executando as migrações

Execute as migrações

```powershell
$ python manage.py migrate
```

### 3.5 Iniciando o servidor

Por fim, inicie o servidor

```powershell
$ python manage.py runserver
```

## 4. Autenticação

[ Voltar ao topo ](#tabela-de-conteúdos)

Autenticação deve ser feita pelo usuário ao inserir os dados exigidos do arquivo .env.example.

## 5. Endpoints

[ Voltar ao topo ](#tabela-de-conteúdos)

### Índice

-   [Users](#1-users)
    -   [POST api/users/](#11-criação-de-usuário)
    -   [POST api/login/](#12-login-de-usuário)
    -   [GET api/users/](#13-listagem-de-usuários)
    -   [GET api/users/<user_id>/](#14-listando-usuário-por-id)
    -   [GET api/users/newest/<by_quantity>/](#15-listando-usuários-mais-recentes-por-quantia)

## 1. Users

[Voltar aos endpoints](#5-endpoints)

O objeto user é definido como:

| Campo      | Tipo          | Descrição                      |
| ---------- | ------------- | ------------------------------ |
| id         | UUID          | Identificador único do usuário |
| nickname   | string        | Apelido do usuário             |
| first_name | string        | Primeiro nome do usuário       |
| last_name  | string        | Último nome do usuário         |
| cellphone  | sting         | Telefone único do usuário      |
| email      | string        | Email único do usuário         |
| password   | hashed string | Senha do usuário               |
| wallet     | decimal       | Valor na carteira do usuário   |

### Endpoints

| Método | Rota                             | Descrição                                               |
| ------ | -------------------------------- | ------------------------------------------------------- |
| POST   | /api/users/                      | Rota para criação de usuário                            |
| POST   | /api/login/                      | Rota para login de Usuário                              |
| GET    | /api/users/                      | Lista todos usuários                                    |
| GET    | /api/users/<user_id>/            | Lista um usuário especifico por id                      |
| GET    | /api/users/newest/<by_quantity>/ | Lista os usuários cadastardos mais recentes por quantia |

---

### 1.1 Criação de usuário

[Voltar aos endpoints](#5-endpoints)

### `/api/users/`

### Exemplo de request

```
POST /api/users
Host: https://rent-play.herokuapp.com/
Authorization: None
Content-type: application/json
```

### Corpo da requisição

```json
{
    "nickname": "Woozie",
    "first_name": "Wellery",
    "last_name": "Chaves",
    "cellphone": "12345678910",
    "email": "wellery@email.com",
    "password": "1234"
}
```

### Exemplo de Response

```
201 Created
```

```json
{
    "id": "8a1fd575-0bc3-4197-ae7d-542bc655fe3b",
    "nickname": "Woozie",
    "first_name": "Wellery",
    "last_name": "Chaves",
    "cellphone": "12345678910",
    "email": "wellery@email.com",
    "wallet": "0.00"
}
```

### Possíveis erros:

| Código do erro  | Descrição                                |
| --------------- | ---------------------------------------- |
| Already exists  |
| 400 Bad Request | user with this nickname already exists.  |
| 400 Bad Request | user with this cellphone already exists. |
| 400 Bad Request | user with this email already exists.     |
| Missing Keys    |
| 400 Bad Request | "This field is required."                |

---

## 1.2 Login de usuário

[Voltar aos endpoints](#5-endpoints)

### `/api/login/`

### Exemplo de request

```
POST /api/login
Host: https://rent-play.herokuapp.com/
Authorization: None
Content-type: application/json
```

### Corpo da requisição

```json
{
    "email": "guilherme@email.com",
    "password": "1234"
}
```

### Exemplo de Response

```
200 OK
```

```json
{
    "token": "2b522ff35792ec048c3d7a0c8541a0c57a9f982b",
    "user": {
        "id": "c18ad943-a672-40c5-968a-5099611b3505",
        "nickname": "guilherme",
        "first_name": "Guilherme",
        "last_name": "Preveda",
        "cellphone": "12345678910",
        "email": "guilherme@email.com",
        "wallet": "0.00"
    }
}
```

### Possíveis erros:

| Código do erro   | Descrição                    |
| ---------------- | ---------------------------- |
| 401 Unauthorized | invalid username or password |
| 400 Bad Request  | "This field is required."    |

---

### 1.3 Listagem de Usuários

[Voltar aos endpoints](#5-endpoints)

### `api/users/`

Exemplo de Request:

```
GET api/users/
Host: https://rent-play.herokuapp.com/
Authorization: None
Content-Type: application/json
```

Corpo da Requisição:

```
Vazio
```

Exemplo de response:

```
200 OK
```

```json
{
    {
	"count": 2,
	"next": null,
	"previous": null,
	"results": [
		{
			"id": "8a1fd575-0bc3-4197-ae7d-542bc655fe3b",
			"nickname": "Woozie",
			"first_name": "Wellery",
			"last_name": "Chaves",
			"cellphone": "09876543211",
			"email": "wellery@email.com",
			"wallet": "0.00"
		},
		{
			"id": "c18ad943-a672-40c5-968a-5099611b3505",
			"nickname": "guilherme",
			"first_name": "Guilherme",
			"last_name": "Preveda",
			"cellphone": "12345678910",
			"email": "guilherme@email.com",
			"wallet": "0.00"
		}
	]
}
}
```

## Possíveis Erros:

Nenhum, o máximo que pode acontecer é retornar uma lista vazia.

---

### 1.4 Listando usuário por ID

[Voltar aos endpoints](#5-endpoints)

### `api/users/<user_id>/`

Exemplo de Request:

```
GET api/users/c18ad943-a672-40c5-968a-5099611b3505/
Host: https://rent-play.herokuapp.com/
Authorization: Token
Content-Type: application/json
```

Corpo da Requisição:

```
Vazio
```

Exemplo de response:

```
200 OK
```

```json
{
    "id": "c18ad943-a672-40c5-968a-5099611b3505",
    "nickname": "guilherme",
    "first_name": "Guilherme",
    "last_name": "Preveda",
    "cellphone": "12345678910",
    "email": "guilherme@email.com",
    "wallet": "0.00"
}
```

## Possíveis Erros:

| Código do erro   | Descrição     |
| ---------------- | ------------- |
| 404 Not Found    | Not Found     |
| 401 Unauthorized | Invalid Token |
| 401 Unauthorized | Missing Token |

---

### 1.5 Listando usuários mais recentes por quantia

[Voltar aos endpoints](#5-endpoints)

### `/api/users/newest/<by_quantity>/`

Exemplo de Request:

```
GET /api/users/newest/1/
Host: https://rent-play.herokuapp.com/
Authorization: Token
Content-Type: application/json
```

Corpo da Requisição:

```
Vazio
```

Exemplo de response:

```
200 OK
```

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "8a1fd575-0bc3-4197-ae7d-542bc655fe3b",
            "nickname": "Woozie",
            "first_name": "Wellery",
            "last_name": "Chaves",
            "cellphone": "09876543211",
            "email": "wellery@email.com",
            "wallet": "0.00"
        }
    ]
}
```

## Possíveis Erros:

| Código do erro   | Descrição     |
| ---------------- | ------------- |
| 404 Not Found    | Not Found     |
| 401 Unauthorized | Invalid Token |
| 401 Unauthorized | Missing Token |
