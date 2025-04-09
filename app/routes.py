# Importa os módulos necessários do Flask
from flask import Blueprint, request, jsonify, render_template

# Importa o modelo de usuário e a instância do banco de dados
from .models import Usuario
from . import db

# Criação de um Blueprint chamado 'main'
# Um Blueprint permite organizar o código de forma modular
main = Blueprint('main', __name__)

# ====================
# ROTA RAIZ (HTML)
# ====================
@main.route('/')
def home():
    # Renderiza o arquivo index.html quando acessa a raiz do site
    return render_template('index.html')

# ====================
# CREATE - Criar usuário
# ====================
@main.route('/usuarios', methods=['POST'])
def criar_usuario():
    data = request.get_json()
    novo_usuario = Usuario(nome=data['nome'], email=data['email'])
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify({'mensagem': 'Usuário criado com sucesso!'})

# ====================
# READ - Listar todos os usuários
# ====================
@main.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = Usuario.query.all()
    resultado = [{'id': u.id, 'nome': u.nome, 'email': u.email} for u in usuarios]
    return jsonify(resultado)

# ====================
# UPDATE - Atualizar um usuário
# ====================
@main.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({'erro': 'Usuário não encontrado'}), 404

    data = request.get_json()
    usuario.nome = data['nome']
    usuario.email = data['email']
    db.session.commit()
    return jsonify({'mensagem': 'Usuário atualizado com sucesso'})

# ====================
# DELETE - Deletar um usuário
# ====================
@main.route('/usuarios/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({'erro': 'Usuário não encontrado'}), 404

    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'mensagem': 'Usuário deletado com sucesso'})
