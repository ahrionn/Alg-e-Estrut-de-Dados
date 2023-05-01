from Computador import Computador

class Notebook(Computador):

    def __init__(self, modelo, cor, preco, tempoDeBateria):
        self.__tempoDeBateria = tempoDeBateria
        super().__init__(modelo, cor, preco)
    
    def getInformacoes(self):
        return "Modelo: " + self.modelo + "\n" + "Cor: " + self.cor + "\n" + "Preço: R$" + str(float(self.preco)) + "\n" + "Tempo de bateria: " + str(self.__tempoDeBateria) + " horas\n"
    
    def cadastrar(self):
        print("\nNotebook cadastrado\n")