# Importa a função create_app do pacote app
# Essa função está no __init__.py e configura toda a aplicação Flask
from app import create_app

# Cria uma instância da aplicação chamando a função create_app
app = create_app()

# Condicional que verifica se esse arquivo está sendo executado diretamente
# Se sim, inicia o servidor Flask em modo debug
if __name__ == '__main__':
    app.run(debug=True)