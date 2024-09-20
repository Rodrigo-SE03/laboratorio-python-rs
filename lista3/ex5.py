num = int(input("Digite um número: "))
sum = 0
cont = 0
val= ''
while True:
    sum+=num
    num = input("Digite um número para continuar ou 'fim' para parar: ")
    cont+=1
    if num == 'fim':
        break
    else:
        num = int(num)
    

print(sum/cont)