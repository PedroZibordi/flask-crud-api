# Importa o módulo principal do Flask e a extensão SQLAlchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Cria uma instância global do SQLAlchemy (será inicializada depois com a app)
db = SQLAlchemy()


# Essa função cria e configura a aplicação Flask.
# É um padrão recomendado quando se quer estruturar projetos maiores.
def create_app():
    # Cria a instância do Flask
    # 'static_folder' é ajustado para garantir que os arquivos CSS/JS sejam carregados corretamente
    app = Flask(__name__, static_folder='../static')

    # Configurações do banco de dados PostgreSQL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:7856@localhost:5432/crud'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Evita warning e melhora performance

    # Inicializa o SQLAlchemy com o app criado
    db.init_app(app)

    # Importa e registra as rotas da aplicação via Blueprint
    from .routes import main  # Importa o blueprint que define as rotas
    app.register_blueprint(main)  # Registra esse blueprint na aplicação principal

    # Retorna a aplicação pronta para uso
    return app
