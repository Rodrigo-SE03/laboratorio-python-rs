peso = float(input('Informe seu peso: ').replace(',','.'))
altura = float(input('Informe sua altura em metros: ').replace(',','.'))

imc = peso/(altura**2)
classificacao = ''
if imc < 18.5:
    classificacao = 'Baixo peso'
elif imc <= 24.9:
    classificacao = 'Peso normal'
elif imc <= 29.9:
    classificacao = 'Excesso de peso'
elif imc < 35:
    classificacao = 'Obesidade'
else:
    classificacao = 'Obesidade extrema'
print('Seu imc é de ',imc)
print(classificacao)