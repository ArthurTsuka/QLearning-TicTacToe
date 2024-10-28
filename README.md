#TicTacToe - Reinforcement Learning

Este projeto implementa um agente de Q-Learning para jogar Tic Tac Toe (Jogo da Velha). Utilizando um algoritmo de aprendizado por reforço, o agente é treinado para aprender estratégias de jogo que maximizam suas chances de vitória contra um oponente

## Instalação

1. Clone o Repositório
```
git clone https://github.com/ArthurTsuka/QLearning-TicTacToe.git
```

2. Instale as depedencias

```
pip install -r requirements.txt
```
3.

```
python ./main.py
```

## Estrutura do Projeto

```src/```: Contém os principais arquivos do projeto, incluindo o ambiente, o agente e a lógica de treinamento.
```ambiente.py```: Implementa a lógica do jogo Tic Tac Toe, incluindo as regras, verificação de vitória e controle do tabuleiro.
```agente.py```: Implementa o agente de Q-Learning e as funções de escolha de ação e atualização da Q-Table.
```train.py```: Contém a função de treinamento, que simula milhares de jogos para ensinar o agente.
```main.py```: Arquivo principal para treinar o agente e permitir que o usuário jogue contra ele