## 2. Una tienda de autopartes: 

class Producto:
    # Constructor de clase
    def __init__(self, nombre, fechaCompra, duracion):
        self.nombre = nombre
        self.fechaCompra = fechaCompra
        self.duracion = duracion
        print('Se ha creado el producto:', self.nombre)

    def __str__(self):
        return f'El producto{self.nombre} con fecha de inicio {self.fechaCompra} con el año de caducidad {self.duracion}'

class Catalogo:

    productos = []  # Esta lista contendrá objetos de la clase Pelicula

    def __init__(self):
        self.productos = []

    def agregar(self, p:productos):  # p será un objeto Pelicula
        self.productos.append(p)

    def mostrar(self):
        for p in self.productos:
            print(p)  # Print toma por defecto str(p)


p1 = Producto('Cofre','2018','2')
p2 = Producto('Marco de Radiador','2019','3')
p3 = Producto('Calavera','2020','4')

c1 = catalogo()
c1.agregar(p1)
c1.agregar(p2)
c1.agregar(p3)

print(c1.productos)
c1.mostrar()






    



