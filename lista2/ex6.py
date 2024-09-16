l1 = float(input("Digite o tamanho do primeiro lado: "))
l2 = float(input("Digite o tamanho do segundo lado: "))
l3 = float(input("Digite o tamanho do terceiro lado: "))
if (l1+l2)>l3 and (l2+l3)>l1 and (l3+l1)>l2:
    if l1 == l2 and l2 == l3:
        print("Triângulo equilátero")
    elif l1 == l2 or l2 == l3 or l3 == l1:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
else:
    print("Essas dimensões não formam um triângulo")