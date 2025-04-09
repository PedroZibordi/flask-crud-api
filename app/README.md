# Primeiro CRUD com Flask + PostgreSQL

Este é meu primeiro projeto prático de API, construído com **Python**, **Flask**, **SQLAlchemy** e **PostgreSQL**.  
O objetivo é desenvolver uma API RESTful com as operações básicas de CRUD (Create, Read, Update, Delete), aprendendo a estrutura de um backend real, integrado com banco de dados relacional.

---

## Tecnologias utilizadas

- Python
- Flask
- Flask SQLAlchemy
- PostgreSQL
- HTML, CSS e JavaScript (básico)
- Postman (para testes da API)

---

## Estrutura do projeto

Primeiro CRUD/ ├── app/ │ ├── init.py │ ├── models.py │ ├── routes.py │ └── templates/ │ └── index.html │ ├── static/ │ ├── style.css │ └── script.js │ ├── run.py ├── requirements.txt └── README.md

yaml
Copiar
Editar

---

## Como executar localmente

1. Clone o repositório:
```bash
git clone https://github.com/PedroZibordi/Portf-lioPZ.git
cd Portf-lioPZ
Crie e ative um ambiente virtual:

bash
Copiar
Editar
python -m venv venv
venv\Scripts\activate  # (no Windows)
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Verifique se o PostgreSQL está rodando e que o banco crud foi criado.

Execute o projeto:

bash
Copiar
Editar
python run.py
Acesse no navegador: http://127.0.0.1:5000

🔗 Endpoints da API
Método	Endpoint	Descrição
GET	/usuarios	Lista todos os usuários
POST	/usuarios	Cadastra novo usuário
PUT	/usuarios/<id>	Atualiza usuário
DELETE	/usuarios/<id>	Deleta usuário
‍💻 Autor
Feito por Pedro Zibordi.
🔗 GitHub: @PedroZibordi
🌐 Portfólio: Portf-lioPZ

