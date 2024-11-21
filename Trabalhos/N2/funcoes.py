import random

def mostrar_tabuleiro(tabuleiro):
    linhas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    # linhas = ['1','2','3','4','5','6','7','8','9','10']
    print('  1 2 3 4 5 6 7 8 9 10')
    for i in range(0, 10):
        print(linhas[i], end=' ')
        for j in range(0, 10):
            print(tabuleiro[i][j], end=' ')
        print()

def posicionar_barcos(tabuleiro, barcos):
    for barco, tamanho in barcos.items():
        coincidente = True
        print('Posicione o', barco)  # Para debug do código
        orientacao = random.choice(['v', 'h'])
        if orientacao == 'v':
            while coincidente == True:
                x = random.randint(0, 9)
                y = random.randint(0, 9 - tamanho)
                for i in range(0, tamanho):
                    if tabuleiro[y + i][x] == 1:
                        coincidente = True
                    else:
                        coincidente = False
                if coincidente == False:
                    for i in range(0, tamanho):
                        tabuleiro[y + i][x] = 1
        else:
            while coincidente == True:
                x = random.randint(0, 9 - tamanho)
                y = random.randint(0, 9)
                for i in range(0, tamanho):
                    if tabuleiro[y][x + i] == 1:
                        coincidente = True
                    else:
                        coincidente = False
                if coincidente == False:
                    for i in range(0, tamanho):
                        tabuleiro[y][x + i] = 1
    return tabuleiro