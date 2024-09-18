from sistemas_regras import SistemaRegras

# Classe responsável por coletar dados do usuário
class AgenteColetor:
    def __init__(self):
        self.dados = {}  # Dicionário para armazenar os dados coletados

    def coletar_dados(self, mensagem):
        """
        Coleta dados com base na mensagem recebida e armazena no dicionário de dados.
        Retorna uma mensagem solicitando o próximo dado a ser informado.
        """
        if 'temperatura' not in self.dados:
            # Armazena a temperatura se ainda não foi coletada
            self.dados['temperatura'] = float(mensagem)
            return "Agora, por favor, informe a umidade ambiente (%):"
        elif 'umidade' not in self.dados:
            # Armazena a umidade se ainda não foi coletada
            self.dados['umidade'] = float(mensagem)
            return "Informe o tipo de solo:"
        elif 'tipo_solo' not in self.dados:
            # Armazena o tipo de solo se ainda não foi coletado
            self.dados['tipo_solo'] = mensagem
            return "Por fim, informe o tipo de planta:"
        elif 'tipo_planta' not in self.dados:
            # Armazena o tipo de planta se ainda não foi coletado
            self.dados['tipo_planta'] = mensagem
            return "Obrigado! Agora estou processando suas informações."
        else:
            # Mensagem retornada se todos os dados já foram coletados
            return "Todos os dados foram coletados."

# Classe responsável por processar dados e gerar recomendações
class AgenteDecisor:
    def __init__(self):
        pass

    def processar_dados(self, dados):
        """
        Processa os dados coletados e gera recomendações usando o SistemaRegras.
        """
        sistema = SistemaRegras(dados['temperatura'], dados['umidade'], dados['tipo_solo'], dados['tipo_planta'])
        return sistema.gerar_recomendacao()  # Retorna as recomendações geradas pelo sistema
