import random
import matplotlib.pyplot as plt
from src.ambiente import tictactoe
from src.agente import Agent

def train_agente(episodios):
    ambiente = tictactoe() # Inicilizaçaõ de um tabuleiro
    agente = Agent() # Criação do agente

    vitorias, empates, derrotas = 0, 0, 0 # Variaveis para mostrar a quantidade de vitorias, empates e derrotas em relação à quantidade de episodios simulados.
    retornos = [] 

    # Simulação de partidas
    for episodio in range(episodios):
        estado = ambiente.reiniciar()
        acao_realizada = False
        retorno = 0

        while not acao_realizada:
            acoes = ambiente.possiveis_acoes()

            if not acoes:
                break 

            acao = agente.escolha_acao(estado, acoes)

            prox_estado, recompensa, acao_realizada = ambiente.step(acao, player=1)

            # Recompensas, depedendo do resultado partida
            if acao_realizada:
                if recompensa == 1:
                    recompensa = 10  # Recompensa positiva quando vence a partida
                    vitorias += 1
                elif recompensa == 0:
                    recompensa = 1  # Recompensa levemente positiva quando vence a partida
                    empates += 1

            if not acao_realizada:
                # Jogadas do oponente(na simulação)
                oponente_acoes = ambiente.possiveis_acoes()
                if oponente_acoes:
                    oponente_acao = random.choice(oponente_acoes)
                    prox_estado, oponente_recompensa, acao_realizada = ambiente.step(oponente_acao, player=2)

                    if oponente_recompensa == 1:
                        recompensa = -10 # Recompensa negativa, caso o agente perde a partida
                        derrotas += 1

            prox_acoes = ambiente.possiveis_acoes()
            # Atualização da q-table
            agente.atualizacao_q_value(estado, acao, recompensa, prox_estado, prox_acoes)

            retorno += recompensa

            estado = prox_estado

        retornos.append(retorno)
    print(f"Vitórias: {vitorias}, Empates: {empates}, Derrotas: {derrotas}")


    return agente
