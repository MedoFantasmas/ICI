#Hecho por Felipe Araya
#19/08/24

import os

def limpiarconsola():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def lee_fichero(archivo):
    f = open(archivo, "r", encoding = "UTF-8")
    datos = f.read().rstrip().replace("\n","-").split("-")
    datos = list(filter(None, datos))
    return datos

def busqueda(datos):
    print(datos)
    diccionario = {}
    for dato in datos:
        if dato == "Mejores marcas de 2024":
            pass
 
def función_uno():
    pass 
   
# Código que solo se ejecuta cuando se ejecuta el script directamente.
if __name__ == "__main__":
    limpiarconsola()
    archivos = ["wr100.txt", "wr200.txt"]
    for archivo in archivos:
        datos = lee_fichero(archivo)
        mejores = busqueda(datos)
