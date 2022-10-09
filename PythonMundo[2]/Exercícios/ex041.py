#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a sua idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JUNIOR
#Até 20 anos: SÊNIOR 
#Acima: MASTER

from datetime import date

atual = date.today().year

nasc = int(input('Ano de nascimento do atleta: '))

idade = atual - nasc

if idade <= 9:
    print(f'idade = {idade} \ncategoria = MIRIM')

elif idade <= 14:
    print(f'idade = {idade} \ncategoria = INFANTIL')

elif idade <= 19:
    print(f'idade = {idade} \ncategoria = JUNIOR')

elif idade == 20:
    print(f'idade = {idade} \ncategoria = SÊNIOR')

else:
    idade > 20
    print(f'idade = {idade} \ncategoria = MASTER')


