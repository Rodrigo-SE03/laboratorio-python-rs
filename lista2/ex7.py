salario = float(input("Insira seu salário: "))
if salario < 1000:
    salario = salario * 1.2
elif salario < 1500:
    salario = salario * 1.15
elif salario < 2000:
    salario = salario * 1.1
else:
    salario = salario * 1.05
print(f"Seu novo salário é: {salario}")