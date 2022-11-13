# Começamos dando um START em nossas variaveis:

cpf_informado = '11122233396'
numero_Digito_Verif_1 = 0
numero_Digito_Verif_2 = 0
check_numero_Digito_Verif_1 = 0
check_numero_Digito_Verif_2 = 0
i = 1

# Verificamos o número de caracteres do CPF informado: 👀

if len(cpf_informado) < 11:
    dif_Numerica_CPF = 11 - len(cpf_informado)
    cpf_informado = '0' * dif_Numerica_CPF + cpf_informado

# Capturamos o número dos dois últimos digítos verificadores do CPF, 1º digíto e 2º digíto:

check_numero_Digito_Verif_1 = int(cpf_informado[9:10])
check_numero_Digito_Verif_2 = int(cpf_informado[10:11])

# Executamos o cálculo do digíto verificador, nesse caso o 1º digíto:

for i in range(1, 10):
    numero_Digito_Verif_1 = numero_Digito_Verif_1 + \
        int(cpf_informado[i-1:i]) * i

# Depois de executar o cálculo, temos que extrair o resto da divisão por 11:

numero_Digito_Verif_1 = numero_Digito_Verif_1 % 11

# Depois de executar o cáculo do resto da divisão por 11, temos que checar se o número é igual a 10:
# Se o número for maior que 10, devemos considerar 0:

if (numero_Digito_Verif_1 == 10):
    numero_Digito_Verif_1 = 0

# Agora iremos verifivar o 1º digíto: 👀

if numero_Digito_Verif_1 != check_numero_Digito_Verif_1:
    print('1º Digíto verificador inválido! ❌')

# Executamos então o cálculo do outro digíto verificador, agora nesse caso o 2º digíto:

for i in range(2, 11):
    numero_Digito_Verif_2 = numero_Digito_Verif_2 + \
        int(cpf_informado[i-1:i]) * (i - 1)

# Depois de executar o cálculo, temos que extrair o resto da divisão por 11 novamente:

numero_Digito_Verif_2 = numero_Digito_Verif_2 % 11

# Novamente, depois de executar o cáculo do resto da divisão por 11, temos que checar se o número é igual a 10:
# Se o número for maior que 10, iremos considerar 0:

if (numero_Digito_Verif_2 == 10):
    numero_Digito_Verif_2 = 0

# E agora verificar o 2º digíto: 👀

if numero_Digito_Verif_2 != check_numero_Digito_Verif_2:
    print('2º Digíto verificador inválido! ❌')

# Partimos agora para concluir a validação do CPF:

if (numero_Digito_Verif_1 == check_numero_Digito_Verif_1 and numero_Digito_Verif_2 == check_numero_Digito_Verif_2):
    print('CPF válido! ✅')
