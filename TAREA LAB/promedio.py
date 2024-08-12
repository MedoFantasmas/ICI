#By Felipe Araya

def promedio(estudiantes):
    #Calcula promedios de notas.
    promedios = []
    for alumno, notas in estudiantes.items():
        promedio = (sum(notas) / len(notas))
        promedios.append([alumno, promedio])
    return promedios

def nota_max(estudiantes):
    #Calcula nota máxima por estudiante.
    maximos = []
    for alumno, notas in estudiantes.items():
        maximos.append([alumno, max(notas)])
    return maximos

def nota_min(estudiantes):
    #Calcula nota mínima por estudiante.
    minimos = []
    for alumno, notas in estudiantes.items():
        minimos.append([alumno, min(notas)])
    return minimos


def genera_salida(notas_promedio, maximos, minimos):
    print("Estudiante:\tPromedio:\tMaximo:\t\tMinimo:")
    for elemento in notas_promedio:
        print(notas_promedio[0][0])


   
# Código que solo se ejecuta cuando se ejecuta el script directamente. 
if __name__ == "__main__": 
    estudiantes = {"Ana": [8, 9, 7, 10],"Julia": [8, 9, 7, 10],"Adriana": [8, 9, 7, 10],"Benjamín": [8, 9, 7, 10],
                   "Diego": [8, 9, 7, 10], "Juan": [8, 9, 7, 10], "María": [9, 10, 9, 8], "Pedro": [7, 8, 6, 9]}
    notas_promedio = promedio(estudiantes)
    maximos = nota_max(estudiantes)
    minimos = nota_min(estudiantes)
    salida = genera_salida(notas_promedio, maximos, minimos)