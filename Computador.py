from abc import ABC, abstractmethod

class Computador(ABC):

    def __init__(self, modelo, cor, preco):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
    
    def getInformacoes(self):
        return "Modelo: " + self.modelo + "\n" + "Cor: " + self.cor + "\n" + "Preço: R$" + self.preco + "\n"
    
    @abstractmethod
    def cadastrar(self):
        pass