from cpf import Cpf
from cnpj import Cnpj


sistema_validador_CPF = Cpf()
print(sistema_validador_CPF.valido('111.222.333-96'))

sistema_validador_CNPJ = Cnpj()
print(sistema_validador_CNPJ.valido('88.458.835/0001-30'))
