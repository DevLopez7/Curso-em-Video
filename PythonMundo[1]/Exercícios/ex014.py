#Escreva um programa que converta uma temperatura em º C e converta para º F.

celsius = float(input('Digite um valor ºC: '))

fahrenheit = (celsius * 9/5) + 32 

print(f'\033[34m{celsius}Cº convertido para Fº = {fahrenheit}')