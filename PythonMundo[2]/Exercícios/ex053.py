#Crie um programa que (leia uma frase) qualquer e diga se ela é um palíndromo, (descondiserando os espaços).
#Ex [APOS A SOPA] [ANA] [A SACADAD DA CASA] [ANOTARAM A DATA DA MARATONA]

frase1 = input('Digite uma frase: ') 
frase2 = frase1


#Tirar os espaços da frase1 e da frase2.
frase1 = frase1.replace(' ', '')
frase2 = frase2.replace(' ', '')

#Guardar o comprimento da frase digitada.
comprimento_frase = len(frase1)

#Fazer o fatiamento da string de trás pra frente utilizando ::-1. 
frase1 = frase1[comprimento_frase::-1]

if frase1 == frase2:
    print('A frase digitada é um palíndromo! = \033[32mTRUE')
else:
    print('A frase digitada não é um palíndromo! = \033[31mFALSE')

print('\033[m')

#_______________________OU_________________________

frase = frase1

reverter_string = ''.join(reversed(frase))
if frase == reverter_string:
    print('A frase digitada é um palíndromo! = \033[32mTRUE')
else:
    print('A frase digitada não é um palíndromo! = \033[31mFALSE')









    