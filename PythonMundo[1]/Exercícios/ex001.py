#Crie um programa que escreva "Olá, Mundo !' na tela. 

nome = 'Lucas Lopes!'

cores = {'limpa':'\033[m',
         'azul':'\033[34m', 
         'amarelo':'\033[33m', 
         'pretoebranco':'\033[7;30m'}

print('{} {} {}'.format(cores['amarelo'], nome, cores['limpa']))