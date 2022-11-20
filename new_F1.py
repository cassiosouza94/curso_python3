class CarroFormula1ScuderiaFerrari:
    def __init__(self, modelo_carro, cor, categoria, lancamento):
        self.modelo_carro = modelo_carro
        self.cor = cor
        self.categoria = categoria
        self.lancamento = lancamento

    def __str__(self):
        return f'Este é o novo {self.modelo_carro} cor {self.cor} na categoria {self.categoria} temporada {self.lancamento}'


carro_corridas = CarroFormula1ScuderiaFerrari(
    'Ferrari F1-75 🏎️ ', 'vermelho com detalhes pretos', 'corridas de automobilismo', 2022)
print(carro_corridas)
