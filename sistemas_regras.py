class SistemaRegras:
    def __init__(self, temperatura, umidade, tipo_solo, tipo_planta):
        """
        Inicializa o sistema de regras com os dados fornecidos.
        
        :param temperatura: Temperatura ambiente em graus Celsius.
        :param umidade: Umidade ambiente em porcentagem.
        :param tipo_solo: Tipo de solo onde a planta está cultivada.
        :param tipo_planta: Tipo de planta para a qual as recomendações são fornecidas.
        """
        self.temperatura = temperatura
        self.umidade = umidade  
        self.tipo_solo = tipo_solo
        self.tipo_planta = tipo_planta

        # Dicionário de recomendações para diferentes tipos de solo
        self.recomendacoes_solo = {
            "arenoso": "Adicionar mais matéria orgânica ao solo. Este solo é ideal para cactos, lavandas e plantas de regiões áridas.",
            "argiloso": "Verificar a drenagem do solo e evitar o encharcamento. Adequado para feijão, batata e cenoura.",
            "siltoso": "Adicionar compostos para melhorar a estrutura do solo e evitar o encharcamento. Ideal para alface, couve e ervilhas.",
            "franco": "Boa mistura de areia, silte e argila. Adequado para quase todas as plantas, como tomate, pimentão e flores.",
            "organico": "Rico em matéria orgânica e nutrientes. Praticamente todas as plantas prosperam, incluindo vegetais e flores.",
            "calcário": "Solo alcalino com altos níveis de cálcio. Ideal para plantas que preferem pH mais alto, como lavandas e algumas ervas.",
            "peat": "Solo ácido com boa capacidade de retenção de água. Ideal para blueberries, camélias e plantas acidófilas.",
            "podzol": "Solo ácido e de baixo nutriente encontrado em regiões frias. Adequado para coníferas e algumas plantas silvestres.",
            "aluvial": "Solo fértil formado por sedimentos de inundação. Adequado para arroz, milho e vegetais de raiz.",
            "laterítico": "Solo denso e difícil encontrado em regiões tropicais. Ideal para mandioca e algumas frutas tropicais.",
            "xistoso": "Solo com rochas e fragmentos de pedra. Bem drenado, mas pouco fértil. Ideal para plantas resistentes como lavanda e ervas mediterrâneas.",
            "vulcânico": "Solo fértil formado por cinzas vulcânicas e lava. Ideal para tomates e batatas.",
            "hidromórfico": "Solo com problemas de drenagem devido à alta umidade. Adequado para plantas aquáticas e semi-aquáticas como junco e nenúfar.",
            "típico": "Solo bem equilibrado, ideal para uma ampla gama de plantas, semelhante ao solo franco.",
            "areno-argiloso": "Mistura de areia e argila. Ideal para culturas que se beneficiam de uma boa mistura de drenagem e retenção de água, como cenouras e ervilhas.",
        }

    def recomendacao_agua(self):
        """
        Gera recomendações de rega com base na temperatura e no tipo de planta.
        """
        if self.tipo_planta == "cacto" or self.tipo_planta == "suculenta":
            if self.temperatura > 30:
                return "Temperatura alta. Regar esporadicamente, mantendo o solo seco entre as regas."
            else:
                return "Regar com moderação. Cactos e suculentas preferem solo seco e não toleram encharcamento."
        elif self.tipo_planta == "orquidea":
            if self.temperatura > 25:
                return "Orquídeas gostam de umidade e rega frequente. Mantenha o solo levemente úmido."
            else:
                return "Regar moderadamente. Orquídeas não toleram solo encharcado."
        elif self.tipo_planta == "planta carnívora":
            if self.temperatura > 20:
                return "Manter o solo úmido, mas não encharcado. Plantas carnívoras preferem água de chuva ou água destilada."
        else:
            if self.temperatura > 35:
                return "A temperatura está muito alta. Rega diária é recomendada para evitar que a planta sofra com a desidratação."
            elif self.temperatura > 30:
                if self.umidade < 40:
                    return "A temperatura está alta e a umidade está baixa. Regar com frequência para manter o solo úmido."
                elif self.umidade < 60:
                    return "A temperatura está alta. Regar moderadamente e monitorar a umidade do solo."
                else:
                    return "Temperatura alta, mas a umidade está adequada. Monitorar o solo e regar conforme necessário."
            elif self.temperatura > 25:
                if self.umidade < 40:
                    return "Temperatura alta e umidade baixa. Regar frequentemente para evitar que a planta sofra com a falta de água."
                elif self.umidade < 60:
                    return "Temperatura moderada e umidade baixa. Regar de forma moderada e ajustar conforme necessário."
                else:
                    return "Temperatura moderada e umidade adequada. Regar conforme a necessidade da planta."
            elif self.temperatura > 20:
                if self.umidade < 40:
                    return "Temperatura agradável, mas umidade baixa. Regar moderadamente para manter o solo úmido."
                elif self.umidade < 60:
                    return "Temperatura agradável. Monitorar o solo e regar de acordo com a necessidade da planta."
                else:
                    return "Temperatura e umidade estão boas. Regar conforme a necessidade da planta."
            else:
                if self.umidade < 40:
                    return "Temperatura baixa e umidade baixa. Regar moderadamente para evitar que o solo fique seco."
                elif self.umidade < 60:
                    return "Temperatura baixa. Ajustar a rega conforme a umidade do solo e a necessidade da planta."
                else:
                    return "Temperatura baixa e umidade adequada. Monitorar a planta e ajustar a rega conforme necessário."

    def recomendacao_solo(self):
        """
        Gera recomendações de solo com base no tipo de solo e tipo de planta.
        """
        # Obtém a recomendação básica para o tipo de solo
        recomendacao = self.recomendacoes_solo.get(self.tipo_solo, "Tipo de solo desconhecido. Verificar condições.")
        
        # Ajusta a recomendação com base no tipo de planta
        if self.tipo_planta in ["cacto", "suculenta"]:
            if self.tipo_solo in ["arenoso", "franco", "organico"]:
                recomendacao += " Este solo é adequado para cactos e suculentas, pois proporciona uma boa drenagem."
            else:
                recomendacao += " Este solo não é ideal para cactos e suculentas. Considere usar um solo mais drenante."
        elif self.tipo_planta == "orquidea":
            if self.tipo_solo in ["organico", "peat"]:
                recomendacao += " Este solo é adequado para orquídeas, pois mantém a umidade e proporciona boa drenagem."
            else:
                recomendacao += " Este solo não é ideal para orquídeas. Considere usar um solo mais leve e drenante."
        elif self.tipo_planta == "planta carnívora":
            if self.tipo_solo in ["peat", "hidromórfico"]:
                recomendacao += " Este solo é adequado para plantas carnívoras, pois mantém a umidade e fornece nutrientes necessários."
            else:
                recomendacao += " Mas este solo não é ideal para plantas carnívoras. Considere usar um solo com alta capacidade de retenção de água."
        
        return recomendacao

    def recomendacao_solar(self):
        """
        Gera recomendações de exposição solar com base na temperatura e no tipo de planta.
        """
        if self.tipo_planta in ["cacto", "suculenta"]:
            if self.temperatura > 30:
                return "Cactos e suculentas preferem sol direto e intenso. Garantir boa iluminação mesmo em temperaturas altas."
            else:
                return "Proporcionar luz solar direta por várias horas do dia. Cactos e suculentas prosperam com muita luz."
        elif self.tipo_planta == "orquidea":
            if self.temperatura > 25:
                return "Orquídeas preferem luz indireta e filtrada. Evitar sol direto que pode causar queimaduras."
            else:
                return "Proporcionar luz indireta e filtrada. Orquídeas não precisam de sol direto intenso."
        elif self.tipo_planta == "planta carnívora":
            if self.temperatura > 20:
                return "Plantas carnívoras gostam de luz direta. Garantir exposição solar adequada para estimular o crescimento e captura de insetos."
            else:
                return "Proporcionar luz indireta se estiver muito frio. Evitar o sol direto para não estressar a planta."
        else:
            if self.temperatura < 10:
                return "Temperatura muito baixa. Aumentar a exposição ao sol para promover o crescimento, especialmente em ambientes internos ou durante o inverno."
            elif self.temperatura < 15:
                return "Temperatura baixa. Aumentar a exposição ao sol, se possível, para garantir que a planta receba luz suficiente."
            elif self.temperatura < 20:
                return "Temperatura fria. Proporcionar luz solar direta durante as horas mais quentes do dia para ajudar no crescimento."
            elif self.temperatura < 25:
                return "Temperatura amena. A exposição ao sol deve ser adequada, proporcionando luz direta durante a manhã e sombra parcial à tarde."
            elif self.temperatura < 30:
                return "Temperatura quente. Garantir que a planta receba luz solar direta, mas evitar a exposição excessiva durante as horas mais quentes do dia para prevenir queimaduras."
            elif self.temperatura < 35:
                return "Temperatura alta. Proteger a planta da luz solar direta nas horas mais quentes para evitar estresse térmico. Fornecer sombra parcial pode ser benéfico."
            else:
                return "Temperatura muito alta. Reduzir a exposição ao sol para evitar queimaduras e estresse térmico. Fornecer sombra e garantir a ventilação adequada."

    def gerar_recomendacao(self):
        """
        Gera um dicionário com as recomendações de água, solo e exposição solar.
        """
        return {
            "Água": self.recomendacao_agua(),
            "\nSolo": self.recomendacao_solo(),
            "\nSol": self.recomendacao_solar()
        }
