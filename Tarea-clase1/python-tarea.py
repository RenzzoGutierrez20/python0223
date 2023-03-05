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
        i = 1 
        for i in range(numero1):
            resultado = resultado + i 
            print("valor de i: ",i) 
            print("valor de resultado: ",resultado) 
        print("Ahora, el valor de resultado total es : ",resultado)    








