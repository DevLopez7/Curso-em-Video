#Refaça o DESAFIO 035 dos triângulos. acrescentando o recurso de mostrar que tipo de triângulo será formado:

#Equilátero: todos os lados iguais.
#Isósceles: dois lados iguais.
#Escaleno: todos os lados diferentes.

med1da = flomed1da = float(input('Primeiro segmento: '))

med2da = float(input('Segundo segmento: '))

med3da = float(input('Terceiro segmento: '))

#se a medida [1] for - que a medida [2] + a medida [3] e a medida [2] for - que a medida [1] + a medida [3] e a medida [3] for - que a medida [1] + a medida [2]
if med1da < med2da + med3da and med2da < med1da + med3da and med3da < med1da + med2da:
    print('Os segmentos acima PODEM FORMAR um triangulo ', end ='')
    
    if med1da == med2da == med3da:
        print('EQUILÁTERO!') #todos os lados iguais
    
    elif med1da != med2da != med3da != med1da:
        print('ESCALENO!') #todos os lados diferentes
    
    else:
        print('ISÓSCELES') 

else:
    print('Os segmentos acima NÃO PODEM FORMAR um triangulo')
