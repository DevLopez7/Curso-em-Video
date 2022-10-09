#Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1: nome com todas as letras maiúsculas.
# 2: nome com todas as letras minúsculas.
# 3: Quantas letras ao todo (sem considerar os espaços).
# 4: Quantas letras tem o primeiro nome.

import os

# Passo 1: coletar o nome do usúario.
nome = str(input('Qual é o seu nome completo? '))

os.system('cls')

print('Analisando seu nome...')

# Passo 2: mostrar o nome com todas as letras maiúsculas.
print(f'nome completo em maiúculo: ',nome.upper())

# Passo 3: mostrar o nome com todas as letras minúsculas.
print(f'nome completo em minúsculo: ',nome.lower())

# Passo 4: mostrar quantas letras tem ao todo sem os espaços.
nome100space = nome.replace(' ', '')

print(f'nome completo contém: {len(nome100space)} letras')

# Passo 5: mostrar quantas letras tem o primeiro nome.
primeironome = nome.split()[0]

print(f'Seu primeiro nome é {primeironome} e ele tem {len(primeironome)} letras') 