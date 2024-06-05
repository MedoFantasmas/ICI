def abrir_fichero():
    try:
        # Abre el archivo en modo lectura ('r' significa lectura)
        f = open("guias.dat", "r", encoding='UTF-8')
        # Realiza operaciones de lectura en el archivo
        guias = f.read().strip().split(",")
        print(guias)
        f.close()
    except FileNotFoundError:
        print("El archivo no existe")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    return guias

def buscar(guias):
    for x in guias:
        i = 22
        for y in guias[i]:
            if guias[7] == 7:
                datos = datos.append(guias[i:i + 18])
            else:
                pass
    return datos

def mostrar(extracción):
    print(extraccion)

if __name__ == "__main__":
    guias = abrir_fichero()
    extraccion = buscar(guias)
    mostrar(extraccion)
