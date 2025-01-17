# EJERCICIO 6: 
class Product:
    id=""
    nombre=""
    precio=""
    tipo=""
    stock=""
    release=""
    def __init__(self,id,nombre,precio,tipo,stock,release) -> None:
        self.id=id
        self.nombre=nombre
        self.precio=precio
        self.tipo=tipo
        self.stock=stock
        self.release=release
        pass
    def __str__(self) -> str:
        return f"el producto {self.nombre} con {self.id}  de {self.precio} cuenta con {self.stock} stock"
    def updateStock(self,stock):
        self.stock=stock
    
class CarritoCompra:
    def __init__(self):
        self.listaProductos=[]
        self.precioTotal=0
    def agregarProducto(self,product:Product,cantidad=1):
        if self.validarStock(product):
            print("agregando producto")
            self.listaProductos.append(product)
            product.updateStock(product.stock-1)
        else:
            print("el producto no tienen stock")
         
    def quitarProdcut(self,product,id):
        self.listaProductos.pop(id)
        self.listaProductos.pop(product)
        pass
    def calcularPrecio(self):
        for i in self.listaProductos:
            self.precioTotal+=i.precio
    def validarStock(self,product:Product):
        existe=False
        if product.stock>0:
            existe=True
        return existe
    def mostrarProductos(self):
        print(len(self.listaProductos))
        if len(self.listaProductos)>0:
            for i in self.listaProductos:
                print(i)
        else:
            print("carrito vacio")

message="""
    1)Agregar Producto
    2)Mostrar Productos
    3)Eliminar producto del carrito
    4)Mostrar Precio total
    5)Salir
"""
id=0
carrito=CarritoCompra()
while True:

    print(message)
    opcion=int(input("ingrese la opcion a realizar:"))
    if opcion==1:
        try:
            id=id+1
            name=input("ingrese el nombre del producto:")
            precio=float(input("ingrese el precio del producto:"))
            tipo=input("ingrese el tipo del prodcuto:")
            stock=int(input("ingrese el stock del prodcuto:"))
            release=int(input("ingrese el release del prodcuto:"))
            px=Product(id,name,precio,tipo,stock,release)
            carrito.agregarProducto()
        except Exception as Error:
                print("sucedio un error")
        else:
            print("agregando en el menu")
    if opcion==2:
        carrito.mostrarProductos()
    if opcion==3:
        id = int(input("Ingrese el numero que desea eliminar"))
        producto = str(input("Ingrese el producto que desea eliminar"))
        carrito.quitarProdcut(id,producto)
    if opcion == 4: 
        carrito.calcularPrecio()
    if opcion==5:
        break
