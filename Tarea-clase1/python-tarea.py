#
#    1.Realizar un programa que ingrese sus datos personales e imprimirlos,
#    poner en comentario su nombre completo. 
#

name = input("Bienvenido, por favor ingrese sus datos: ");
# Renzo Hubert Gutiérrez Ramos 
print("Sus datos son: ",name)







#
#    2.Calcule el área de un círculo, triángulo y cuadrado con radio ingresado
#    desde el teclado
#

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


