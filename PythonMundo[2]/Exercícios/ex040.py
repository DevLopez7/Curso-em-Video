#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9:RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO

nota1 = float(input('Primeira nota: '))

nota2 = float(input('Segunda nota: '))

média = (nota1 + nota2) / 2

if 7 > média >= 5:
    print(f'A média do aluno foi {média}. Situação = aluno em processo de RECUPERAÇÃO')

elif média < 5:
    print(f'A média do aluno foi {média}. Situação = aluno REPROVADO!')

elif média >= 7:
    print(f'A média do aluno foi {média}. Situação = aluno APROVADO!')