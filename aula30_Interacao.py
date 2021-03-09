lista = [1, 2, 3, 4, 5]

# i = 0
# qtd = len(lista)
# while i < qtd:
#     print(lista[i])
#     i += 1

# for item in lista:
#     print(item)

# for item in [1, 2, 3, 4, 5]:
#     print(item)

# for item in lista:
#     print(item * 100)

# for idx in range(len(lista)):
#     lista[idx] += 50
# print(lista)

for idx, item in enumerate(lista):
    lista[idx] += 1000
print(lista)