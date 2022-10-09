#Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre (quantas pessoas ainda não atingiram a maioridade) e (quantas já são maiores).

from datetime import date #importar o módulo que puxa a data atual do sistema.
from os import system as terminal #importar o módulo que limpa o terminal.

terminal('clear')

atual = date.today().year #pegar o ano atual do dispositivo.

totalmaiores = 0 #variável para armazenar os valores de pessoas que são maiores de idade.
totalmenores = 0 #variável para armazenar os valores de pessoas que são menores de idade.

for pessoas in range(1, 8): #repetir o código abaixo num range de 1 a 7.
    
    nasc = int(input(f'Em que ano a {pessoas}ª pessoa nasceu? ')) #coletar as datas de nascimento.
    
    terminal('clear') #limpar o terminal a cada data informada.
    
    idade = atual - nasc #calcular a idade da pessoa de acordo com a data de nascimento digitada.

    if idade >= 21: #se tiver 21 ou + a pessoa será maior de idade então entrará +1 valor na variável "totalmaiores".
        totalmaiores += 1 
        

    else: #se não tiver 21 ou + a pessoa será menor de idade então entrará +1 valor na variável "totalmenores".
        totalmenores += 1 

print(f'Ao todo tivemos {totalmaiores} pessoas maiores de idade!') #printar quantas pessoas são maiores de idade.   
print(f'E também tivemos {totalmenores} pessoas menores de idade!') #printar quantas pessoas são menores de idade.


