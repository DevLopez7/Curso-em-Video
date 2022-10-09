#Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 a 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
import time

computador = randint (0, 5) #Faz o computador "PENSAR"

print('-=-' *20)
print('Vou pensar em um número entre 0 a 5. Tente advinhar...')
print('-=-' *20)

jogador = int(input('Em que número eu pensei? '))

print('PROCESSANDO...')

time.sleep(3)

if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
    
else: 
    print(f'GANHEI!, Eu pensei no número {computador} e não no {jogador}!')
