import os

opcoes = {
    '1':'Binário para Decimal',
    '2':'Binário para Hexadecimal',
    '3':'Decimal para Binário',
    '4':'Decimal para Hexadecimal',
    '5':'Hexadecimal para Binário',
    '6':'Hexadecimal para Decimal',
    '7':'Sair'
    }
running = True

def bin_dec():
    num = input('Digite o número em Binário: ')
    for n in range(2,10):
        if str(n) in num:
            return "Valor inválido"
    cont = 0
    dec = 0
    for d in num[::-1]:
        dec += int(d)*2**cont
        cont+=1
    return f'\nBinário: {num}\nDecimal: {dec}'

def bin_hex():
    num = input('Digite o número em Binário: ')
    for n in range(2,10):
        if str(n) in num:
            return "Valor inválido"
    cont = 0
    dec = 0
    for d in num[::-1]:
        dec += int(d)*2**cont
        cont+=1
    hexa = ''
    while True:
        print(dec)
        hexa += hex_table(dec%16,1)
        dec = dec // 16
        if dec < 16:
            if dec != 0:
                hexa += hex_table(dec,1)
            break
    hexa = hexa[::-1]
    return f'\nBinário: {num}\nHexadecimal: {hexa}'

def dec_bin():
    num = int(input('Digite o número em Decimal: '))
    binario = ''
    while True:
        binario += str(num%2)
        num = num // 2
        if num < 2:
            if num != 0:
                binario += str(num)
            break
    binario = binario[::-1]
    return f'\nDecimal: {num}\nBinário: {binario}'

def dec_hex():
    num = int(input('Digite o número em Decimal: '))
    dec = num
    hexa = ''
    while True:
        print(dec)
        hexa += hex_table(dec%16,1)
        dec = dec // 16
        if dec < 16:
            if dec != 0:
                hexa += hex_table(dec,1)
            break
    hexa = hexa[::-1]
    return f'\nDecimal: {num}\nHexadecimal: {hexa}'

def hex_bin():
    num = input('Digite o número em Hexadecimal: ')
    dec = 0
    cont = 0
    for d in num[::-1]:
        dec += int(hex_table(d,0))*16**cont
        cont+=1
    binario = ''
    while True:
        binario += str(dec%2)
        dec = dec // 2
        if dec < 2:
            if dec != 0:
                binario += str(dec)
            break
    binario = binario[::-1]
    return f'\nHexadecimal: {num}\nBinário: {binario}'

def hex_dec():
    num = input('Digite o número em Hexadecimal: ')
    dec = 0
    cont = 0
    for d in num[::-1]:
        dec += int(hex_table(d,0))*16**cont
        cont+=1
    return f'\nHexadecimal: {num}\nDecimal: {dec}'

def hex_table(d,op):
    d = str(d)
    hex_map = {
        '0':'0',
        '1':'1',
        '2':'2',
        '3':'3',
        '4':'4',
        '5':'5',
        '6':'6',
        '7':'7',
        '8':'8',
        '9':'9',
        '10':'A',
        '11':'B',
        '12':'C',
        '13':'D',
        '14':'E',
        '15':'F'
    }
    if op == 1:
        return hex_map[d]
    else:
        for key,value in hex_map.items():
            if d == value:
                return key

    
def operate(op):
    resp = 0
    match op:
        case 1: 
            resp = bin_dec()
        case 2:
            resp = bin_hex()
        case 3:
            resp = dec_bin()
        case 4:
            resp = dec_hex()
        case 5:
            resp = hex_bin()
        case 6:
            resp = hex_dec()
    return resp

def mostrar_menu():
    for key,value in opcoes.items():
        print(f'{key}. {value}')

while running:
    mostrar_menu()
    try:
        operacao = int(input('\n'))
    except:
        print('\nValor inválido. Digite um número de 1 a 7.')
        continue
    if operacao == 7:
        break
    elif operacao > 7 or operacao < 1:
        print('\nValor inválido. Digite um número de 1 a 7.')
        continue
    else:
        resultado = operate(operacao)

    print('\n  ',resultado)