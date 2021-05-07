# NOME()
#     INSTRUÇÕES

def exibirnome():
    print('Curso de Python')

def somar(num1=0, num2=0):
    soma = num1 + num2
    return soma

def inteiros(inicio=0, final=0):

    if inicio < 0 or final <= 0:
        return -1

    lista = list(range(inicio, final+1))
    return lista

def inteirosseminicio(final=0, inicio=None):
    if inicio == None:
        inicio = 0
    if inicio < 0 or final <= 0:
        return -1

    lista = list(range(inicio, final+1))
    return lista


# exibirnome()
#
# x = 33
# y = 65
# s = somar(x, y)
# print(f'Soma de {x} {y} = {s}')

minhalista = inteiros(2, 8)

if type(minhalista) is int:
    print('Valores inválidos nos parâmetros')
else:
    print(minhalista)

minhalista = inteirosseminicio(12)
if type(minhalista) is int:
    print('Valores inválidos nos parâmetros')
else:
    print(minhalista)
