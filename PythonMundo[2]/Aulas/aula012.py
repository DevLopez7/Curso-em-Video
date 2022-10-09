nome = str(input('Qual é o seu nome: '))

if nome == 'lucas':
    print('Que nome bonito!')

elif nome == 'pedro' or nome == 'maria' or nome == 'paulo':
    print('Seu nome é bem popular no Brasil!')

elif nome in 'ana claudia jessica juliana':
    print('Belo nome feminino')

else: 
    print('Seu nome é bem normal..')

print(f'Tenha um bom dia!, {nome}')