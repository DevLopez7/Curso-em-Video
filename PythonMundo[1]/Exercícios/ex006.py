#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('digite um número: '))

print(f'\033[35m [O dobro do número é {n*2}]\n \033[32m [O triplo é {n*3}]\n \033[31m [A raiz quadrada é {n**1/2:.2f}]')