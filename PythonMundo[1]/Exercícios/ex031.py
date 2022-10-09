#Desemvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem.
#Cobrando R$ 0.50 por Km para viagens de até 200Km e R$ 0,45 para viagens mais longas.

distancia = float(input('Qual a distância da sua viagem? '))

print(f'Você está prestes a começar uma viagem de {distancia}Km.')

if distancia <= 200:
    preço = distancia * 0.50

else:
    preço = distancia * 0.45
print(f'Sua viagem será de {distancia}Km e você tera que pagar {preço}R$.')
    

