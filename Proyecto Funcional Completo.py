#Allan Stiven Ramos Lopez
#Carne: 7590-25-10622
#Avance de Proyecto 05 - Pila, cola, ordenamientos

from collections import deque

#Aqui colocamos todas las funciones que utilizaremos en el programa

#calculamos el promedio sumando las notas y diviendo en 3
def promedio_notas(n1, n2, n3):
    return (n1 + n2 + n3) / 3

#lee notas para asignarle un valor a las variables n1, n2 y n3
def leer_notas():
    while True:
        n1 = int(input("Ingrese nota 1 (0 a 100): "))
        if 0 <= n1 <= 100:
            break
    while True:
        n2 = int(input("Ingrese nota 2 (0 a 100): "))
        if 0 <= n2 <= 100:
            break
    while True:
        n3 = int(input("Ingrese nota 3 (0 a 100): "))
        if 0 <= n3 <= 100:
            break
    return n1, n2, n3

#Esta funcion agrega un alumno con un curso y nos indica que se guardo correctamente
def agregar_alumno(lista, historial, cola_revision):
    nombre = input("Ingrese nombre del alumno: ")
    curso = input("Ingrese curso del alumno: ")
    n1, n2, n3 = leer_notas()
    prom = promedio_notas(n1, n2, n3)
    alumno = {"nombre": nombre, "curso": curso, "notas": [n1, n2, n3], "promedio": prom}
    lista.append(alumno)
    historial.append(f"Se agrego al alumno {nombre}")
    cola_revision.append(nombre)
    print("Alumno agregado correctamente.\n")

#Mostramos a los alumnos en una lista
def mostrar_alumnos(lista):
    if not lista:
        print("No hay alumnos registrados.\n")
        return
    for i, alumno in enumerate(lista, 1):
        print(f"{i}. {alumno['nombre']} - Curso: {alumno['curso']} - Promedio: {round(alumno['promedio'], 2)}")

#Promedio general
def calcular_promedio_general(lista):
    if len(lista) == 0:
        print ("Error: 0 alumnos registrados.")
        return
    
    suma = 0 
    for alumno in lista:
        suma += alumno["promedio"]
    promedio_general = suma/len(lista)
    print(f"Promedio general: {promedio_general:.2f}\n")

#Promedio de cada alumno
def mostrar_promedio_alumno(lista):
    if len(lista) == 0:
        print("Error: 0 alumnos registrados.")
        return
    
    print("Promedio de cursos de cada alumno individualmente.")
    for alumno in lista:
        print(f"-{alumno['nombre']}: {alumno['promedio']:.2f}")
    print("")

#Ordenamiento por busqueda binaria.
def busqueda_binaria(lista, curso_buscado):
    if not lista:
        return None
    
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda+derecha)//2
        curso_actual = lista[medio]["curso"].lower()

        if curso_actual == curso_buscado.lower():
            return lista[medio]
        elif curso_actual < curso_buscado.lower():
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return None


#Muestra los promedios de cada alumno y tambien el promedio general.
def mostrar_todos_promedios(lista):
    if len(lista) == 0:
        print("Error: 0 alumnos registrados.")

    suma = 0
    print("Promedio por alumnos:")
    for alumno in lista:
        print(f"{alumno['nombre']}: {alumno['promedio']:.2f} ")
        suma += alumno["promedio"]
    promedio_general = suma/len(lista)
    print(f"\nPromedio general: {promedio_general:.2f}\n")

#Buscamos alumnos de manera lineal
def buscar_alumno(lista, nombre):
    for alumno in lista:
        if alumno["nombre"].lower() == nombre.lower():
            return alumno
    return None

#Actualiza notas de un alumno en especifico
def actualizar_notas(lista, historial):
    nombre = input("Ingrese el nombre del alumno a actualizar: ")
    alumno = buscar_alumno(lista, nombre)
    if alumno:
        n1, n2, n3 = leer_notas()
        alumno["notas"] = [n1, n2, n3]
        alumno["promedio"] = promedio_notas(n1, n2, n3)
        historial.append(f"Se actualizaron las notas de {nombre}")
        print("Notas actualizadas correctamente.\n")
    else:
        print("Alumno no encontrado.\n")

#Eliminamos un alumno poniendo su nombre
def eliminar_alumno(lista, historial):
    nombre = input("Ingrese el nombre del alumno a eliminar: ")
    alumno = buscar_alumno(lista, nombre)
    if alumno:
        lista.remove(alumno)
        historial.append(f"Se elimino al alumno {nombre}")
        print("Alumno eliminado correctamente.\n")
    else:
        print("Alumno no encontrado.\n")

#Eliminamos el ultimo alumno en entrar (como una pila)
def eliminar_ultimoalumno(lista, historial):
    if lista:
        alumno = lista.pop()
        historial.append(f"Se elimino al ultimo alumno ingresado: {alumno['nombre']}")
        print(f"Se elimino correctamente al ultimo alumno: {alumno['nombre']}\n")
    else:
        print("No hay alumnos en la lista.\n")

#Mostramos la estadistica de cuantos alumnos aprobados y reprobados tengamos
def mostrar_estadisticas(lista):
    aprobados = sum(1 for alumno in lista if alumno["promedio"] >= 61)
    reprobados = len(lista) - aprobados
    print(f"Total de alumnos: {len(lista)}")
    print(f"Aprobados: {aprobados}")
    print(f"Reprobados: {reprobados}\n")

#Muestra la ultima accion realizada
def ver_historial(historial):
    if historial:
        print("Ultima accion realizada:", historial.pop())
    else:
        print("Historial vacio.\n")

#Atiende a los alumnos en orden de cola de pila
def atender_revision(cola_revision):
    if cola_revision:
        print("Atendiendo revision de:", cola_revision.popleft())
    else:
        print("No hay alumnos en cola de revision.\n")

#Ordena a los alumnos en burbuja por medio del promedio
def ordenar_burbuja(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j]["promedio"] > lista[j + 1]["promedio"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    print("Lista ordenada con burbuja.\n")

#Funcion para ordenar la lista basandose en el metodo de insercion
def ordenar_insercion(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j]["promedio"] > clave["promedio"]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    print("Lista ordenada con insercion.\n")

#Algoritmo donde ejecutamos todas las funciones
def main():
    alumnos = []
    historial = []
    cola_revision = deque()

    while True:
        print("\nGestor De Notas Academicas")
        print("1. registrar nuevo curso")
        print("2. mostrar todos los cursos y notas")
        print("3. calcular promedio general")
        print("4. contar cursos aprobados y reprobados")
        print("5. buscar curso por nombre (busqueda lineal)")
        print("6. actualizar nota de un curso")
        print("7. eliminar un curso")
        print("8. ordenar un curso por nota (ordenamiento burbuja)")
        print("9. ordenar cursos por nombre (ordenamiento insercion)")
        print("10. buscar curso por nombre (busqueda binaria)")
        print("11. simular cola de solicitudes de revision")
        print("12. mostrar historial de cambios (pila)")
        print("13. salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            agregar_alumno(alumnos, historial, cola_revision)
        elif opcion == "2":
            mostrar_alumnos(alumnos)
        elif opcion == "3":
            mostrar_todos_promedios(alumnos)
        elif opcion == "4":
            mostrar_estadisticas(alumnos)
        elif opcion == "5":
            nombre = input("Ingrese el nombre del alumno a buscar: ")
            alumno = buscar_alumno(alumnos, nombre)
            if alumno:
                print(f"{alumno['nombre']} - Curso: {alumno['curso']} - Promedio: {round(alumno['promedio'], 2)}")
            else:
                print("Alumno no encontrado.\n")
        elif opcion == "6":
            actualizar_notas(alumnos, historial)
        elif opcion == "7":
            eliminar_alumno(alumnos, historial)
        elif opcion == "8":
            ordenar_burbuja(alumnos)
        elif opcion == "9":
            ordenar_insercion(alumnos)
        elif opcion == "10":
            busqueda_binaria(alumnos, nombre)
        elif opcion == "11":
            atender_revision(cola_revision)
        elif opcion == "12":
            ver_historial(historial)
        elif opcion == "13":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida.\n")

if __name__ == "__main__":
    main()
