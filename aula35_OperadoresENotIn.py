# print(2 in [1, 2, 3, 4, 5])
# print(10 not in [1, 2, 3, 4, 5])

l = [1, 2, 3, 4, 5, 6]
# if 2 in l:
#     print('Está na lista.')
# else:
#     print('Não está na lista')
# if 10 not in l:
#     print('10 não está na lista.')

# if 2 and 3 and 4 in l:
#     print('Está na lista.')

# if 2 or 10 in l:
#     print('Um está na lista.')
# else:
#     print('Nenhum número não está na lista')

x = 10
z = 30
y = 20

num = int(input('Digite um número: '))
if num in [x, y, z]:
    print(f'O número {num} está na lista.')
else:
    print(f'O número {num} não está na lista.')
