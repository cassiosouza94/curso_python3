class Calendario:
    def __str__(self):
        return f'Hoje é {self.dia} de {self.mes} de {self.ano}'


data = Calendario()
data.dia = 16
data.mes = 'Novembro'
data.ano = 2022
print(data)
