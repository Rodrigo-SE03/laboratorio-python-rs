# Faça uma função que receba dois conjuntos e devolva a intersecção entre os
# dois, exemplo:
# conjunto1 = {1, 2, 3}
# conjunto2 = {2, 3, 4}
# resultado = {2, 3}

def interseccao(conjunto1, conjunto2):
    return conjunto1 & conjunto2

conjunto1 = {1, 2, 3}
conjunto2 = {2, 3, 4}
print(interseccao(conjunto1, conjunto2))