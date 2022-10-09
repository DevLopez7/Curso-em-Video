#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

#Qual a função da primeira variavel?
    #(coletar o valor digitado pelo usúario)
preco = float(input('informe o preço do produto R$: '))

#Qual a função da segunda variavel?
    #(fazer o calculo de porcentagem)
preconovo = preco - (preco/100*5)

print(f'\033[35mO valor de R${preco:.2f} agora com desconto de 5% é: R${preconovo:.2f}')

    
