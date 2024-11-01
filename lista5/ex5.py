# Crie uma função que receba o número do mês e retorne o nome do mês, faça
# isso utilizando uma tupla para guardar e recuperar os nomes dos meses.

def nome_mes(numero):
    meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
             'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
    return meses[numero-1]

numero = int(input('Digite o número do mês: '))
print(f'Mês: {nome_mes(numero)}')