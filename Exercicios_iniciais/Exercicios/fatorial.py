print('='*30)
print('Função para calcular Fatoriais')
print('='*30)
num = int(input('Digite um número inteiro para ver seu fatorial: '))
c = num
f = 1
while (c > 0):
    f = c * f
    if c != 1:
        print(f'{c} x ',end='')
    else:
        print(f'{c} = {f}', end='')
    c = c - 1
print(f'\nPortanto o fatorial de {num} vale {f}.')