#Matemático
numero = int(input('Digite um número de 0 a 9999: '))
unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000)
print(f'Milhar: {milhar}')
print(f'Centena: {centena}')
print(f'Dezena: {dezena}')
print(f'Unidade: {unidade}')
print('')

#Manipulando a string
numero = input('Digite um número com 4 dígitos: ')
numero = numero.strip()
print(f'Milhar: {numero[0]}')
print(f'Centena: {numero[1]}')
print(f'Dezena: {numero[2]}')
print(f'Unidade: {numero[3]}')
print('')

#usando .zfill
numero = input('Digite um número de 0 a 9999: ')
numero = numero.zfill(4)
print(f'Milhar: {numero[0]}')
print(f'Centena: {numero[1]}')
print(f'Dezena: {numero[2]}')
print(f'Unidade: {numero[3]}')
