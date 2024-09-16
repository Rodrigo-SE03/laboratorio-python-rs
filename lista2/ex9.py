a = float(input("Digite o valor de a: "))
if a == 0:
    print("A equação não é do segundo grau.")
    exit()
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
delta = b**2 - 4*a*c
if delta < 0:
    print("A equação não possui raízes reais.")
    exit()
x1 = (-b + delta**0.5) / (2*a)
x2 = (-b - delta**0.5) / (2*a)
print("As raízes da equação são:")
print(f"x1 = {x1}")
print(f"x2 = {x2}")