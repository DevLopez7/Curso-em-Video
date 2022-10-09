#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

num = int(input('Digite um número: '))

print(f'O sucessor de \033[31m [{num}] \033[30m é \033[32m [{num+1}] \033[30m. O antecessor de \033[33m [{num}]\033[30m é \033[34m [{num-1}].')