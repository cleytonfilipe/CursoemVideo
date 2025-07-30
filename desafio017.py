print('Desafio 017 - Python - Curso em Video')
import math
print('Qual o valor da hipotenusa do triângulo retângulo?')
co = int(input('Qual o valor do cateto oposto? '))
ca = int(input('Qual o valor do cateto adjacente? '))
sqc = pow(co, 2) + pow(ca, 2)
print('A hipotenusa deste triângulo retângulo é {:.2f}!'.format(math.sqrt(sqc)))
