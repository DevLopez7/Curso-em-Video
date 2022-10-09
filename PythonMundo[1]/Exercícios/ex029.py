#Escreva um programa que leia a velocidade de um carro.
#if ele ultrapassar 80km/h., mostre uma mensagem dizendo que ele foi multado. 
#a multa vai custar R$ 7,00 por cada Km acima do limte.

velocidade = float(input('Qual é a velocidade atual do carro? '))

if velocidade > 80:
    print('MULTADO!, Você exedeu o limite permitido que é de 80Km/h')
    
    multa = (velocidade - 80) * 7
    print(f'Você deve pagar uma multa de R${multa}')

print('Tenha um bom dia! Digija com segunça!')

