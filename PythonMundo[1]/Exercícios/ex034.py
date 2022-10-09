#Escreva um programa que pergunta o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00 calcule um aumento de 10%.
#Para os inferiores ou iguais o aumento é de 15%.


salario = float(input('Qual é a sua renda mensal? '))

if salario > 1250:
    aumento = salario * 10 / 100
    print(f'Seu salario teve um aumento de 10% e passou a ser {salario + aumento}')

else: 
    aumento = salario * 15 / 100
    print(f'Seu salario teve um aumento de 15% e passou a ser {salario + aumento}')

