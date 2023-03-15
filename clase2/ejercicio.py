
# Bucle While = Mientras

while False: #Con true, cambiamos a false para que no ejecute
    print("Ejecutando")

## Detenemos la consola por ctrl + C

year_init = int(input("año de inicio de reporte"))
year_end = int(input("año de fin de reporte"))
lista_year_not_report = [2008,2009,2010]

while year_init <= year_end:
    if year_init in lista_year_not_report:
        print(f"este año {year_init} no hay reporte")
    print(f"El reporte de este año {year_init}")
    year_init+=1 # year_init=year_init+1







