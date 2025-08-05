from random import choice
print('Desafio 019 - Python - Curso em Video')
print('Sorteando os alunos!')
a1 = input('Qual o primeiro aluno? ')
a2 = input('Qual o segundo aluno? ')
a3 = input('Qual o terceiro aluno? ')
a4 = input('Qual o quarto aluno? ')
lista = [a1, a2, a3, a4]
esc = choice(lista)
print('O aluno escolhido foi {}!'.format(esc))
