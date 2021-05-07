# arq = open('amigos.txt', 'r')

# for linha in arq:
#     print(linha)
#
# linhas = arq.read(3)
# print(linhas)
#
# arq.close()

arq2 = open('amigos2.txt', 'r')

# cod = arq2.read(3)
# print(cod)
# nom = arq2.read(20)
# print(nom)
# traco = arq2.read(2)
#
# cod = arq2.read(3)
# print(cod)
# nom = arq2.read(20)
# print(nom)
# traco = arq2.read(2)

# lista=arq2.readlines()
# #print(lista)
# for linha in lista:
#     print(linha)

# linha1 = arq2.readline()
# linha2 = arq2.readline()
# print(linha1)
# print(linha2)

linha = arq2.readline()

while len(linha) > 0:
    print(linha)
    linha = arq2.readline()

arq2.close()