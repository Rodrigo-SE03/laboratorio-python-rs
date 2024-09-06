salario = input("Digite o salário bruto: ")
liquido = float(salario) - (float(salario) * (0.12) + float(salario) * (0.08) + float(salario) * (0.05))
print("O salário líquido é: ", liquido)