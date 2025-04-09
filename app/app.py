# Importando as bibliotecas essenciais do Flask e SQLAlchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Criando a aplicação Flask
app = Flask(__name__)


# Define a URI de conexão com o banco PostgreSQL
# Formato: 'postgresql://usuário:senha@host:porta/nome_do_banco'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:7856@localhost:5432/crud'

# Desativa o rastreamento de modificações
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Cria uma instância do SQLAlchemy, que será usada para interagir com o banco
db = SQLAlchemy(app)



class Usuario(db.Model):
    # Define a coluna 'id' como chave primária e do tipo inteiro
    id = db.Column(db.Integer, primary_key=True)

    # Coluna 'nome', tipo string com limite de 100 caracteres, obrigatória (nullable=False)
    nome = db.Column(db.String(100), nullable=False)

    # Coluna 'email', tipo string, obrigatória e única (não pode haver duplicados)
    email = db.Column(db.String(100), unique=True, nullable=False)

    # Representação do objeto quando printado no terminal
    def __repr__(self):
        return f'<Usuario {self.nome}>'

# ========================
# Rota principal do sistema
# ========================

@app.route('/')
def home():
    # Mensagem simples de verificação
    return "Hello World! O Flask está rodando corretamente"

# =======================
# Execução da aplicação
# =======================

if __name__ == '__main__':
    # Garante que o contexto da aplicação está ativo ao criar as tabelas
    with app.app_context():
        db.create_all()  # Cria todas as tabelas do banco definidas pelos modelos (caso não existam)

    # Inicia o servidor Flask em modo debug (atualizações automáticas e mensagens de erro detalhadas)
    app.run(debug=True)
