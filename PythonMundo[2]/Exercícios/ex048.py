#Faça um programa que calcule a soma de todos os números impares que são multiplos de 3 e que se encontram no intervalo de 1 até 500.

soma = 0

cont = 0

for valores in range(1, 501, 2):
    if valores % 3 == 0:
        cont = cont + 1
        soma = soma + valores

print(f'A de {cont} valores solicitdos é {soma}')

