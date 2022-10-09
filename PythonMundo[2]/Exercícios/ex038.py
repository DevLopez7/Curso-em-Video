#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: 
#O primeiro valor é maior 
#O segundo valor é maior
# Não existe valor maior, os dois são iguais

n1 = int(input('Digite um número inteiro: ')) 

n2 = int(input('Digite outro número inteiro: '))

if n1 > n2:
    print(f'O {n1} é o maior')


elif n2 > n1:
    print(f'O {n2} é o maior') 

elif n1 == n2:
    print('Não existe valor maior, os dois números são iguais!')

else: 
    print('Opção inválida. Tente novamente.')