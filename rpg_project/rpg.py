# RPG Supporting System

from curses.ascii import isalpha

# Variaveis:
#Nome do jogo
game = ""  
#Quantidade de jogadores
playerNumber = 0   
#Lista de players
playerNames = []


def main()


def intro()

    # introdução
    print("Olá! Vamos jogar um jogo?")
    
    # Nome do jogo
    game = input("Qual jogo estamos jogando? ")
    print("Legal, então vamos jogar " + game)

    # Personagens
    while True:
        playerNumber = int(input("Qual a quantidade de jogadores?"))
        if playerNumber > 0 and playerNumber =< 6:
            break
        else:
            print("No máximo 6 jogadores. Tente de novo.")
                
    # Nome dos personagens
    print("Hora de definir o nome dos personagens!")
    for player in range(playerNumber):
        while True:
            p = input("Qual o nome do personagem " + (player +1))
            confirm = input("Confirma o nome: " + p + "(Sim/Nao)")
            if confirm[0].lower() == 's':
                playerNames.append(p)
                break
    
