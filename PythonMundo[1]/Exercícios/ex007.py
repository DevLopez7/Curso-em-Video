#Desenvolva um programa que leia as duas notas de um aluno , calcule e mostre a sua média.

nota1 = float(input('\033[31m digite a primeira nota: '))

nota2 = float(input('\033[32m digite a segunda nota: '))

media = (nota1+nota2)/2

print(f'a média do aluno é {media:.1f}')