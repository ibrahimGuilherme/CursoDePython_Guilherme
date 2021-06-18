# arq = open('pessoas.txt', 'r')
#
# linha = arq.readline()
#
# while len(linha) > 0:
#
#     #print(linha)
#
#     cod = linha[0:5].strip()
#     nome = linha[5:46].strip()
#     telefone = linha[46:82].strip()
#     email = linha[82:125].strip()
#
#     print(f'\nCódigo..: {cod}')
#     print(f'Nome....: {nome}')
#     print(f'Telefone: {telefone}')
#     print(f'E-mail..: {email}')
#
#     linha = arq.readline()
#
#
# arq.close()
a = 'abc'
b = 123
print('o alfabeto é %s e o resto é %s'%(a, b))