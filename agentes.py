from sistemas_regras import SistemaRegras

# Classe responsável por coletar dados do usuário
class AgenteColetor:
    def __init__(self):
        self.dados = {}  # Dicionário para armazenar os dados coletados

    def coletar_dados(self, mensagem):
        """
        Coleta dados com base na mensagem recebida e armazena no dicionário de dados.
        Também reconhece saudações e responde apropriadamente.
        """
        # Verifica se a mensagem é uma saudação
        saudacoes = {
            "oi": "Olá! Como posso ajudar?",
            "bom dia": "Bom dia! Como posso ajudar?",
            "boa tarde": "Boa tarde! Como posso ajudar?",
            "boa noite": "Boa noite! Como posso ajudar?"
        }

        mensagem_lower = mensagem.lower()  # Converte a mensagem para minúsculas para facilitar a comparação

        # Se a mensagem for uma saudação, responde com a saudação correspondente
        if mensagem_lower in saudacoes:
            return saudacoes[mensagem_lower]
        
        # Caso não seja uma saudação, prossegue com a coleta de dados
        if 'temperatura' not in self.dados:
            try:
                # Verifica se a entrada é um número válido para temperatura
                self.dados['temperatura'] = float(mensagem)
                return "Agora, por favor, informe a umidade ambiente (%):"
            except ValueError:
                return "Por favor, insira um valor numérico válido para a temperatura (°C):"
        elif 'umidade' not in self.dados:
            try:
                # Verifica se a entrada é um número válido para umidade
                self.dados['umidade'] = float(mensagem)
                return "Informe o tipo de solo:"
            except ValueError:
                return "Por favor, insira um valor numérico válido para a umidade (%):"
        elif 'tipo_solo' not in self.dados:
            # Verifica se o tipo de solo é um valor esperado
            tipos_solo_validos = ['arenoso', 'argiloso', 'humoso', 'siltoso', 'franco', 'organico', 'calcário', 'peat', 'podzol', 'aluvial', 'laterítico', 'xistoso', 'vulcânico', 'hidromórfico', 'típico', 'areno-argiloso']
            if mensagem_lower in tipos_solo_validos:
                self.dados['tipo_solo'] = mensagem_lower
                return "Por fim, informe o tipo de planta:"
            else:
                return "Tipo de solo inválido ou não está na base de dados. Por favor, escolha entre: " + ", ".join(tipos_solo_validos) + "."
        elif 'tipo_planta' not in self.dados:
            # Valida o tipo de planta
            # tipos_planta_validos = ['cacto', 'suculenta', 'orquidea', 'planta carnívora', 'violeta', 'samambaia', 'gerânio']  # Adicione mais tipos se necessário
            tipos_planta_validos = [
                'cacto', 'suculenta', 'orquidea', 'planta carnívora', 'violeta', 'samambaia', 'gerânio',  # Tipos originais
                # Plantas de Interior
                'pothos', 'ficus', 'lírio da paz',
                # Plantas de Exterior
                'rosa', 'hortênsia', 'lavanda', 'bromélia', 'azaleia',
                # Plantas Ornamentais
                'orquídea', 'palmeira', 'suculentas', 'cipreste', 'árvore da felicidade',
                # Plantas Medicinais
                'aloe vera', 'camomila', 'erva-cidreira', 'hortelã', 'gengibre',
                # Plantas Frutíferas
                'laranja', 'maçã', 'banana', 'abacate', 'manga',
                # Plantas Leguminosas
                'feijão', 'ervilha', 'lentilha', 'grão-de-bico', 'soja'
            ]
            if mensagem.lower() in tipos_planta_validos:
                self.dados['tipo_planta'] = mensagem
                return "Obrigado! Agora estou processando suas informações."
            else:
                return "Tipo de planta inválido. Por favor, escolha entre: " + ", ".join(tipos_planta_validos) + "."
        else:
            # Mensagem retornada se todos os dados já foram coletados
            return self.finalizar_coleta()
        
    def finalizar_coleta(self):
        """
        Finaliza a coleta de dados, processa os dados e limpa as entradas.
        """
        # Aqui você pode chamar o AgenteDecisor para processar os dados, se necessário
        return "Vamos começar novamente.\n", self.resetar_coleta()

    def resetar_coleta(self):
        """
        Limpa o dicionário de dados para reiniciar a coleta de informações.
        """
        self.dados.clear()  # Limpa o dicionário de dados para começar novamente
        return "Por favor, informe a temperatura ambiente (°C):"




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
