n = input('Digite algo: ')
print(type(n))
print('Isto é ou são números? ')
n1 = (n.isnumeric())
if n1:
    print('Sim!')
else:
    print('Não!')
print('Isto é ou são letras? ')
a1 = (n.isalpha())
if a1:
    print('Sim!')
else:
    print('Não!')
print('Isto é alfanumerico? ')
an1 = (n.isalnum())
if an1:
    print('Sim!')
else:
    print('Não!')
print('Isto está em maiúsculo? ')
u1 = (n.isupper())
if u1:
    print('Sim!')
else:
    print('Não!')
