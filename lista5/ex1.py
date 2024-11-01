# Faça uma função que receba um vetor de 10 posições e devolva 2 vetores, um
# com os números pares e outro com os números impares.

def separa_pares_impares(vetor):
    pares = []
    impares = []
    for i in vetor:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    return pares, impares

vetor = []
i=0
while i<10:
    vetor.append(int(input('Digite um número: ')))
    i += 1
pares, impares = separa_pares_impares(vetor)
print(f'Pares: {pares}')
print(f'Impares: {impares}')