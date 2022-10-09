#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou íMPAR.

num =int(input('Me diga um número qualquer: '))

if (num %2) == 0:
        print(f'O{num} é um número par')
else:
        print(f'O{num} é um número ímpar')
