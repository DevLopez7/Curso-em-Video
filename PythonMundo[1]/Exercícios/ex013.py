#Faça um algoritmo que leia o salário de um funcionário, e mostre seu novo salário com 15% de aumento.

#Qual a função da primeira variavel?
    #(coletar o valor digitado pelo usúario)
salario = float(input('Digite o salário do funcionário R$ '))

#Qual a função da segunda variavel?
    #(fazer o calculo de porcentagem)
aumento = salario + (salario/100*15)

print(f'\033[36mO funcionário que recebia {salario}R$ teve um aumento e passsou a receber {aumento}R$')