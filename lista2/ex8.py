custo_hora = float(input("Insira o custo da hora: "))
horas = float(input("Insira a quantidade de horas trabalhadas: "))
salario = custo_hora * horas
desconto = 0
if salario < 1500:
    pass
elif salario < 1800:
    desconto = 0.05
elif salario < 2500:
    desconto = 0.1
elif salario < 3000:
    desconto = 0.2
else:
    desconto = 1

print(f"Salário bruto: {salario}")
print(f"Desconto: {desconto}")
print(f"Salário líquido: {salario - salario * desconto}")