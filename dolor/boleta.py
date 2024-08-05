#By Felipe Araya

def abrir_fichero():
    f = open("SetDePruebas.txt", "r", encoding='UTF-8')
    datos = f.read().strip().replace("\n"," ").replace("\t"," ").split(" ")
    f.close()
    return datos

def limpieza(datos):
    datos = list(filter(None, datos))

    return datos

def busca_caso(datos):
    for dato in datos:
        busca = "3688580-4"
        if dato == busca:
            posicion = datos.index(busca)
            indice = int(posicion)
            caso = []
            while len(caso) <= 30:
                caso.append(datos[indice])
                indice =+ 1
            print(caso)

if __name__ == "__main__":
    datos = abrir_fichero()
    datos = limpieza(datos)
    caso = busca_caso(datos)
