nome = input('Qual é o seu nome? : ')
print(f'Muito prazer em te conhecer, {nome}!')

dia_nascimento = input('Em qual dia você nasceu? : ')
mes_nascimento = input('Qual foi o mês que você nasceu? : ')
ano_nascimento = input(f'E qual é o seu ano de nascimento {nome}? :')
print('Você nasceu no dia {} do mês de {} no ano de {}'.format(
    dia_nascimento, mes_nascimento, ano_nascimento))
