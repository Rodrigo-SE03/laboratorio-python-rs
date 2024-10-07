def count_v(text):
    cont = 0
    for c in text:
        if c in "aeiou":
            cont += 1
    return cont

texto = input("Digite o texto: ")
print(f"O texto possui {count_v(texto)} vogais")