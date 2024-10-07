def fibo(num):
    fib=1
    prev1=1
    prev2=1
    for i in range(num-2):
        fib = prev1+prev2
        prev1 = prev2
        prev2 = fib
    return fib

num = int(input("Digite a quantidade de termos da sequência: "))    
print(fibo(num))