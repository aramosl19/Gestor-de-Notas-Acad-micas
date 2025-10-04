# Allan Stiven Ramos Lopez
# Carne: 7590-25-10622
# Avance de Proyecto 05 - Pila, cola, ordenamientos

from collections import deque

# Aqui colocamos todas las funciones que utilizaremos en el programa

# calculamos el promedio sumando las notas y diviendo en 3
def promedio_notas(n1, n2, n3):  
    return (n1 + n2 + n3) / 3

# lee notas para asignarle un valor alas variables n1, n2 y n3
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

# Esta funcion agrega un alumno con un curso y nos indica que se guardo correctamente
    
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

# Mostramos a los alumnos en una lista de primero segundo tercero.
def mostrar_alumnos(lista):  
    if not lista:
        print("No hay alumnos registrados.\n")
        return
    for i, alumno in enumerate(lista, 1):
        print(f"{i}. {alumno['nombre']} - Curso: {alumno['curso']} - Promedio: {round(alumno['promedio'], 2)}")
        
# Buscamos alumnos de manera lineal
def buscar_alumno(lista, nombre):
    for alumno in lista:
        if alumno["nombre"].lower() == nombre.lower():
            return alumno
    return None

# Actualiza notas de un alumno en especifico
    
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

# Eliminamos un alumno poniendo su nombre
def eliminar_alumno(lista, historial):  
    nombre = input("Ingrese el nombre del alumno a eliminar: ")
    alumno = buscar_alumno(lista, nombre)
    if alumno:
        lista.remove(alumno)
        historial.append(f"Se elimino al alumno {nombre}")
        print("Alumno eliminado correctamente.\n")
    else:
        print("Alumno no encontrado.\n")

# eliminamos el ultimo alumno en entrar tal que un pop
def eliminar_ultimoalumno(lista, historial):  
    if lista:
        alumno = lista.pop()
        historial.append(f"Se elimino al ultimo alumno ingresado: {alumno['nombre']}")
        print(f"Se elimino correctamente al ultimo alumno: {alumno['nombre']}\n")
    else:
        print("No hay alumnos en la lista.\n")

# Mostramos la estadistica que tengamos de cuantos aluumnos aprobados y reprobados tengamos
def mostrar_estadisticas(lista):  
    aprobados = sum(1 for alumno in lista if alumno["promedio"] >= 61)
    reprobados = len(lista) - aprobados
    print(f"Total de alumnos: {len(lista)}")
    print(f"Aprobados: {aprobados}")
    print(f"Reprobados: {reprobados}\n")

# Muestra la ultima accion realizada
    
def ver_historial(historial):  
    if historial:
        print("Ultima accion realizada:", historial.pop())
    else:
        print("Historial vacio.\n")

# Atiende a los alumnos en orden de cola de pila
def atender_revision(cola_revision):  
    if cola_revision:
        print("Atendiendo revision de:", cola_revision.popleft())
    else:
        print("No hay alumnos en cola de revision.\n")

# Ordena a los alumnos en burbuja por medio del promedio
def ordenar_burbuja(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(n-1-i):
            if lista[j]["promedio"] > lista[j+1]["promedio"]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    print("Lista ordenada con burbuja.\n")

# Funcion para ordenar la lista basandose en el metodo de insercion
def ordenar_insercion(lista):  
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j]["promedio"] > clave["promedio"]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = clave
    print("Lista ordenada con insercion.\n")

# Algoritmo donde ejecutamos todas las funciones
    
def main():
    alumnos = []
    historial = []
    cola_revision = deque()

    while True:
        print("\n--- MENU ---")
        print("1. Agregar alumno")
        print("2. Mostrar alumnos")
        print("3. Buscar alumno")
        print("4. Actualizar notas")
        print("5. Eliminar alumno")
        print("6. Estadisticas")
        print("7. Eliminar ultimo alumno ingresado")
        print("8. Ver historial")
        print("9. Atender revision")
        print("10. Ordenar alumnos por promedio (Burbuja)")
        print("11. Ordenar alumnos por promedio (Insercion)")
        print("12. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            agregar_alumno(alumnos, historial, cola_revision)
        elif opcion == "2":
            mostrar_alumnos(alumnos)
        elif opcion == "3":
            nombre = input("Ingrese el nombre del alumno a buscar: ")
            alumno = buscar_alumno(alumnos, nombre)
            if alumno:
                print(f"{alumno['nombre']} - Curso: {alumno['curso']} - Promedio: {round(alumno['promedio'], 2)}")
            else:
                print("Alumno no encontrado.\n")
        elif opcion == "4":
            actualizar_notas(alumnos, historial)
        elif opcion == "5":
            eliminar_alumno(alumnos, historial)
        elif opcion == "6":
            mostrar_estadisticas(alumnos)
        elif opcion == "7":
            eliminar_ultimoalumno(alumnos, historial)
        elif opcion == "8":
            ver_historial(historial)
        elif opcion == "9":
            atender_revision(cola_revision)
        elif opcion == "10":
            ordenar_burbuja(alumnos)
        elif opcion == "11":
            ordenar_insercion(alumnos)
        elif opcion == "12":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida.\n")

if __name__ == "__main__":
    main()
