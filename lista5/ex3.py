# Crie uma função que receba uma matriz 3x3 e devolva a soma de todos os
# elementos da matriz.

def soma_matriz(matriz):
    soma = 0
    for linha in matriz:
        for elemento in linha:
            soma += elemento
    return soma

matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f'Digite o elemento ({i}, {j}): ')))
    matriz.append(linha)

print(f'Soma da matriz: {soma_matriz(matriz)}')