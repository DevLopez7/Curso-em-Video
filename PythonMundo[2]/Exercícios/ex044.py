#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto.
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

nome = input('Digite seu nome: ')

print(f'Olá {nome} Seja Bem-vindo@ a loja \033[4;33m ALÉM DO VISÍVEL!\033[m')

preço = float(input('Digite o preço do produto R$: '))

print('''Escolha uma das formas de pagamento:
----------------------------------------
[1] À vista dinheiro/cheque (10% de desconto).

[2] À vista no cartão (5% de desconto).

[3] Em até 2x no cartão (preço normal).

[4] 3x ou mais no cartão (20% de juros).
----------------------------------------''')

opção = int(input('Sua opção: '))
if opção == 1: 
    pagar = preço - (preço * 10) / 100
    print(f'Sua compra no valor de {preço}R$ com 10% de desconto vai custar{pagar}R$')

elif opção ==2:
    pagar = preço - (preço * 5) / 100
    print(f'Sua compra no valor de {preço}R$ com 5% de desconto vai custar{pagar}R$')

elif opção == 3:
    pagar = (preço)
    print(f'Sua compra vai custar{pagar}R$')

elif opção == 4:
    pagar = preço + (preço * 20) / 100
    print(f'Sua compra no valor de {preço}R$ com 20% de JUROS vai custar{pagar}R$')

else:
    print('Opção inválida. Tente novamente!')