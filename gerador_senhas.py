from lib2to3.pygram import Symbols
import random 
from string import digits
from string import punctuation
from string import ascii_letters
from PySimpleGUI import PySimpleGUI as sg


def geradorSenhas(valores):
    numero_elementos_senha = int(valores['numero_elementos'])
    symbols = ascii_letters + digits + punctuation
    secure_random = random.SystemRandom()
    password = "".join(secure_random.choice(symbols) for i in range(numero_elementos_senha)) 
    return password


# Interface Gráfica
sg.theme('Reddit')
layout = [
    [sg.Text('Tamanho da senha'), sg.Input(key='numero_elementos', size=(20,1))],
    [sg.Button('Gerar')]
]

janela = sg.Window('Gerador de senhas', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED: #Caso o usuário saia da aplicação
        break
    if eventos == 'Gerar':
        # Validação de usuários
        senha = geradorSenhas(valores)
        janela['OUTPUT'].update(senha)
