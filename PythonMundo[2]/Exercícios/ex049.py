#Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço FOR.

import os

num = int(input('Digite um número para ver sua tabuada: '))

os.system('clear')

print(f'\033[32m     TABUADA DO {num}')

print('-='*11)

for tabuada in range(1, 11):
    print(f'{num}x{tabuada:2} = {num*tabuada}')

print('-='*11)
 