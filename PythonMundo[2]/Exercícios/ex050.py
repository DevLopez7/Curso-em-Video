#Desenvolva um programa que (leia seis números inteiros) e (mostre a soma apenas daqueles que forem pares), Se o valor digitado for ímpar, desconsidere-o.

import os
os.system('clear')

soma = 0
cont = 0

for c in range(1, 7):

#for para repetir o código abaixo
#_________________________________________________   
    num = int(input(f'Digite o {c} valor: '))
    if num % 2 == 0: #somar apenas os números pares e dizer quantos pares foi informado.
        cont += 1
        soma += num
#___________________________________________________

print(f'Você informou {cont} valores (pares) e a soma foi {soma}.')

# -=-=-=-=-=-=-=-=-=-=-=-=DICAS-=-=-=-=-=-=-=-=-=-=-=-= 
# soma = 1
# soma = 2
# soma = 3
# soma = soma + 2 #O python interpretara de cima para baixo, a variável "soma" válida sempre será a última declarada, ou seja, o resultado seria 5.