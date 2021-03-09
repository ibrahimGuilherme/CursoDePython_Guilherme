from typing import List

frase = 'Curso de Python e Banco de Dados'

print(frase.split())
palavras = frase.split()
print(palavras)

print(palavras[2])
linguagem = palavras[2]
print(linguagem)

frase2 = '1,2,3,4,5'
print(frase2.split(','))
print(frase2.split(',', maxsplit=2))

frase3 = '-'.join(palavras)
print(frase3)