amigos = {'Ana':64389764, 'Bruna':87435437, 'Julia':787784547}
print(amigos)

if 'Ana' in amigos:
    print(f'Telefone {amigos["Ana"]}.')
else:
    print('não tenho o telefone de Ana.')

amigo = str(input('Digite o nome: '))

if amigo not in amigos:
    print(f'Não tenho o telefone do {amigo}.')
else:
    print(f'Telefone do {amigo} {amigos[amigo]}.')

amigo = amigos.pop('Ana')
print(amigo)
amigo = amigos.pop('Julia')
print(amigo)
print(amigos)

amigo = amigos.popitem()
print(amigo)

print(amigos)

d1 = {'Ana':64389764, 'Bruna':87435437}
d2 = {'Julia':787784547, 'Regina': 4389458734}
print(d1)
print(d2)
d1.update(d2)
print(d1)
print(d1['Regina'])

for chave in d1:
    print(chave)

for valor in d1.values():
    print(valor)

for chave, valor in d1.items():
    # print(chave)
    # print(valor)
    print(f'{chave} => {valor}')

chaves = list(d1.keys())
valores = list(d1.values())
print(chaves)
print(valores)
print(valores[1])
print(valores[2])

chaves = ['Ana', 'Bruna', 'Julia', 'Regina']
valores = [ 100,     200,     300,      400]

dicfinal = dict(zip(chaves, valores))
print(chaves)
print(valores)
print(dicfinal)