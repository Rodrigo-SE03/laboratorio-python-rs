# Faça um código que receba 10 números e retorne esses números em uma lista
# ordenada.

vetor = []
i=0
while i<10:
    vetor.append(int(input('Digite um número: ')))
    i += 1
    
print(f'Lista: {vetor}')
print(f'Lista ordenada: {sorted(vetor)}')