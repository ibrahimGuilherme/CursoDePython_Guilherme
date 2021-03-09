# print('Início')
# for num in range(0, 6):
#     print(num)
#     if num == 2:
#         break
# print('Final')

# for c in 'Curso de Python':
#     print(c)
#     if c == 'o':
#         break

# for c in 'Curso de Python':
#     if c == 'o':
#         continue
#     print(c)

# for c in 'Curso de Python':
#     if c in 'ory':
#         continue
#     print(c)

soma = 0
print('Digite apenas números entre 0 e 10.\nA soma máxima será 20.')

for num in range(0, 4):
    n = int(input('Número: '))
    if n >= 0 and n <= 10:
        soma += n
    else:
        print(f'Serão somados apenas números entre 0 e 10, {n} não será somado')
    if soma >= 20:
        soma = 20
        print('valor máximo da soma atingido')
        break
print(f'Soma = {soma}')