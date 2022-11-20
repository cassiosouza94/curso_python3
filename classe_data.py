class Data:
    def __init__(self, dia_semana, dia, mes, ano):
        self.dia_semana = dia_semana
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f'Hoje é {self.dia_semana}, {self.dia} de {self.mes} de {self.ano}'


data_de_hoje = Data('Quarta-feira', 16, 'Novembro', 2022)
print(data_de_hoje)
