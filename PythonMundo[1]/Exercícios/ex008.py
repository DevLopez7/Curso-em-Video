#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Digite um valor: '))

c = m*100

mm = m*1000

print(f'[{m}metros] é igual a {c}centímetros. [{c}centímetros] é igual a {mm}milímetros.')