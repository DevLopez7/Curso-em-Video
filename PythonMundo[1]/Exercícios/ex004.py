#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

var1 = input('Escreva algo: ')

print('-='*25)
print('\033[37m [o tipo primitivo desse valor é] ', type(var1))
print('\033[32m [só tem espaços?] =', var1.isspace())
print('\033[33m [é um número?] =', var1.isnumeric())
print('\033[34m [é alfabético?] =', var1.isalpha())
print('\033[35m [é alfanumérico?] =', var1.isalnum())
print('\033[36m [está em maiúsculas?] =', var1.isupper())
print('\033[31m [está em minúsculas?] =', var1.islower())
print('\033[30m [está capitalizada?] =', var1.istitle())
print('-='*25)

