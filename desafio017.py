print('Desafio 017 - Python - Curso em Video')
from math import hypot
print('Vamos ver quanto mede a hipotenusa do triângulo retângulo!')
co = float(input('Qual o valor do cateto oposto? '))
ca = float(input('Qual o valor do cateto adjacente? '))
hi = hypot(co, ca)
print('A hipotenusa deste triângulo retângulo vai medir {:.2f}!'.format(hi))
