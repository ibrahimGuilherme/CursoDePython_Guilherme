idade = int(input('Qual sua idade? '))

if idade <18:
    print('Apenas pessoas com 18 anos ou mais podem entrar.')
else:
    print('Bem vindo ao bar!')

    if idade <= 21:
        print('Você pode solicitar refrigerantes')
    elif idade > 21 and idade <=60:
        print('Você pode solicitar cereja ou vodka')
    else:
        print('Você pode solicitar água')
