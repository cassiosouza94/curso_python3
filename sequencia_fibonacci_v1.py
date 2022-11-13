def fibonacci(limitation_on_count):

    penultimo_numero = 0
    ultimo_numero = 1
    print(f'{penultimo_numero} - {ultimo_numero}', end='-')
    while ultimo_numero < limitation_on_count:
        proximo_numero = penultimo_numero + ultimo_numero
        print(f'{proximo_numero}', end='-')
        penultimo_numero = ultimo_numero
        ultimo_numero = proximo_numero


if __name__ == '__main__':
    fibonacci(20000)
