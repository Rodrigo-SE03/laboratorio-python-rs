# Faça um código que receba 10 números e retorne uma lista com os números
# sem repetição. Exemplo:
# Entrada: 1 1 2 3 5 5
# Saída: 1 2 3 5


vetor = []
i=0
while i<10:
    vetor.append(int(input('Digite um número: ')))
    i += 1
print(f'Lista com repetições: {vetor}')
print(f'Lista sem repetições: {list(set(vetor))}')