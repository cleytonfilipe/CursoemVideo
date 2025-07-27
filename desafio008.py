print('Desafio 008 - Python - Curso em Video')
print('Conversor de Medidas')
m = float(input('Digite um valor em metros: '))
if m < 2:
    a1 = 'metro'
elif m >= 2:
    a1 = 'metros'
print('{} {} são {} centímetros e {} milímetros!'.format(m, a1, m*100, m*1000))
