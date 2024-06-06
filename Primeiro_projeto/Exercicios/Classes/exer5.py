from dataclasses import dataclass


@dataclass
class Bola:
    def __init__(self, cor: str, circunferencia: float, material: str):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor: str):
        self.cor = nova_cor

    def mostraCor(self):
        print(f"a cor da bola é {self.cor}")


class Quadrado:
    def __init__(self, lado: float):
        self.lado = lado

    def muda_lado(self, novo_
        (self.lado * self.lado) = area

