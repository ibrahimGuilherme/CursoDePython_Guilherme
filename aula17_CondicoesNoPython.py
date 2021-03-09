idade = int(input('Qual a sua idade? '))

# if idade < 18:
#     print('Apenas maiores de dezoito anos podem entrar.')
# else:
#     print('Olá! Aproveite o nosso bar! ')
#     bebida = str(input('Qual bebida vai querer? '))
#     print(f'Segue sua bebida {bebida}')

if idade<18:
    print('Apenas maiores de dezoito anos podem entrar.')
elif idade>=18 and idade<21:
    print('Você pode consumir refrigerantes')
else:
    print('Bem vindo!')
    bebida = str(input('Qual bebida deseja? '))
    print(f'Segue sua bebida: {bebida}')
#and ou or