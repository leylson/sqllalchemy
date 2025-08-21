📚 Sistema Escolar (Python + SQLAlchemy)
Este projeto é um sistema escolar simples em desenvolvimento, utilizando Python e SQLAlchemy com banco de dados SQLite para exercitar conhecimentos.
O objetivo é gerenciar pessoas e atividades escolares através de operações básicas de CRUD (Create, Read, Update, Delete).

🚀 Tecnologias utilizadas
Python 3.x

SQLAlchemy

📂 Estrutura do Projeto


├── models.py        # Definição das classes do banco (Pessoas, Atividades)

├── app.py           # Funções para manipular os dados (CRUD)

├── baseEscolar.db   # Banco de dados SQLite (gerado automaticamente)

└── README.md

-------------------------------------------

⚙️ Funcionalidades já implementadas
Criar pessoas no banco de dados

Consultar pessoa pelo nome

Consultar todas as pessoas cadastradas

Alterar idade de uma pessoa

Excluir pessoa do banco

----------------------------------------

🛠️ Como rodar o projeto
Clone este repositório:

git clone https://github.com/seuusuario/seurepositorio.git

cd seurepositorio

-----------------------------------------

Crie um ambiente virtual e instale as dependências:

python -m venv venv

source venv/bin/activate   # Linux/Mac

venv\Scripts\activate      # Windows

pip install sqlalchemy

-------------------------------------------

Inicialize o banco de dados:
python models.py
