#
#    1.Realizar un programa que ingrese sus datos personales e imprimirlos,
#    poner en comentario su nombre completo. 
#
bienvenido = """*****************************************************************************************************
*****************************************************************************************************
  -------  ------- -------- |\       |  \            / -------- |\ 	 | -------  ------    -------
  |      |    |    |        | \      |   \          /  |	| \      |    |     |     \   |     |
  |      |    |    |	    |  \     |    \        /   |        |  \     |    |     |      |  |     |
  |------     |    |------  |   \    |     \      /    |------  |   \    |    |     |      |  |     |
  |      |    |    |        |    \   |      \    /     |        |    \   |    |     |      |  |     |
  |      |    |    |        |	  \  |       \  /      |        |     \  |    |     |     /   |     | 
  -------  ------- -------- |      \ |        \/       -------- |      \ | -------- ------    -------
******************************************************************************************************
******************************************************************************************************"""
print(bienvenido)

print("Tenemos para usted multiples opciones donde deberá escoger qué opción desea...")
opciones = """
    1. Imprimir sus datos
    2. Calcular el área de un triangulo, circulo y rectangulo
    3. Ingresar tres valores para sumar, restar, multiplicar y dividir 
    4. Tipo de dato de lo que se va a ingresar 
    5. Ruta donde se encuentra trabajando
    6. Calcular la suma del valor digitado hasta ese número 
    7. Comparar numeros
    8. Contraseña: Ingresar a su usuario
"""
print(opciones)
op = int(input("Seleccione un numero: "))



#
# 1. Realizar un programa que ingrese sus datos personales e imprimirlos, poner en comentario su nombre completo
# 
if type(op) == int:
    if op==1:
        nombre = input("Bienvenido, por favor ingrese sus datos: ")
        # Mi nombre es: Renzo Hubert Gutiérrez Ramos 
        print("Sus datos son: ",nombre)


#
#    2.Calcule el área de un círculo, triángulo y cuadrado con radio ingresado
#    desde el teclado
#
    elif op == 2:
        radio = int(input("Bienvenido, por favor ingrese un valor para el radio - Area de Circulo: "))
        base = int(input("Ingrese valor para Base - Area de Triangulo: "))
        altura = int(input("Ingrese valor para Altura - Area de Triangulo: "))
        lado = int(input("Ingrese el valor de un lado de un cuadrado - Area de un cuadrado"))
        pi = 3.14
        areacirculo = pow(radio,2)*pi
        areatriangulo = (base * altura)/2
        areacuadrado = pow(lado,2)
        print("El valor del área de un circulo es: ", areacirculo)
        print("El valor del área de un triangulo es: ", areatriangulo)
        print("El valor del área de un cuadrado es: ", areacuadrado)


#
#   3.Ingrese 3 valores y realice las operaciones de suma, resta, multiplicación, división y división entera.
#
    elif op == 3:
        valor1 = int(input("Ingrese el primer valor: "))
        valor2 = int(input("Ingrese el segundo valor: "))
        valor3 = int(input("Ingrese el tercer valor: "))

        suma = valor1+valor2+valor3
        resta = (valor1-valor2)-valor3
        multiplicacion = valor1*valor2*valor3
        division = (valor1/valor2)/3
        divisionEntera = (valor1//valor2)//valor3

        print("La suma es: ",suma," - La resta es: ",resta," - La multiplicacion es: ",multiplicacion, " - la division es: ",
        division, " - la division entera es: ",divisionEntera)


#
#   4.Ingrese el valor e imprima el tipo de dato 
# 
    elif op==4:
        valor = input("Ingrese un valor para saber el tipo de dato: ")
        print(type(valor))


#
#   5.Realice un programa que imprima la ruta completa donde se encuentra trabajando
#   Nota: agregar el siguiente código
#   1. import sys
#   2. variable = sys.argv[0]
    elif op == 5:
        import sys 
        ruta = sys.argv[0]
        print("Esta es la ruta donde estás trabajando: ",ruta)

#
#   6. Realice un programa que calcule la suma de los números hasta el valor ingresado
#   Ejemplo: si se ingresa 5 se tendrá que calcular 1+2+3+4+5... etc
# 
    elif op == 6:
        numero1 = int(input("Ingresa un valor para sumar hasta ese número: "))
        suma = 0
        for i in range(numero1):
            resultado = suma + i + 1 
            suma = resultado 
            print("El valor de i es: ", i, "El valor de la suma es: ", suma)
        print("El resultado total es: ", suma)

#
#   7.Realizar un programa que lea 2 números por teclado y determine los siguientes aspectos
#   - Si los dos numeros son iguales
#   - Si los dos numeros son diferentes
#   -Si el primero es mayor que el segundo
#   -Si el segundo es mayor o igual que el primero 

    elif op == 7:
        variable1 = int(input("Ingrese el primer numero: "))
        variable2 = int(input("Ingrese el segundo numero: "))
        if(variable1 == variable2):
            print("Las variables que colocaste son iguales")
        elif(variable1 != variable2):
            print("Las variables son diferentes")   
            if(variable1 > variable2):
                print(f"La primera variable {variable1} es mayor que la segunda variable {variable2}")
            elif(variable2 >= variable1):
                print(f"La seguunda variable {variable2} es menor o igual que la primera variable {variable1}")

#
#   8.Escribir un programa que almacene la cadena de caracteres CONTRASEÑA en una variable, pregunte al usuario por la contraseña
#   e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta
#   las mayusculas y minusculas
#

    elif op == 8:
        contraseña = []
        contraseñaNueva = input("Escriba su nueva contraseña: ")
        contraseña.append(contraseñaNueva)
        contraseñaNueva = input("Escriba su contraseña para volver a afirmar que es usted: ")
        if(contraseñaNueva == contraseña[0]):
            print("Bienvenido, acabamos de confirmar que es usted")
        else:
            print("Lo sentimos, no podemos ingresar a tu cuenta")


#
#   9.Defina una lista con al menos 4 elementos que a su vez sean tuplas que tengan la siguiente estructura ('nombre', 'edad', 'dni')
#   y otra que sea una lista de DNI's
#   -Realizar un programa que filtre a la persona mayores de edad y a los que cumplen esa opción verificar que su dni se encuentre
#   ahi, por ultimo imprimir el nombre de las personas que cumplen las condiciones anteriores
#   -Definir una lista vacia, que luego se agregue el elemento que cumplio todas las condiciones

lista9 = [('nombre','edad', 'dni'), ('DNIs')]
    


