def calculadora():
    print('\n' + '-' * 40)
    print(f'{"         C A L C U L A D O R A"}')
    print('-' * 40)
def menu():
    calculadora()
    print('1. Somar')
    print('2. Subtrair')
    print('3. Multiplicar')
    print('4. Dividir')
    print('5. Digitar outros números')
    print('6. Sair')

def somar(n1=0, n2=2):
    r = n1 + n2
    return r

def subtrair(n1=0, n2=2):
    r = n1 - n2
    return r

def multiplicar(n1=0, n2=2):
    r = n1 * n2
    return r

def dividir(n1=0, n2=2):
    r = n1 / n2
    return r

num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))

while num1>0 and num2>0:
    menu()
    opcao = int(input('Qual a sua opção [1/2/3/4/5/6]? '))

    if opcao < 1 or opcao > 6:
        print('\nOpção inválida')
        input('\nPressione <ENTER>\n')
        continue
    if opcao == 1:
        res = somar(num1, num2)
        print(f'\n{num1} + {num2} = {res}')
        input('\nPressione <ENTER>\n')
    elif opcao == 2:
        res = subtrair(num1, num2)
        print(f'\n{num1} - {num2} = {res}')
        input('\nPressione <ENTER>\n')
    elif opcao == 3:
        res = multiplicar(num1, num2)
        print(f'\n{num1} * {num2} = {res}')
        input('\nPressione <ENTER>\n')
    elif opcao == 4:
        res = dividir(num1, num2)
        print(f'\n{num1} / {num2} = {res:.2f}')
        input('\nPressione <ENTER>\n')
    elif opcao == 5:
        num1 = int(input('Número 1: '))
        num2 = int(input('Número 2: '))
        input('\nPressione <ENTER>\n')
    elif opcao == 6:
        break