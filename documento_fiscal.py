class DocumentoFiscal:
    def __init__(self):
        self.numero_Digito_Verificador_1 = []
        self.numero_Digito_Verificador_2 = []

    def calcular_digito_verificador(self, documento, digito=1):
        pass

    def valido(self, documento):

        documento = documento.replace(
            '.', '').replace('/', '').replace('-', '')

        if (not documento.isnumeric()):
            return False

        digitos = None

        if (len(documento) == 11):
            digitos = documento[:9]
        elif (len(documento) == 14):
            digitos = documento[:12]
        else:
            return False

        digito_verificador_1 = self.calcular_digito_verificador(
            digitos, 1)
        digito_verificador_2 = self.calcular_digito_verificador(
            digitos + str(digito_verificador_1), 2)

        return documento == digitos + str(digito_verificador_1) + str(digito_verificador_2)
