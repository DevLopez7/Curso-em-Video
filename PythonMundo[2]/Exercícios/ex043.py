#Desenvolva um programa que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#Abaixo de 18.5: Abaixo do peso
#Entre 18.5 e 25: Peso ideal
#25 até 30: Sobrepeso
#30 até 40:Obesidade
#Acima de 40: Obesidade mórbida

peso = float(input('Informe seu peso (kg): '))

altura = float(input('Informe sua altura (metro e cm): '))

imc = peso / (altura**2)

if imc < 18.5:
    print(f'O imc dessa pessoa é de {imc:.1f}\n ,  [Abaixo do peso]')

elif 25 > imc >= 18.5:
    print(f'O imc dessa pessoa é de {imc:.1f} [Peso ideal]')

elif 30 > imc >= 25:
    print(f'O imc dessa pessoa é de {imc:.1f} [Sobrepeso]')

elif 40 > imc >= 30:
    print(f'O imc dessa pessoa é de {imc:.1f} [Obesidade]')

elif imc > 40:
    print(f'O imc dessa pessoa é de {imc:.1f} [Obesidade mórbida]')