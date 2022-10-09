# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

num = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para converção:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')

opção = int(input('Sua opção: '))

if opção == 1:
    print(f'{num} convertido para BINARIO = [{bin(num)[2:]}]')

elif opção == 2:
    print(f'{num} convertido para OCTAL = [{oct(num)[2:]}]')

elif opção == 3:
    print(f'{num} convertido para HEXADECIMAL = [{hex(num)[2:]}]')
    
else:
    print('Opção inválida. Tente novamente.')
