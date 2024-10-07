def count_p(text):
    text = text.split(' ')
    return len(text)

texto = input("Digite o texto: ")
print(f"O texto possui {count_p(texto)} palavras")