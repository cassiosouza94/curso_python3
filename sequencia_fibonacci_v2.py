def fibonacci(limitation_on_count):

    penultimo_numero = 0
    ultimo_numero = 1
    print(f'{penultimo_numero}, {ultimo_numero}', end='-')
    while ultimo_numero < limitation_on_count:
        penultimo_numero, ultimo_numero = ultimo_numero, penultimo_numero + ultimo_numero
        print(ultimo_numero, end='-')


if __name__ == '__main__':
    fibonacci(20000)
