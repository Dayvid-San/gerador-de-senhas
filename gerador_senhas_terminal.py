import random 
from string import digits
from string import punctuation
from string import ascii_letters


tipos_elementos = str(input('Quais os elementos devo colocar?\n1 - Números\n2 - Caracteres\n3 - Letras\n'))
numero_elementos_senha = str(input('Qual a quantidade elementos na senha?\n'))



def geradorSenhas(numero):
    #symbols = ascii_letters + digits + punctuation
    #symbols = digits if 1 and 2 and 3 else 
    if '3' in tipos_elementos:
        symbols += ascii_letters
    if '2' in tipos_elementos:
        symbols += punctuation
    if '1' in tipos_elementos:
        symbols += digits

    
    secure_random = random.SystemRandom()
    password = "".join(secure_random.choice(symbols) for i in range(numero)) 
    print(password)

geradorSenhas(numero_elementos_senha)
