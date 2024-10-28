from src.ambiente import tictactoe
from src.agente import Agent
from src.train import train_agente

def jogar_contra_agente(agente, ambiente):
    estado = ambiente.reiniciar()
    jogo_terminado = False

    print("Bem-vindo ao Tic Tac Toe!")
    print("Você é o jogador 'O' (2) e o agente é o 'X' (1).")

    # Ações do Agente(ele começa jogando)
    acoes = ambiente.possiveis_acoes()
    acao_agente = agente.escolha_acao(estado, acoes)
    estado, _, jogo_terminado = ambiente.step(acao_agente, player=1)

    while not jogo_terminado:
        # Renderiza o tabuleiro atual
        ambiente.tabuleiro_renderizado()

        # Jogada do usuário
        acoes = ambiente.possiveis_acoes()
        print("\nSuas ações possíveis:", acoes)
        try:
            acao = input("Escolha sua ação (ex: '0 1' para linha 0, coluna 1): ")
            linha, coluna = map(int, acao.split())

            if (linha, coluna) not in acoes:
                print("Ação inválida! Tente novamente.")
                continue
            
            # Ação escolhida pelo o jogador humano
            estado, _, jogo_terminado = ambiente.step((linha, coluna), player=2)

            #Verificação
            if ambiente.verificacao_ganhador(2)[0] == 1:
                ambiente.tabuleiro_renderizado()
                print("Você venceu!")
                break

        except ValueError:
            continue

        acoes = ambiente.possiveis_acoes()
        acao_agente = agente.escolha_acao(estado, acoes)
        estado, _, jogo_terminado = ambiente.step(acao_agente, player=1)

        #Verificação
        if ambiente.verificacao_ganhador(1)[0] == 1:
            ambiente.tabuleiro_renderizado()
            print("O agente venceu!")
            break
        #Verificação
        if not ambiente.possiveis_acoes():
            ambiente.tabuleiro_renderizado()
            print("Empate!")
            break

def main():
    # Treinamento do agente com 100 mil episodios
    agente = train_agente(episodios=100000)
    # Criação do tabuleiro
    ambiente = tictactoe()

    while True:
        print("\nEscolha uma opção:")
        print("1. Jogar contra o agente")
        print("2. Sair")
        escolha = input("Opção: ")

        if escolha == "1":
            jogar_contra_agente(agente, ambiente)
        elif escolha == "2":
            print("Saindo do jogo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
