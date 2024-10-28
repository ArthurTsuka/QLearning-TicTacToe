import random

class Agent:
    # Alpha = Define o quanto o agente valoriza novas informações em relação às antigas na atualização do q-value
    # gamma = Define a importancia das recompensas futuras em relação às recompensas imediatas
    # Episilon = Controla a frequência com que o agente faz uma jogada aleatoria em vez de escolher a ação de maior valor da tablea Q
    def __init__(self, alpha=0.1, gamma=0.1, epsilon = 0.05):
        self.q_table = {} 
        self.apha = alpha # Taxa de aprendizado
        self.gamma = gamma # Fator de Desconto
        self.epsilon = epsilon # Probabilidade fazer uma exploração aleatoria

    # fUNÇÃO para determinar a escolha da proxima acao (Aleatoria ou baseada na tabela Q)
    def escolha_acao(self, estado, acoes):
        # Exploração aleatoria
        if random.random() < self.epsilon:
            return random.choice(acoes)
        maximo_q = float("-inf") # Valor extremamente baixo(pra passar pelo if (sempre))
        best_acoes = [] # Melhores ações

        # Exploração baseada na q-table
        for acao in acoes:
            q_value = self.q_table.get((estado, acao), 0)

            if q_value > maximo_q:
                maximo_q = q_value
                best_acoes = [acao]
            elif q_value == maximo_q:
                best_acoes.append(acao)
        # Caso tenha mais de uma ação "boa", escolhemos aleatoriamente, as melhores açoes, caso nao tenha ação boa, escolhemos alguma acao aleatoria dentro de acoes.
        return random.choice(best_acoes) if best_acoes else random.choice(acoes)
        
    # Função responsavel pea atualização da tabela de acordo com a equação de bellman    
    def atualizacao_q_value(self, estado, acao, recompensa, prox_estado, prox_acoes):
        q_value = self.q_table.get((estado, acao), 0)


        maximo_q = float("-inf")
        for prox_acao in prox_acoes:
            prox_q_value = self.q_table.get((prox_estado, prox_acao), 0)
            if prox_q_value > maximo_q:
                maximo_q = prox_q_value
        # Equação de bellman / Atualização da tabela
        self.q_table[(estado, acao)] = q_value + self.apha * (recompensa + self.gamma * maximo_q - q_value)
