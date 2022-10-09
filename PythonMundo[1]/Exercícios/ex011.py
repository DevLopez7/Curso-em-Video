#Faça um programa que leia a (largura e a altura)  de uma parede em metros, (calcule a sua área)
#e a quantidade de tinta necessária para pintá-la, sabendo de (cada litro de tinta, pinta uma área de 2m2).

largura = float(input('Informe quantos metros de largura: '))

altura = float(input('Informe quantos metros de altura: '))

area = largura*altura

tinta = area/2

print(f'\033[32mSua parede tem a dimensão de ({largura} x {altura}) e sua área é de ({area}) '
      f'então será necessário ({tinta}) litros de tinta para pinta-lá.  ')