import math

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
    
    area = math.pi * float(raio) ** 2
    print("A área é: ", area)

def q4 () :
    tempC = input("Digite a temperatura em Celsius: ")
    tempF = (float(tempC) * 1.8) + 32
    print("A temperatura em Fahrenheit é: ", tempF)

def q5 () :
    tempF = input("Digite a temperatura em Fahrenheit: ")
    tempC = (float(tempF) - 32) * 5/9
    print("A temperatura em Celsius é: ", tempC)

q3()