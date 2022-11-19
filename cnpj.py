from documento_fiscal import DocumentoFiscal


class Cnpj(DocumentoFiscal):
    def __init__(self):
        self.numero_Digito_Verificador_1 = list(
            range(5, 1, -1)) + list(range(9, 1, -1))
        self.numero_Digito_Verificador_2 = list(
            range(6, 1, -1)) + list(range(9, 1, -1))

    def calcular_digito_verificador(self, cnpj, digito=1):
        numeros = self.numero_Digito_Verificador_1 if digito == 1 else self.numero_Digito_Verificador_2
        resultado = (sum(int(digito) * numero for digito,
                     numero in zip(cnpj, numeros))) % 11
        return 0 if resultado < 2 else 11 - resultado
