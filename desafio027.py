nome = input('Qual o seu nome completo? ')
nome = nome.title().strip().split()
print(f'Seu primeiro nome é: {nome[0]}')
print(f'Seu último nome é: {nome[-1]}')
