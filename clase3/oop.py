##Introduccion a programacion orientada a objetos
c = list() #dado que list también es una clase
##creando clase


class Customer: 
##atributos y que funcionalidades hace
    id = 0
    fullname= ""
    dni = ""
    productoComprado = ""
    fecha = ""
    def __init__(self, idParametro, fullnameParametro, dniParametro):
        self.id = idParametro
        self.fullname = fullnameParametro
        self.dni = dniParametro 
    
    def verificar(self, fullname):
        print("Este es el cliente",self.fullname)
    def comprar(self,product):
        self.productoComprado = product
try:
    ismael = Customer(1,'Ismael Marin','77878778')
    ismael.comprar("celular")
    ismael.verificar()
    print(__name__)

    pass
## describan un clase x sus atributos y métodos


"""class Rectangulo:
    base 
    altura
"""


















