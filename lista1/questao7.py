a = input("Digite o valor de a: ")
b = input("Digite o valor de b: ")
c = input("Digite o valor de c: ")
delta = float(b) ** 2 - 4 * float(a) * float(c)
x1 = (-float(b) + (delta**0.5)) / (2 * float(a))
x2 = (-float(b) - (delta**0.5)) / (2 * float(a))
print("As raízes são: ", x1, " e ", x2)