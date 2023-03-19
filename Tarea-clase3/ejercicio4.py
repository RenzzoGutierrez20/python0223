## Ejercicio 4: Programa que tenga una clase Producto. 

class Producto:
    pais:str
    lote:str
    año:int
    nombre:str 
    def __init__(self,pais,lote,año,nombre):
        self.pais=pais
        self.lote=lote
        self.año=año
        self.nombre=nombre

    def format(self):
        return f"Codigo:{self.pais}-{self.lote}-{self.año}, producto: {self.nombre}"
    
    def verificar(self):
        print("este es el producto",self.nombre)

    def agregarPais(self, city):
        self.pais = city

    def agregarLote(self, Lote):
        self.lote = Lote
    def agregarAño(self, Lote):
        self.lote = Lote