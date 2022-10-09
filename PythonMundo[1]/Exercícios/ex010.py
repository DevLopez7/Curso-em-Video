#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#Sabendo que a cotação do dolar está 5.35$.

dinheiro = float(input('informe quanto dinheiro vc tem? R$ '))

dolares = dinheiro/5.21

print(f'Com {dinheiro}R$ você pode comprar \033[32m{dolares:.2f}US$')