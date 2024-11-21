import random
from funcoes import mostrar_tabuleiro, posicionar_barcos
import os

# -------Configuração do tabuleiro-------
tabuleiro_inimigo = [[]]
tabuleiro_visivel = [[]]
linhas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
# linhas = ['1','2','3','4','5','6','7','8','9','10']
for i in range(0,10):
    tabuleiro_inimigo.append([])
    tabuleiro_visivel.append([])
    for j in range(0,10):
        tabuleiro_inimigo[i].append(0)
        tabuleiro_visivel[i].append("~")
tabuleiro_inimigo.pop()
tabuleiro_visivel.pop()
# ---------------------------------------

# -------Definição das embarcações-------
barcos = {
    "porta_avioes": 5,
    "navio_de_guerra": 4,
    "submarino": 3,
    "contratorpedeiro": 3,
    "patruha": 2
}
total = 0
for barco in barcos:
    total += barcos[barco]

tabuleiro_inimigo = posicionar_barcos(tabuleiro_inimigo, barcos)
# ---------------------------------------



# -------Loop principal do jogo-------
invalido = False
acerto = False
start = 0
hits = [[]]
while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    # ------Usar para tomar spoiler----------
    mostrar_tabuleiro(tabuleiro_inimigo)
    print('--------------------------------')
    print(total)
    # ---------------------------------------
    
    if invalido:
        print("Coordenada inválida!")
        invalido = False
    elif acerto:
        print("Acertou!")
        acerto = False
    elif acerto == False and start != 0:
        print("Errou!")
    start = 1

    mostrar_tabuleiro(tabuleiro_visivel)

    tiro = input("Digite a coordenada do tiro (ex: A1): ")
    tiro = tiro.replace(" ", "")
    try:
        y = tiro[0].upper()
        x = int(tiro[1:]) - 1
    except:
        invalido = True
        continue
    if x>10 or x<0 or y not in linhas:
        invalido = True
        continue
    y = linhas.index(y)
    if [y,x] in hits:
        invalido = True
        continue
    elif tabuleiro_inimigo[y][x] == 1:
        tabuleiro_visivel[y][x] = "X"
        hits.append([y,x])
        total -= 1
        acerto = True
    else:
        tabuleiro_visivel[y][x] = "O"

    if total == 0:
        print("Todas as embarcações foram afundadas!")
        mostrar_tabuleiro(tabuleiro_visivel)
        print("Você venceu!")
        break
# ---------------------------------------