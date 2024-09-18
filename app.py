from flask import Flask, render_template, request, jsonify
from agentes import AgenteColetor
from agentes import AgenteDecisor

# Criação da instância do aplicativo Flask
app = Flask(__name__, template_folder='pages')

# Inicializando os agentes
agente_coletor = AgenteColetor()  # Agente responsável por coletar dados do usuário
agente_decisor = AgenteDecisor()  # Agente responsável por processar dados e fornecer recomendações

@app.route('/')
def index():
    """
    Rota para a página inicial. Renderiza o template 'index.html'.
    """
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """
    Rota para receber e processar mensagens do chat.
    Aceita solicitações POST contendo mensagens do usuário.
    """
    # Obtém os dados JSON da solicitação
    data = request.get_json()
    user_message = data.get('message')  # Extrai a mensagem do usuário do JSON

    # Verifica se a mensagem é uma solicitação inicial para iniciar o chat
    if user_message == "Iniciar":
        response_message = "Olá! Eu sou o assistente virtual para cuidados com plantas. Vou te ajudar a cuidar das suas plantas no dia a dia. Primeiro, por favor, informe a temperatura ambiente."
        return jsonify({"response": response_message})

    # O agente coletor simula a coleta de dados a partir da entrada do usuário
    resposta_coletor = agente_coletor.coletar_dados(user_message)
    
    # Se todos os dados foram coletados, processa os dados e retorna a recomendação
    if resposta_coletor == "Obrigado! Agora estou processando suas informações.":
        recomendacoes = agente_decisor.processar_dados(agente_coletor.dados)
        response_message = ""
        # Concatena as recomendações em uma única string para a resposta
        for aspecto, recomendacao in recomendacoes.items():
            response_message += f"{aspecto.capitalize()}: {recomendacao}\n"
        return jsonify({"response": response_message})
    
    # Caso a coleta de dados não esteja completa, retorna a resposta do agente coletor
    return jsonify({"response": resposta_coletor})

# Verifica se o script está sendo executado diretamente e inicia o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)  # Executa o servidor em modo de depuração
