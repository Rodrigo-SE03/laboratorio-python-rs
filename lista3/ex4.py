num = int(input("Digite a quantidade de termos da sequência: "))
fib=1
prev1=1
prev2=1
for i in range(num-2):
    fib = prev1+prev2
    prev1 = prev2
    prev2 = fib
    
print(fib)
