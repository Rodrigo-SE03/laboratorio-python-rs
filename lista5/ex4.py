# Crie um código que receba nome e telefone de uma lista de contatos, até que
# receba -1, então imprima a lista com os nomes e telefones dos contatos.

contatos = {}
while True:
    nome = input('Digite o nome do contato: ')
    if nome == '-1':
        break
    telefone = input('Digite o telefone do contato: ')
    contatos[nome] = telefone

print('\nLista de contatos:')
for nome, telefone in contatos.items():
    print(f'{nome}: {telefone}')