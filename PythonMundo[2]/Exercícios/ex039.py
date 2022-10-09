#Faça um programa que leia o ano de nascimento de um jovem e informe. de acordo com a sua idade:
#Se ele ainda vai se alistar ao serviço militar.
#Se é a hora de se alistar 
#Se já passou do tempo de alistamento.
#Seu programa também deverá também mostrar o tempo que falta ou que passsou do prazo. 

from datetime import date

atual = date.today().year

print('''Escolha seu sexo digitando o número:
[1] para FEMININO
[2] para MASCULINO''')

sexo = int(input('Sua opção: '))

if sexo == 1:
    print('Mulheres não precisam fazer alistamento militar obrigatório.')

elif sexo ==2:
    nasc = int(input('Ano de nascimento: '))
    idade = atual - nasc
    print(f'Você nasceu em {nasc} e tem {idade} anos em {atual}. ')

    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    
    elif idade < 18:
        saldo = 18 -idade 
        print(f'Ainda faltam {saldo} anos para o alistamento.')
        ano = idade + atual
        print(f'Seu alistamento será em {ano}.')
    
    elif idade > 18:
        saldo = idade - 18
        print(f'Você já deveria ter se alistado há {saldo} ano(s).')
        ano = atual - saldo
        print(f'Seu alistamento foi em {ano}.')

else:
    print('Opção inválida. Tente novamente.')
