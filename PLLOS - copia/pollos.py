import matplotlib.pyplot as plt

def lectura_datos(): #Lee los datos del archivo.
    f = open("protocolo_vigilancia.txt", "r", encoding='UTF-8')
    datos = f.read().strip().replace("\n",",").replace("-","").split(",")
    f.close()
    return datos

def h5ni_region(datos): #Obtiene la cantidad de casos de secuenciación por región de H5N1.
    i = 8
    j = 3
    regiones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while i <= 51850:
        if datos[i] == 'H5N1':
            if datos[j] == "Arica":
                regiones[0] += 1
            elif datos[j] == "Tarapaca":
                regiones[1] += 1
            elif datos[j] == "Antofagasta":
                regiones[2] += 1
            elif datos[j] == "Atacama":
                regiones[3] += 1
            elif datos[j] == "Coquimbo":
                regiones[4] += 1
            elif datos[j] == "Valparaiso":
                regiones[5] += 1
            elif datos[j] == "Metropolitana":
                regiones[6] += 1
            elif datos[j] == "O Higgins":
                regiones[7] += 1
            elif datos[j] == "Maule":
                regiones[8] += 1
            elif datos[j] == "Nuble":
                regiones[9] += 1
            elif datos[j] == "Bio Bio":
                regiones[10] += 1
            elif datos[j] == "Araucania":
                regiones[11] += 1
            elif datos[j] == "Los Rios":
                regiones[12] += 1
            elif datos[j] == "Los Lagos":
                regiones[13] += 1
            elif datos[j] == "Aysen":
                regiones[14] += 1
            elif datos[j] == "Magallanes":
                regiones[15] += 1
            else: continue
        i += 10
        j += 10
    return regiones

def neg_abr2023(datos): #Obtiene la cantidad de casos negativos para abril del 2023.
    i = 2
    j = 9
    caso_neg = 0
    while i <= 51850:
        x = datos[i]
        str_x = str(x)
        if str_x[3] == "4":
            if str_x[7] == "3":
                if datos[j] == "Negativo":
                    caso_neg += 1
        i += 10
        j += 10
    return caso_neg

def neg_yunco(datos): #Obtiene cantidad de casos negativos de la especie “Yunco”.
    i = 5
    j = 9
    yunco = 0
    while i <= 51850:
        if datos[i] == "Yunco":
            if datos[j] == "Negativo":
                yunco += 1
        i += 10
        j += 10
    return yunco

def neg_lile_jun2023(datos): #Obtiene la cantidad de casos negativos para la especie “Lile” para junio del 2023.
    pass

def incidencias(datos): #Obtiene y grafica la cantidad de casos negativos de las especies: Gaviota, Piquero, Salteador, Pelicano y Guanay.
    i = 5
    j = 9
    especie = ["Gaviota", "Piquero", "Salteador", "Pelicano", "Guanay"]
    cantidad = [0, 0, 0, 0, 0]
    while i <= 51850:
        if datos[j] == "Negativo":
            if datos[i] == especie[0]:
                cantidad[0] += 1
            elif datos[i] == especie[1]:
                cantidad[1] += 1
            elif datos[i] == especie[2]:
                cantidad[2] += 1
            elif datos[i] == especie[3]:
                cantidad[3] += 1
            elif datos[i] == especie[4]:
                cantidad[4] += 1
        i += 10
        j += 10

    plt.xlabel("Especie")
    plt.ylabel("Cantidad de casos")

    plt.bar(especie, cantidad)

    plt.show()

def genera_salida(casos_sec, casos_neg_abr, casos_neg_yunco, casos_neg_lile_jul): #Genera todo lo que será ,ostrado de salida.
    f = open("resultadoS3.txt", "w")
    f.write("Autores: Felipe Araya D. - Jose Cares C.\n")
    f.write("Cantidad de casos de secuenciacion por region:\n")
    f.write("    Arica: ")
    f.write(str(casos_sec[0]))
    f.write("\n    Tarapaca: ")
    f.write(str(casos_sec [1]))
    f.write("\n    Antofagasta: ")
    f.write(str(casos_sec[2]))
    f.write("\n    Atacama: ")
    f.write(str(casos_sec[3]))
    f.write("\n    Coquimbo: ")
    f.write(str(casos_sec[4]))
    f.write("\n    Valparaiso: ")
    f.write(str(casos_sec[5]))
    f.write("\n    Region Metropolitana: ")
    f.write(str(casos_sec[6]))
    f.write("\n    O Higgins: ")
    f.write(str(casos_sec[7]))
    f.write("\n    Maule: ")
    f.write(str(casos_sec[8]))
    f.write("\n    Nuble: ")
    f.write(str(casos_sec[9]))
    f.write("\n    Biobio: ")
    f.write(str(casos_sec[10]))
    f.write("\n    La Araucania: ")
    f.write(str(casos_sec[11]))
    f.write("\n    Los Lagos: ")
    f.write(str(casos_sec[12]))
    f.write("\n    Aysen: ")
    f.write(str(casos_sec[13]))
    f.write("\n    Los Rios: ")
    f.write(str(casos_sec[14]))
    f.write("\n    Magallanes: ")
    f.write(str(casos_sec[15]))
    f.write("\n------------------------------------------------------\n")
    f.write("Casos negativos mes abril del 2023: ")
    f.write(str(casos_neg_abr))
    f.write("\n------------------------------------------------------\n")
    f.write("Casos negativos especie Yunco: ")
    f.write(str(casos_neg_yunco))
    f.write("\n------------------------------------------------------\n")
    f.write("Incidencias 06/2023 del 'Lile': ")
    f.write("xxxx")

if __name__ == "__main__":
    datos = lectura_datos()
    casos_sec = h5ni_region(datos)
    casos_neg_abr = neg_abr2023(datos)
    casos_neg_yunco = neg_yunco(datos)
    casos_neg_lile_jul = neg_lile_jun2023(datos)
    genera_salida(casos_sec, casos_neg_abr, casos_neg_yunco, casos_neg_lile_jul)
    incidencias(datos)
#    print(datos)
