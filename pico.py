def abrir_fichero():
    # Abre el archivo en modo lectura ('r' significa lectura)
    f = open("guias.dat", "r", encoding='UTF-8')
    # Realiza operaciones de lectura en el archivo
    guias = f.read().rstrip()
    f.close()
    return guias

if __name__ == "__main__":
    guias = abrir_fichero()
    print(guias)
    