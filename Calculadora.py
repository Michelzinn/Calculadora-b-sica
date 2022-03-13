while True:
    num_1 = input('Digite um número: ')
    num_2 = input('Digite um número: ')
    operador = input('Digite um operador (+,-,*,/) ')

    if not num_1.isdigit() or not num_2.isdigit():
        print('você precisa digitar um número inteiro!')
        quit()

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == '/':
        print(num_1 / num_2)
    else:
        print('operador invalido')
        break

    continuacao = input('Quer continuar a calcular? (S/N) ')
    if continuacao == 'n' or continuacao == 'N':
        break
