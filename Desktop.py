from Computador import Computador

class Desktop(Computador):

    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        self.__potenciaDaFonte = potenciaDaFonte
        super().__init__(modelo, cor, preco)
    
    def getInformacoes(self):
        return "Modelo: " + self.modelo + "\n" + "Cor: " + self.cor + "\n" + "Preço: R$" + str(float(self.preco)) + "\n" +  "Potência da fonte: " + str(self.__potenciaDaFonte) + " Watts\n"
    
    def cadastrar(self):
        print("\nDesktop cadastrado\n")
