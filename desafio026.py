frase = input('Digite uma frase: ')
print(f'A letra "A" aparece {frase.count('A')} vezes')
print(f'e aparece primeiramente na posição {frase.find('A')}')
print(f'e aparece ultimamente na posição {frase.rfind('A')}')