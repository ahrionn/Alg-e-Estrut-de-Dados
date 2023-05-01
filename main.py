from Desktop import Desktop
from Notebook import Notebook

#Testar Desktop
desk = Desktop("Nvidia Ultimate Desktop Pack", "Preto", 7000, 500)
desk.cadastrar()
print(desk.getInformacoes())

#Testar Notebook
note = Notebook("Notebook Asus AMD Ryzen 5", "Prata", 2370, 10)
note.cadastrar()
print(note.getInformacoes())
