#Faca um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for p in range(1, 6): #repetir o código abaixo 5 vezes
#_____________________________________________________________________
    peso = float(input(f'Peso da {p}ª pessoa: ')) #coletar os 5 pesos.
    
    if p == 1: #se for o primeiro laço
        
        maior = peso #maior se torna o primeiro peso digitado.
        menor = peso #menor se torna o primeiro peso digitado.
    
    else: #se não for o primeiro laço
        
        if peso > maior: #se o peso que acabou de ser lido for maior do que o maior peso que foi guardado, o maior peso passa a ser o peso que acabou de ser lido.
            maior = peso
        
        if peso < menor: #se o peso que acabou de ser lido for menor do que o menor peso que foi guardado, o menor peso passa a ser o peso que acabou de ser lido.
            menor = peso
#_____________________________________________________________________
print(f'O maior peso lido foi de {maior}Kg.')
print(f'O menor peso lido foi de {menor}Kg.')


#----------DICAS----------
#7 = maior 
#7 = menor 
#Quando quiser o maior e o menor, verifique se é a primeira ocorrência, se for a primeira ocorrência
#Se é o primeiro número "peso" primeiro laço que ta acontecendo, ele vai ser o maior e o menor ao mesmo tempo pois não foi lido nada de diferente disso.