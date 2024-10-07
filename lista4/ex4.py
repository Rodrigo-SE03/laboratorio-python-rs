def find_l(text,l):
    try:
        return text.index(l)
    except:
        return "O texto não possui essa letra"

texto = input("Digite o texto: ")
letra = input("Digite a letra que deseja encontrar: ")
print(f"A letra '{letra}' está na posição: ",find_l(texto,letra))