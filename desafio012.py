print('Desafio 012 - Python - Curso em Video')
print('5% de desconto!')
p = float(input('Qual o preço do produto? R$'))
print('O valor do desconto é de R${:.2f} e o preço total com o desconto é R${:.2f}!'.format(p*0.05, p-p*0.05))
