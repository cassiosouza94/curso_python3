from documento_fiscal import DocumentoFiscal


class Cpf(DocumentoFiscal):
    def __init__(self):
        self.numero_Digito_Verificador_1 = range(10, 0, -1)
        self.numero_Digito_Verificador_2 = range(11, 0, -1)

    def calcular_digito_verificador(self, cpf, digito=1):
        numeros = self.numero_Digito_Verificador_1 if digito == 1 else self.numero_Digito_Verificador_2
        resultado = (sum(int(digito) * numero for digito,
                     numero in zip(cpf, numeros)))
        resultado = (resultado * 10) % 11
        return 0 if resultado == 10 else resultado
