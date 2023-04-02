import pandas as pd
print("Esta es la version de pandas: "+pd.__version__)
df_cliente = pd.read_csv('./input/Datos_csv.csv')
df_cliente.head()

df_prov = pd.read_csv('./input/DATOS_CVS2.csv')
df_prov.head()

#Utilizar Merge para juntar los dataframes.
df_ambas = df_prov.merge(df_cliente, left_on="ID",right_on="ID_Cli")
df_ambas.head()

#Añadir columna con un solo valor único
df_ambas['Pais'] = "Perú"
df_ambas.head()

#Definimos una función para una nueva columna
def get_observacion(n:int):
    if n>5:
        return "Precio medio"
    else:
        return "Precio normal"

df_ambas['Observacion'] = df_ambas.Precio.apply(get_observacion)



