#Para la pregunta 4 al importar las funciones usar el manejo de errores (try, except) y en las sentencias de "else"
#imprimir la ruta del directorio de trabajo os.getcwd() y en las sentencia finally imprimir "proceso terminado"}

from ejercicio4 import format,verificar,agregarPais,agregarLote

try: 
    verificar() 
    agregarPais('Mexico')
    agregarLote('0002')
except: 
    print("Ha ocurrido un error en el código. Vuelve a intentarlo.")
else: 
    os.getcwd()
finally: 
    print("Proceso terminado")
