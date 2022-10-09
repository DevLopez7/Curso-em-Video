#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o (valor da casa), o (salário do comprador) e (em quantos anos ele vai pagar).
#(Calcule o valor da prestação mensal), sabendo que ela (não pode exeder (30%) do salário) ou então o (empréstimo será negado).

casa = float(input('Valor da casa: R$ '))

salario = float(input('Salário do comprador: R$ '))

anos = int(input('Quantos anos de financiamento: ')) 

prestação = casa / (anos * 12)

mínimo = (salario * 30) / 100

print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${prestação:.2f} ')

if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO! ')

else: 
    print('Empréstimo NEGADO!')




