def count_p(text):
    if text == text[::-1]:
        return 'é um palíndromo'
    else:
        return 'não é um palíndromo'

texto = input("Digite a palavra ou frase: ")
print(f"O texto {count_p(texto)}")