import random 
from string import digits
from string import punctuation
from string import ascii_letters



def somador_listas(lista):
    total
    for i in lista:
        total = total + i
    
    return total


def geradorSenhas(numero):
    tipos_elementos = str(input('Quais os elementos devo colocar?\n1 - Números\n2 - Caracteres\n3 - Letras\n'))
    symbols = []
    #symbols = ascii_letters + digits + punctuation
    #symbols = digits if 1 and 2 and 3 else 
    if '3' in tipos_elementos:
        symbols.append(ascii_letters)
    if '2' in tipos_elementos:
        symbols.append(punctuation)
    if '1' in tipos_elementos:
        symbols.append(digits)
    else:
        print('Não entendi sua resposta.\nTente novamente!')

    symbols = somador_listas(symbols)
    
    secure_random = random.SystemRandom()
    password = ''.join(secure_random.choice(symbols) for i in range(numero)) 
    print(password)
'''
    

'''




numero_elementos_senha = str(input('Qual a quantidade elementos na senha?\n'))

geradorSenhas(numero_elementos_senha)
