import random 
from string import digits
from string import punctuation
from string import ascii_letters

symbols = ascii_letters + digits + punctuation
print(symbols)

def geradorSenhas(numero):
    #symbols = ascii_letters + digits + punctuation
    symbols = []
    symbolsnew = saberChar(symbols)
    secure_random = random.SystemRandom()
    password = ''.join(secure_random.choice(symbolsnew) for i in range(numero)) 
    print(password)



def saberChar(symbolsParams):
    tipos_elementos = str(input('Quais os elementos devo colocar?\n1 - Números\n2 - Caracteres\n3 - Letras\n'))
    
    if '3' in tipos_elementos:
        symbolsParams.append(ascii_letters)
    if '2' in tipos_elementos:
        symbolsParams.append(punctuation)
    if '1' in tipos_elementos:
        symbolsParams.append(digits)
    else:
        print('Não entendi sua resposta.\nTente novamente!')
    return ''.join(symbolsParams)



numero_elementos_senha = int(input('Qual a quantidade elementos na senha?\n'))

geradorSenhas(numero_elementos_senha)
