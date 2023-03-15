#bloque basico de manejo de errores

try:
    n = int(input("Introduce numero"))
    m = 7 

    print("{}/{} = {}".format(m,n,m/n))

except:
    print("Ingrese un valor correcto")

try:
    lista = []
    lista.pop()

except: 
    print("La lista esta vacia")

## arrastrando
listaGlobal = []
listaGlobalv2 = [1,2,3,32,33,2,3]
def retirarElementos(listaParametro:list): 
    try: 
        listaParametro.pop()
        print(listaParametro)
    except:
        print("La lista esta vacia")

retirarElementos(listaGlobal)
retirarElementos(listaGlobalv2)

try: 
    a = "Hola"
    print(a+1)
except:
    print("except")
else:
    print("Solo si el bloque try ejecuta correctamente ok")
finally:
    print("siempre se ejecuta")


def indexOfList(lista:list):
    try: 
        print(lista[5])
    except:
        print("esta fuera de rango")


listaGlobal = [1,2131,2]
indexOfList(listaGlobal)

### mejoramos los errores

def indexOfListv2(lista:list):
    try:
        lista.pop()

    except Exception as error:
        print("Este es el error =>" error)
indexOfList(listaGlobal)















