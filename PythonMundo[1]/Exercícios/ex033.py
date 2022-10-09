#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
#Verificar quem é o menor

num1 = int(input('Primeiro valor: '))

num2 = int(input('Segundo valor: '))

num3 = int(input('Terceiro valor: '))

maior = num1

if num2 > num1 and num2 > num3:
    maior = num2

if num3 > num1 and num3 > num2:
    maior = num3
menor = num1

if num2 < num3 and num2 < num1:
    menor = num2

if num3 < num2 and num3 < num1:
    menor = num3
    
print(f"O menor número digitado foi {menor}")
print(f"O maior número digitado foi {maior}")
