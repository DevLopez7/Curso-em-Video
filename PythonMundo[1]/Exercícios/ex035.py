#Desenvolva um programa que leia o comprimento de três retas e diga ao usúario se elas podem ou não formar um triângulo.

med1da = float(input('Digite o primeiro segmento: '))

med2da = float(input('Digite o segundo segmento: '))

med3da = float(input('Digite o terceiro segmento: '))

#[< = menor] [> = maior]
if med1da < med2da + med3da and med2da < med1da + med3da and med3da < med1da + med2da:
    print('Os segmentos acima PODEM FORMAR um triangulo')

else:
    print('Os segmentos acima NÃO PODEM FORMAR um triangulo')