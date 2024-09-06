def q1 () :
    nome = input("Digite seu nome: ")
    print("Olá, ", nome)

def q2 () :
    altura = input("Digite a altura: ")
    largura = input("Digite a largura: ")
    area = float(altura) * float(largura)
    print("A área é: ", area)

def q3 () :
    raio = input("Digite o raio: ")
    
    area = 3.14 * float(raio) ** 2
    print("A área é: ", area)

def q4 () :
    tempC = input("Digite a temperatura em Celsius: ")
    tempF = (float(tempC) * 1.8) + 32
    print("A temperatura em Fahrenheit é: ", tempF)

def q5 () :
    tempF = input("Digite a temperatura em Fahrenheit: ")
    tempC = (float(tempF) - 32) * 5/9
    print("A temperatura em Celsius é: ", tempC)

def q6() :
    dias = input("Digite a quantidade de dias: ")
    segundos = int(dias) * 24 * 60 * 60
    print("A quantidade de segundos é: ", segundos)

def q7() : 
    a = input("Digite o valor de a: ")
    b = input("Digite o valor de b: ")
    c = input("Digite o valor de c: ")
    delta = float(b) ** 2 - 4 * float(a) * float(c)
    x1 = (-float(b) + (delta**0.5)) / (2 * float(a))
    x2 = (-float(b) - (delta**0.5)) / (2 * float(a))
    print("As raízes são: ", x1, " e ", x2)

def q8() :
    n1 = input("Digite a primeira nota: ")
    n2 = input("Digite a segunda nota: ")
    n3 = input("Digite a terceira nota: ")
    n4 = input("Digite a quarta nota: ")
    media = (float(n1) + float(n2) + float(n3) + float(n4)) / 4
    print("A média é: ", media)

def q9() :
    salario = input("Digite o salário bruto: ")
    liquido = float(salario) - (float(salario) * (0.12) + float(salario) * (0.08) + float(salario) * (0.05))
    print("O salário líquido é: ", liquido)

def q10() :
    peso = input("Digite o peso: ")
    altura = input("Digite a altura: ")
    imc = float(peso)/(float(altura)**2)
    print("O IMC é: ", imc)
