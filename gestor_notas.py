#Allan Stiven Ramos Lopez
#Carne 7590-25-10622

from collections import deque

#lee una nota validando que sea un numero entre 0 y 100
def leer_nota():
    while True:
        try:
            nota = int(input("Ingrese la nota obtenida: "))
            if 0 <= nota <= 100:
                return nota
        except ValueError:
            #si el usuario ingresa algo que no es numero se repite la solicitud
            pass

#agrega un alumno con su curso y nota a la lista y registra la accion en historial y cola de revision
def agregar_alumno(lista, historial, cola_revision):
    nombre_alumno = input("Ingrese el nombre del alumno: ").strip()
    if not nombre_alumno:
        print("El nombre no puede estar vacío")
        return

    curso = input("Ingrese el nombre del curso: ").strip()
    if not curso:
        print("El nombre del curso no puede estar vacío")
        return

    nota = leer_nota()
    registro = {"alumno": nombre_alumno, "curso": curso, "nota": nota}
    lista.append(registro)
    historial.append(f"Se agregó: {nombre_alumno} - {curso} - Nota: {nota}")
    cola_revision.append(f"{nombre_alumno} ({curso})")
    print("Alumno registrado con éxito\n")

#muestra todos los alumnos, cursos y notas si hay registros
def mostrar_cursos(lista):
    if not lista:
        print("No hay alumnos registrados\n")
        return
    print("Alumnos registrados:")
    for i, r in enumerate(lista, 1):
        print(f"{i}. Nombre: {r['alumno']} - Curso: {r['curso']} - Nota: {r['nota']}")
    print("")

#calcula el promedio general de todas las notas y lo muestra con dos decimales
def calcular_promedio_general(lista):
    if not lista:
        print("No hay alumnos registrados\n")
        return
    suma = sum(r["nota"] for r in lista)
    promedio = suma / len(lista)
    print(f"Promedio general: {promedio:.2f}\n")

#cuenta cuantos alumnos aprobaron y reprobaron (nota >= 60)
def contar_aprobados_reprobados(lista):
    if not lista:
        print("No hay alumnos registrados\n")
        return
    aprobados = sum(1 for r in lista if r["nota"] >= 60)
    reprobados = len(lista) - aprobados
    print(f"Alumnos aprobados: {aprobados}")
    print(f"Alumnos reprobados: {reprobados}\n")

#busca alumnos o cursos por coincidencia parcial
def buscar_curso(lista):
    if not lista:
        print("No hay alumnos registrados\n")
        return
    texto = input("Ingrese el nombre del alumno o curso a buscar: ").lower()
    encontrado = False
    for r in lista:
        if texto in r["alumno"].lower() or texto in r["curso"].lower():
            print(f"Encontrado: {r['alumno']} - {r['curso']} - Nota: {r['nota']}\n")
            encontrado = True
    if not encontrado:
        print("No se encontró ningún registro\n")

#actualiza la nota de un alumno en un curso
def actualizar_curso(lista, historial):
    if not lista:
        print("No hay alumnos registrados\n")
        return
    nombre = input("Ingrese el nombre del alumno: ")
    curso = input("Ingrese el curso: ")
    for r in lista:
        if r["alumno"].lower() == nombre.lower() and r["curso"].lower() == curso.lower():
            nueva_nota = leer_nota()
            anterior = r["nota"]
            r["nota"] = nueva_nota
            historial.append(f"Se actualizó: {nombre} - {curso} - Nota anterior: {anterior} -> Nueva nota: {nueva_nota}")
            print("Nota actualizada correctamente\n")
            return
    print("No se encontró el alumno o curso indicado\n")

#elimina un registro
def eliminar_curso(lista, historial):
    if not lista:
        print("No hay alumnos registrados\n")
        return
    nombre = input("Ingrese el nombre del alumno: ")
    curso = input("Ingrese el curso: ")
    for r in lista:
        if r["alumno"].lower() == nombre.lower() and r["curso"].lower() == curso.lower():
            confirm = input("¿Está seguro que desea eliminarlo (s/n)?: ").lower()
            if confirm == "s":
                lista.remove(r)
                historial.append(f"Se eliminó: {nombre} - {curso} - Nota: {r['nota']}")
                print("Registro eliminado correctamente\n")
            else:
                print("Eliminación cancelada\n")
            return
    print("No se encontró el registro indicado\n")

#ordenar por nota descendente (burbuja)
def ordenar_burbuja(lista):
    if not lista:
        print("No hay alumnos registrados\n")
        return
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j]["nota"] < lista[j + 1]["nota"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    print("Registros ordenados por nota:")
    for i, r in enumerate(lista, 1):
        print(f"{i}. {r['alumno']} - {r['curso']} - Nota: {r['nota']}")
    print("")

#ordenar por nombre de alumno (inserción)
def ordenar_insercion(lista):
    if not lista:
        print("No hay alumnos registrados\n")
        return
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j]["alumno"].lower() > clave["alumno"].lower():
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    print("Registros ordenados por nombre de alumno:")
    for i, r in enumerate(lista, 1):
        print(f"{i}. {r['alumno']} - {r['curso']} - Nota: {r['nota']}")
    print("")

#búsqueda binaria por nombre de alumno
def busqueda_binaria(lista):
    if not lista:
        print("No hay alumnos registrados\n")
        return
    nombre = input("Ingrese el nombre del alumno a buscar: ").lower()
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        actual = lista[medio]["alumno"].lower()
        if actual == nombre:
            print(f"Encontrado: {lista[medio]['alumno']} - {lista[medio]['curso']} - Nota: {lista[medio]['nota']}\n")
            return
        elif actual < nombre:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    print("Alumno no encontrado\n")

#simula una cola de revisión
def simular_cola_revision(cola_revision):
    print("Ingrese solicitudes de revisión (escriba 'fin' para terminar):")
    while True:
        curso = input("> ")
        if curso.lower() == "fin":
            break
        cola_revision.append(curso)
    if not cola_revision:
        print("No hay solicitudes para procesar\n")
        return
    print("\nProcesando solicitudes:")
    while cola_revision:
        print(f"Revisando: {cola_revision.popleft()}")
    print("")

#muestra el historial (como pila)
def mostrar_historial(historial):
    if not historial:
        print("Historial vacío\n")
        return
    print("Historial de cambios recientes:")
    for i, accion in enumerate(reversed(historial), 1):
        print(f"{i}. {accion}")
    print("")

#menú principal
def main():
    registros = []
    historial = []
    cola_revision = deque()

    while True:
        print("\nGestor de Alumnos y Cursos")
        print("1. Registrar nuevo alumno")
        print("2. Mostrar todos los registros")
        print("3. Calcular promedio general")
        print("4. Contar aprobados y reprobados")
        print("5. Buscar alumno o curso")
        print("6. Actualizar nota")
        print("7. Eliminar registro")
        print("8. Ordenar por nota (burbuja)")
        print("9. Ordenar por nombre (inserción)")
        print("10. Buscar alumno (búsqueda binaria)")
        print("11. Simular cola de revisión")
        print("12. Mostrar historial")
        print("13. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_alumno(registros, historial, cola_revision)
        elif opcion == "2":
            mostrar_cursos(registros)
        elif opcion == "3":
            calcular_promedio_general(registros)
        elif opcion == "4":
            contar_aprobados_reprobados(registros)
        elif opcion == "5":
            buscar_curso(registros)
        elif opcion == "6":
            actualizar_curso(registros, historial)
        elif opcion == "7":
            eliminar_curso(registros, historial)
        elif opcion == "8":
            ordenar_burbuja(registros)
        elif opcion == "9":
            ordenar_insercion(registros)
        elif opcion == "10":
            busqueda_binaria(registros)
        elif opcion == "11":
            simular_cola_revision(cola_revision)
        elif opcion == "12":
            mostrar_historial(historial)
        elif opcion == "13":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida\n")

if __name__ == "__main__":
    main()

