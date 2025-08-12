from random import shuffle
print('Desafio 020 - Python - Curso em Video')
print('Ordem dos Alunos!')
a1 = input('Qual o primeiro aluno? ')
a2 = input('Qual o segundo aluno? ')
a3 = input('Qual o terceiro aluno? ')
a4 = input('Qual o quarto aluno? ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem dos alunos será ')
print(lista)
