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
        # Gera recomendações de rega com base na temperatura e no tipo de planta.
        # Para cactos, suculentas, aloe vera e lavanda, que têm necessidades de rega semelhantes
        if self.tipo_planta in ["cacto", "suculenta", "aloe vera", "lavanda"]:
            # Se a temperatura estiver alta (> 30°C), recomenda-se regar esporadicamente e manter o solo seco
            if self.temperatura > 30:
                return "Temperatura alta. Regar esporadicamente, mantendo o solo seco entre as regas."
            else:
                # Caso contrário, regar com moderação, já que essas plantas preferem solo seco
                return "Regar com moderação. Essas plantas preferem solo seco e não toleram encharcamento."

        # Para orquídeas, que têm necessidades específicas de umidade
        elif self.tipo_planta == "orquidea":
            # Se a temperatura estiver acima de 25°C, recomenda-se rega frequente para manter a umidade
            if self.temperatura > 25:
                return "Orquídeas gostam de umidade e rega frequente. Mantenha o solo levemente úmido."
            else:
                # Em temperaturas mais baixas, regar moderadamente para evitar encharcamento
                return "Regar moderadamente. Orquídeas não toleram solo encharcado."

        # Para plantas carnívoras, que precisam de solo úmido e água específica
        elif self.tipo_planta == "planta carnívora":
            if self.temperatura > 20:
                # Manter o solo úmido e usar água de chuva ou destilada é recomendado
                return "Manter o solo úmido, mas não encharcado. Plantas carnívoras preferem água de chuva ou água destilada."

        # Para plantas como pothos, ficus, lírio da paz e hortênsias
        elif self.tipo_planta in ["pothos", "ficus", "lírio da paz", "hortênsia"]:
            # Em temperaturas acima de 25°C, elas gostam de umidade, e a rega regular é importante
            if self.temperatura > 25:
                return "Essas plantas gostam de umidade. Regar regularmente, mas permita que o solo seque entre as regas."
            else:
                # Caso contrário, regar moderadamente para manter a umidade do solo
                return "Regar moderadamente. Mantenha a umidade do solo."

        # Para rosas e hortênsias
        elif self.tipo_planta in ["rosa", "hortênsia"]:
            # Em temperaturas altas (> 30°C), rega diária é recomendada
            if self.temperatura > 30:
                return "Precisam de bastante água em altas temperaturas. Regar diariamente."
            else:
                # Caso contrário, regar de forma moderada para manter o solo úmido
                return "Regar de forma moderada. Preferem solo úmido, mas não encharcado."

        # Para plantas frutíferas e cítricas
        elif self.tipo_planta in ["frutíferas", "citrus"]:
            # Em altas temperaturas (> 30°C), é necessário regar diariamente
            if self.temperatura > 30:
                return "Essas plantas precisam de bastante água em altas temperaturas. Regar diariamente."
            else:
                # Em temperaturas mais baixas, regar moderadamente, mantendo o solo úmido
                return "Regar moderadamente, mantendo o solo úmido."

        # Para leguminosas como feijão, ervilha, lentilha, grão-de-bico e soja
        elif self.tipo_planta in ["feijão", "ervilha", "lentilha", "grão-de-bico", "soja"]:
            # Em temperaturas acima de 25°C, rega frequente é necessária
            if self.temperatura > 25:
                return "Essas plantas gostam de solo úmido. Regar frequentemente em temperaturas quentes."
            else:
                # Em temperaturas mais baixas, regar moderadamente para manter o solo levemente úmido
                return "Regar moderadamente. Manter o solo levemente úmido."

        # Regras gerais para plantas que não se enquadram nas categorias acima
        else:
            if self.temperatura > 35:
                # Em temperaturas muito altas (> 35°C), rega diária é recomendada
                return "A temperatura está muito alta. Rega diária é recomendada para evitar que a planta sofra com a desidratação."
            elif self.temperatura > 30:
                if self.umidade < 40:
                    # Temperatura alta (> 30°C) e umidade baixa (< 40%) requerem rega frequente
                    return "Temperatura alta e umidade baixa. Regar frequentemente para manter o solo úmido."
                elif self.umidade < 60:
                    # Se a umidade estiver entre 40% e 60%, regar moderadamente
                    return "Temperatura alta. Regar moderadamente e monitorar a umidade do solo."
                else:
                    # Se a umidade estiver acima de 60%, monitorar o solo e regar conforme necessário
                    return "Temperatura alta, mas a umidade está adequada. Monitorar o solo e regar conforme necessário."
            elif self.temperatura > 25:
                if self.umidade < 40:
                    # Temperatura moderada (> 25°C) e umidade baixa (< 40%) requerem rega frequente
                    return "Temperatura alta e umidade baixa. Regar frequentemente para evitar que a planta sofra com a falta de água."
                elif self.umidade < 60:
                    # Se a umidade estiver entre 40% e 60%, regar moderadamente
                    return "Temperatura moderada e umidade baixa. Regar de forma moderada e ajustar conforme necessário."
                else:
                    # Se a umidade estiver acima de 60%, regar conforme necessário
                    return "Temperatura moderada e umidade adequada. Regar conforme a necessidade da planta."
            elif self.temperatura > 20:
                if self.umidade < 40:
                    # Temperatura agradável (> 20°C) e umidade baixa (< 40%) requerem rega moderada
                    return "Temperatura agradável, mas umidade baixa. Regar moderadamente para manter o solo úmido."
                elif self.umidade < 60:
                    # Se a umidade estiver entre 40% e 60%, monitorar o solo e regar conforme necessário
                    return "Temperatura agradável. Monitorar o solo e regar de acordo com a necessidade da planta."
                else:
                    # Se a umidade estiver acima de 60%, regar conforme necessário
                    return "Temperatura e umidade estão boas. Regar conforme a necessidade da planta."
            else:
                # Para temperaturas abaixo de 20°C, ajustes de rega com base na umidade
                if self.umidade < 40:
                    return "Temperatura baixa e umidade baixa. Regar moderadamente para evitar que o solo fique seco."
                elif self.umidade < 60:
                    return "Temperatura baixa. Ajustar a rega conforme a umidade do solo e a necessidade da planta."
                else:
                    return "Temperatura baixa e umidade adequada. Monitorar a planta e ajustar a rega conforme necessário."

    def recomendacao_solo(self):
        # Gera recomendações de solo com base no tipo de solo e tipo de planta.

        # Obtém a recomendação básica para o tipo de solo a partir de um dicionário de recomendações predefinidas.
        # Se o tipo de solo não for encontrado, retorna uma mensagem padrão.
        recomendacao = self.recomendacoes_solo.get(self.tipo_solo, "Tipo de solo desconhecido. Verificar condições.")
        
        # Ajusta a recomendação de solo dependendo do tipo de planta.
        
        # Para plantas como cactos, suculentas, aloe vera e lavanda, que preferem solos bem drenados.
        if self.tipo_planta in ["cacto", "suculenta", "aloe vera", "lavanda"]:
            # Verifica se o solo atual é adequado, fornecendo boa drenagem.
            if self.tipo_solo in ["arenoso", "franco", "organico", "calcário", "xistoso"]:
                recomendacao += f" Este solo é adequado para {self.tipo_planta}, pois proporciona uma boa drenagem."
            else:
                # Caso o solo não seja adequado, recomenda um solo mais drenante.
                recomendacao += " Este solo não é ideal para essa planta. Considere usar um solo mais drenante."
        
        # Para orquídeas, que preferem solos leves e com boa drenagem.
        elif self.tipo_planta == "orquidea":
            # Verifica se o solo é adequado para manter a umidade e proporcionar drenagem.
            if self.tipo_solo in ["organico", "peat"]:
                recomendacao += " Este solo é adequado para orquídeas, pois mantém a umidade e proporciona boa drenagem."
            else:
                # Se o solo não for ideal, sugere usar um mais adequado.
                recomendacao += " Este solo não é ideal para orquídeas. Considere usar um solo mais leve e drenante."
        
        # Para plantas carnívoras, que precisam de solos úmidos.
        elif self.tipo_planta == "planta carnívora":
            # Verifica se o solo é capaz de reter umidade e fornecer os nutrientes necessários.
            if self.tipo_solo in ["peat", "hidromórfico"]:
                recomendacao += " Este solo é adequado para plantas carnívoras, pois mantém a umidade e fornece nutrientes necessários."
            else:
                # Sugere um solo mais adequado para reter água.
                recomendacao += " Este solo não é ideal para plantas carnívoras. Considere usar um solo com alta capacidade de retenção de água."

        # Para plantas de interior como pothos, ficus, lírio da paz e hortênsias, que requerem um equilíbrio de nutrientes e drenagem.
        elif self.tipo_planta in ["pothos", "ficus", "lírio da paz", "hortênsia"]:
            # Verifica se o solo fornece o equilíbrio certo entre nutrientes e drenagem.
            if self.tipo_solo in ["franco", "argiloso", "organico"]:
                recomendacao += f" Este solo é ideal para {self.tipo_planta}, pois proporciona um bom equilíbrio de nutrientes e drenagem."
            else:
                # Se o solo não for adequado, recomenda ajustar o solo para atender às necessidades da planta.
                recomendacao += " Este solo não é o mais adequado para essa planta. Considere usar um solo mais equilibrado."

        # Para plantas frutíferas e cítricas, que precisam de solo rico em nutrientes e boa drenagem.
        elif self.tipo_planta in ["frutíferas", "citrus"]:
            # Verifica se o solo é apropriado para frutíferas.
            if self.tipo_solo in ["franco", "argiloso", "aluvial"]:
                recomendacao += " Este solo é adequado para frutíferas, pois fornece nutrientes necessários e boa drenagem."
            else:
                # Sugere um solo mais rico em nutrientes caso o solo atual não seja ideal.
                recomendacao += " Este solo pode não ser o mais adequado para frutíferas. Considere usar solo mais rico em nutrientes."

        # Para rosas e hortênsias, que preferem solos que retêm umidade e nutrientes.
        elif self.tipo_planta in ["rosa", "hortênsia"]:
            # Verifica se o solo retém umidade suficiente e fornece nutrientes.
            if self.tipo_solo in ["franco", "argiloso", "organico"]:
                recomendacao += f" Este solo é ideal para {self.tipo_planta}, pois proporciona boa retenção de umidade e nutrientes."
            else:
                # Recomenda um solo mais adequado caso o atual não seja o melhor.
                recomendacao += f" Este solo não é o ideal para {self.tipo_planta}. Considere um solo mais rico."

        # Para leguminosas como feijão, ervilha e grão-de-bico, que requerem solos que mantenham a umidade e forneçam nutrientes.
        elif self.tipo_planta in ["feijão", "ervilha", "lentilha", "grão-de-bico", "soja"]:
            # Verifica se o solo mantém a umidade e é nutritivo o suficiente.
            if self.tipo_solo in ["franco", "argiloso", "aluvial"]:
                recomendacao += " Este solo é adequado para leguminosas, pois mantém a umidade e fornece nutrientes."
            else:
                # Caso o solo não seja o ideal, recomenda um solo mais nutritivo.
                recomendacao += " Este solo pode não ser o ideal para leguminosas. Considere usar um solo mais rico em nutrientes."

        # Caso o tipo de planta não se enquadre em nenhum dos grupos anteriores, fornece uma recomendação genérica.
        else:
            recomendacao += " Para essa planta, recomenda-se verificar as necessidades específicas do solo."

        # Retorna a recomendação final ajustada.
        return recomendacao
        

    def recomendacao_solar(self):
        # Gera recomendações de exposição solar com base na temperatura e no tipo de planta.
        # Verifica se a planta é do tipo que prefere sol intenso (ex.: cactos, suculentas).
        if self.tipo_planta in ["cacto", "suculenta", "aloe vera", "lavanda"]:
            # Se a temperatura for maior que 30°C, recomenda sol direto e intenso.
            if self.temperatura > 30:
                return f"{self.tipo_planta} preferem sol direto e intenso. Garantir boa iluminação mesmo em temperaturas altas."
            else:
                # Caso contrário, recomenda exposição ao sol por várias horas do dia.
                return "Proporcionar luz solar direta por várias horas do dia. Essas plantas prosperam com muita luz."

        # Verifica se a planta é uma orquídea, que prefere luz indireta.
        elif self.tipo_planta == "orquidea":
            # Para temperaturas acima de 25°C, evitar sol direto para prevenir queimaduras.
            if self.temperatura > 25:
                return "Orquídeas preferem luz indireta e filtrada. Evitar sol direto que pode causar queimaduras."
            else:
                # Se a temperatura estiver abaixo de 25°C, luz indireta ainda é a recomendação.
                return "Proporcionar luz indireta e filtrada. Orquídeas não precisam de sol direto intenso."

        # Verifica se a planta é carnívora, que tem uma preferência por luz direta.
        elif self.tipo_planta == "planta carnívora":
            # Se a temperatura for superior a 20°C, recomenda exposição solar direta.
            if self.temperatura > 20:
                return "Plantas carnívoras gostam de luz direta. Garantir exposição solar adequada para estimular o crescimento e captura de insetos."
            else:
                # Se estiver muito frio, recomenda evitar sol direto.
                return "Proporcionar luz indireta se estiver muito frio. Evitar o sol direto para não estressar a planta."

        # Para plantas como pothos, ficus, lírio da paz e hortênsias, as recomendações variam com a temperatura.
        elif self.tipo_planta in ["pothos", "ficus", "lírio da paz", "hortênsia"]:
            # Em temperaturas abaixo de 15°C, recomenda aumentar a exposição ao sol.
            if self.temperatura < 15:
                return "Temperatura baixa. Aumentar a exposição ao sol, se possível, para garantir que a planta receba luz suficiente."
            # Para temperaturas abaixo de 20°C, luz solar direta nas horas mais quentes do dia.
            elif self.temperatura < 20:
                return "Temperatura fria. Proporcionar luz solar direta durante as horas mais quentes do dia para ajudar no crescimento."
            # Para temperaturas abaixo de 25°C, recomenda luz direta pela manhã e sombra parcial à tarde.
            elif self.temperatura < 25:
                return "Temperatura amena. A exposição ao sol deve ser adequada, proporcionando luz direta durante a manhã e sombra parcial à tarde."
            # Para temperaturas acima de 25°C, evitar exposição excessiva ao sol nas horas mais quentes.
            else:
                return "Temperatura quente. Garantir que a planta receba luz solar direta, mas evitar a exposição excessiva durante as horas mais quentes do dia para prevenir queimaduras."

        # Para plantas frutíferas ou citrus, a recomendação depende da temperatura.
        elif self.tipo_planta in ["frutíferas", "citrus"]:
            # Se a temperatura for inferior a 20°C, recomenda aumentar a exposição ao sol para auxiliar na frutificação.
            if self.temperatura < 20:
                return "Temperatura baixa. Aumentar a exposição ao sol para ajudar na frutificação."
            # Se a temperatura for inferior a 25°C, recomenda luz solar direta, principalmente pela manhã.
            elif self.temperatura < 25:
                return "Temperatura amena. Proporcionar luz solar direta, principalmente durante a manhã."
            # Para temperaturas mais altas, recomenda sol pleno, mas proteção em temperaturas extremas.
            else:
                return "Temperatura quente. Essas plantas preferem sol pleno, mas em temperaturas extremas, proteger das horas mais quentes."

        # Para rosas e hortênsias, as recomendações variam de acordo com a temperatura.
        elif self.tipo_planta in ["rosa", "hortênsia"]:
            # Para temperaturas abaixo de 15°C, garantir luz, mas evitar temperaturas extremas.
            if self.temperatura < 15:
                return "Temperatura baixa. Proteger das temperaturas extremas, mas garantir luz suficiente."
            # Para temperaturas amenas (até 25°C), luz direta de manhã e sombra à tarde.
            elif self.temperatura < 25:
                return "Temperatura amena. Proporcionar luz solar direta pela manhã e sombra à tarde para rosas e hortênsias."
            # Em temperaturas quentes, sombra parcial durante as horas mais quentes.
            else:
                return "Temperatura quente. Garantir que as rosas e hortênsias tenham sombra parcial durante as horas mais quentes."

        # Caso a planta não esteja listada acima, seguem recomendações gerais para diferentes faixas de temperatura.
        else:
            # Temperatura muito baixa (< 10°C): aumentar a exposição ao sol.
            if self.temperatura < 10:
                return "Temperatura muito baixa. Aumentar a exposição ao sol para promover o crescimento, especialmente em ambientes internos ou durante o inverno."
            # Temperaturas frias (10°C - 15°C): aumentar a exposição ao sol.
            elif self.temperatura < 15:
                return "Temperatura baixa. Aumentar a exposição ao sol, se possível, para garantir que a planta receba luz suficiente."
            # Temperaturas amenas (15°C - 20°C): exposição ao sol durante as horas mais quentes.
            elif self.temperatura < 20:
                return "Temperatura fria. Proporcionar luz solar direta durante as horas mais quentes do dia para ajudar no crescimento."
            # Temperatura amena (20°C - 25°C): luz direta de manhã, sombra à tarde.
            elif self.temperatura < 25:
                return "Temperatura amena. A exposição ao sol deve ser adequada, proporcionando luz direta durante a manhã e sombra parcial à tarde."
            # Temperatura quente (25°C - 30°C): evitar sol excessivo.
            elif self.temperatura < 30:
                return "Temperatura quente. Garantir que a planta receba luz solar direta, mas evitar a exposição excessiva durante as horas mais quentes do dia para prevenir queimaduras."
            # Temperaturas altas (30°C - 35°C): proteger a planta de luz direta nas horas mais quentes.
            elif self.temperatura < 35:
                return "Temperatura alta. Proteger a planta da luz solar direta nas horas mais quentes para evitar estresse térmico. Fornecer sombra parcial pode ser benéfico."
            # Temperatura muito alta (> 35°C): reduzir exposição solar.
            else:
                return "Temperatura muito alta. Reduzir a exposição ao sol para evitar queimaduras e estresse térmico. Fornecer sombra e garantir a ventilação adequada."

    # Método que gerará a recomendação com base em todas as regras declaradas acima
    def gerar_recomendacao(self):
        """
        Gera um dicionário com as recomendações de água, solo e exposição solar.
        """
        return {
            "Água": self.recomendacao_agua(), # Busca a recomendação de água
            "\nSolo": self.recomendacao_solo(), # Busca a recomendação de solo
            "\nSol": self.recomendacao_solar() # Busca a recomendação de sol
        }
