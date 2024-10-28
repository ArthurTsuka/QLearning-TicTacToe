import numpy as np

class tictactoe:
    def __init__(self):
        #Inicialização do tabuleiro
        self.tabuleiro = np.zeros((3, 3), dtype=int)

    
    def reiniciar(self):
        # Função para reiniciar o tabuleiro/jogo
        self.tabuleiro = np.zeros((3, 3), dtype=int)

        return self.get_estado()

    def get_estado(self):
        # Estado do tabuleiro
        return tuple(self.tabuleiro.reshape(-1))
    
    # Lista com todas as ações disponiveis no momento.
    def possiveis_acoes(self):
        acoes = []
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i, j] == 0:
                    acoes.append((i, j))
        return acoes
    
    # Responsavel pela execucao de uma jogada
    def step(self, acao, player):
        if self.tabuleiro[acao] == 0:
            self.tabuleiro[acao] = player
            recompensa, movimento_realizado = self.verificacao_ganhador(player)
            return self.get_estado, recompensa, movimento_realizado
        else:
            return self.get_estado, -3, True
    
    # Todas as verificações (vitoria, empate, derrota)
    def verificacao_ganhador(self, player):
        for i in range(3):
            if all(self.tabuleiro[i][j] == player for j in range(3)):
                return 1, True  # Vitória na linha

        # Verifica colunas
        for j in range(3):
            if all(self.tabuleiro[i][j] == player for i in range(3)):
                return 1, True 

        # Verifica diagonal principal
        if all(self.tabuleiro[i][i] == player for i in range(3)):
            return 1, True

        # Verifica diagonal secundária
        if all(self.tabuleiro[i][2 - i] == player for i in range(3)):
            return 1, True

        # Verifica se o tabuleiro está cheio (empate)
        if all(self.tabuleiro[i][j] != 0 for i in range(3) for j in range(3)):
            return 0, True  # Empate

        return 0, False  

    # Renderizacao e criação do formato do tabuleiro no terminal
    def tabuleiro_renderizado(self):
        symbols = {0: " ", 1: "X", 2: "O"}
        print("\nTabuleiro atual:")
        for row in self.tabuleiro:
            print(" | ".join(symbols[cell] for cell in row))
            print("-" * 5)
