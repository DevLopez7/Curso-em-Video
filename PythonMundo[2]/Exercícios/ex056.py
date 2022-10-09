#Desenvolva um programa que leia o nome, idade, sexo de 4 pessoas. No final do programa mostre:
#A média da idade do grupo.
#Qual é o nome do homem mais velho.
#Quantas mulheres tem menos de 20 anos.

soma_idade = 0
média_idade = 0
maior_idade_M = 0
nome_maisvelho = ''
total_mulheres20 = 0

for dados in range(1, 5):
    
    print(f'-=-=- {dados}ª PESSOA -=-=-')

    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M]\[F]: ')).strip()

    soma_idade += idade
    
    if dados == 1 and sexo in 'Mm':
        
        maior_idade_M = idade
        nome_maisvelho = nome 
    
    if sexo in 'Mm' and idade > maior_idade_M:
        
        maior_idade_M = idade
        nome_maisvelho = nome 
    
    if sexo in 'Ff' and idade < 20:
        
        total_mulheres20 += 1

média_idade = soma_idade / 4

print(f'A média de idade do grupo é {média_idade} anos')
print(f'O homem mais velho tem {maior_idade_M} anos e se chama {nome_maisvelho}')
print(f'Ao todo são {total_mulheres20} mulheres com menos de 20 anos')
