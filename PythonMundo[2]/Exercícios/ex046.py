#Faça um programa que mostre na tela uma contagem regressiva para a explosão de uma BOMBA, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

import os
from time import sleep as segundos

os.system('clear')

print('[BOMBA ATIVADA!]')

for contagem in range(10, -1, -1):
    segundos(1)
    print(contagem)

print('\033[31mBOOOOMMMM!!!!')
