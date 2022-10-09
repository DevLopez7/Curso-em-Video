#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
total = 0

for contador in range(1, num + 1):
    
    if num % contador ==0:
        print('\033[33m', end='')
        total +=1 

    else:
        print('\033[31m', end= '')

    print(f'{contador} ', end='')

print(f'\n\033[mO número {num} foi divisível {total} vezes.')

if total == 2:
    print(f'{num} é PRIMO!')

else:
    print(f'{num} não é PRIMO!') 

#----------DICAS----------
#Um número natural é primo se ele possui apenas dois divisores positivos e distintos.
#Ou seja, um número natural é primo se ele é maior que 1 e é divisível apenas por si próprio e por 1.
#Um exemplo: o número 2. Ele só é divisível por ele mesmo, e por 1.