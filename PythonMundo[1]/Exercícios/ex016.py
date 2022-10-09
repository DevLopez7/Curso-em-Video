#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
#exemplo: digite um número: 6.127, o número 6.127 tem a parte inteira 6

from math import trunc

num = float(input('digite um número: '))

print('\033[34m O número {} tem a parte inteira {}'.format(num, trunc(num)))

num = float(input('digite um número: '))

print('\033[32m O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))