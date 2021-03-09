# inicio = int(input('Início: '))
# final = int(input('final: '))
# passo = int(input('Passo: '))
# for num in range(inicio, final+1, passo):
#     print(f'Número {num}')

soma = 0
print('Digite apenas números entre 0 e 10.')

for num in range(0, 3):
    n = int(input('Número: '))
    if n >= 0 and n <= 10:
        soma += n
    else:
        print(f'Serão somados apenas números entre 0 e 10, {n} não será somado')

print(f'Soma = {soma}')