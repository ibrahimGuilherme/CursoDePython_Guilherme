# arq = open('teste.txt', 'a')
# arq.write('Curso de Python\n')
# arq.write('Curso de SQL\n')
# arq.close()

arq1 = open('amigos.txt', 'r')
arq2 = open('teste.txt', 'w')

while True:
    texto = arq1.readline()

    if texto == '':
        break

    if texto[:5] == 'ffffj':
        continue
    arq2.write(texto)
arq1.close()
arq2.close()