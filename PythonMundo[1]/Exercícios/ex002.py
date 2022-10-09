#Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

nome = input('Digite seu nome: ')

cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',}

print('Seja bem-vindo, {} {}{}!'.format(cores['vermelho'], nome, cores['limpa']))