import random
def jogar(n):
    resultados = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0}
    for i in range(0,n):
        resultados[str(random.randint(1,6))] += 1
    return resultados

n = int(input('Digite um número (natural): '))
print(f'O resultado de {n} lançamentos de um dado é:')
for k,v in jogar(n).items():
    print(f'{k}: {v}')