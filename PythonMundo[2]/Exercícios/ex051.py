#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('='*30)
print('    10 TERMOS DE UMA PA')
print('='*30)

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: ')) 

décimo = primeiro + (10 - 1) * razão

for intervalo in range(primeiro, décimo + razão, razão):
    print(intervalo, end=' ↦ ')

print('ACABOU!!!')

