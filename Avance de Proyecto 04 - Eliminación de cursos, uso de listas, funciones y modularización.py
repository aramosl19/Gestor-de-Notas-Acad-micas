# Allan Stiven Ramos López
# Carné: 7590-25-10622
# Avance de Proyecto 04 - Eliminación de cursos, uso de listas, funciones y modularización.

# ------------------ Funciones ------------------

# Calcular promedio
def promedio_notas(n1, n2, n3):
    return (n1 + n2 + n3) / 3

# Leer notas con validacion
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

# Agregar alumno
def agregar_alumno(lista):
    nombre = input("Ingrese nombre del alumno: ")
    curso = input("Ingrese curso del alumno: ")
    n1, n2, n3 = leer_notas()
    prom = promedio_notas(n1, n2, n3)
    alumno = {"nombre": nombre, "curso": curso, "notas": [n1, n2, n3], "promedio": prom}
    lista.append(alumno)
    print("Alumno agregado correctamente.\n")

# Mostrar todos los alumnos
def mostrar_alumnos(lista):
    if not lista:
        print("No hay alumnos registrados.\n")
        return
    for i, alumno in enumerate(lista, 1):
        print(f"{i}. {alumno['nombre']} - Curso: {alumno['curso']} - Promedio: {round(alumno['promedio'], 2)}")

# Buscar alumno (búsqueda lineal)
def buscar_alumno(lista, nombre):
    for alumno in lista:
        if alumno["nombre"].lower() == nombre.lower():
            return alumno
    return None

# Actualizar notas de un alumno
def actualizar_notas(lista):
    nombre = input("Ingrese el nombre del alumno a actualizar: ")
    alumno = buscar_alumno(lista, nombre)
    if alumno:
        print("Alumno encontrado. Ingrese las nuevas notas:")
        n1, n2, n3 = leer_notas()
        alumno["notas"] = [n1, n2, n3]
        alumno["promedio"] = promedio_notas(n1, n2, n3)
        print("Notas actualizadas correctamente.\n")
    else:
        print("Alumno no encontrado.\n")

# Eliminar curso (o alumno)
def eliminar_alumno(lista):
    nombre = input("Ingrese el nombre del alumno a eliminar: ")
    alumno = buscar_alumno(lista, nombre)
    if alumno:
        lista.remove(alumno)
        print("Alumno eliminado correctamente.\n")
    else:
        print("Alumno no encontrado.\n")

# Contadores de aprobados y reprobados
def mostrar_estadisticas(lista):
    aprobados = sum(1 for alumno in lista if alumno["promedio"] >= 61)
    reprobados = len(lista) - aprobados
    print(f"Total de alumnos: {len(lista)}")
    print(f"Aprobados: {aprobados}")
    print(f"Reprobados: {reprobados}\n")

# ------------------ Programa principal ------------------
def main():
    alumnos = []
    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar alumno")
        print("2. Mostrar alumnos")
        print("3. Buscar alumno")
        print("4. Actualizar notas")
        print("5. Eliminar alumno")
        print("6. Estadísticas")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_alumno(alumnos)
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
                actualizar_notas(alumnos)
        elif opcion == "5":
                eliminar_alumno(alumnos)
        elif opcion == "6":
                mostrar_estadisticas(alumnos)
        elif opcion == "7":
                print("Saliendo del programa...")
                break
        else:
                print("Opción no válida.\n")

if __name__ == "__main__":
    main()