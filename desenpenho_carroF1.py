class CarroFormula1ScuderiaFerrari:
    def __init__(self, velocidade_maxima):
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = 0

    def aceleracao(self, delta=5):
        maxima = self.velocidade_maxima
        nova_velocidade_atingida = self.velocidade_atual + delta
        self.velocidade_atual = nova_velocidade_atingida if nova_velocidade_atingida <= maxima else maxima
        return self.velocidade_atual

    def frenagem(self, delta=5):
        nova_velocidade_atingida = self.velocidade_atual - delta
        self.velocidade_atual = nova_velocidade_atingida if nova_velocidade_atingida >= 0 else 0
        return self.velocidade_atual


if __name__ == '__main__':
    piloto_equipe = CarroFormula1ScuderiaFerrari(400)

    for _ in range(30):
        print(piloto_equipe.aceleracao(20))
        print('🏎')

    for _ in range(15):
        print(piloto_equipe.frenagem(delta=30))
        print('🏎')
