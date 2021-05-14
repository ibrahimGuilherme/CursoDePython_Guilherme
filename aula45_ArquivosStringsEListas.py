pessoas = [[1, 'Ibrahim Guilherme Moraes de Oliveira', '(10) 9.1234-5678', 'iibrahimguilherme00@gmail.com'],
           [2, 'Guilherme Moraes de Oliveira', '(11) 9.1234-5678', 'iibrahimguilherme01@gmail.com'],
           [3, 'Moraes de Oliveira', '(12) 9.1234-5678', 'iibrahimguilherme02@gmail.com'],
           [4, 'Oliveira', '(13) 9.1234-5678', 'iibrahimguilherme03@gmail.com']]


# pessoa = pessoas[0]

# print(pessoas)
#
# print(f'Código: {pessoa[0]}')
# print(f'Nome: {pessoa[1]}')
# print(f'Telefone: {pessoa[2]}')
# print(f'E-mail: {pessoa[3]}')

# Cod: 5
# Nome: 40
# Telefone: 35
# E-mail: 40

# for pessoa in pessoas:
#
#     codigo = pessoa[0]
#     nome = pessoa[1]
#     telefone = pessoa[2]
#     email = pessoa[3]
#
#     registro = f'{codigo: >5} {nome: >40} {telefone: >35} {email: >40}'
#     print(registro)

arq = open('pessoas.txt', 'w')

for pessoa in pessoas:

    codigo = pessoa[0]
    nome = pessoa[1]
    telefone = pessoa[2]
    email = pessoa[3]

    registro = f'{codigo: >5} {nome: >40} {telefone: >35} {email: >40}\n'
    print(registro)

    arq.write(registro)

arq.close()