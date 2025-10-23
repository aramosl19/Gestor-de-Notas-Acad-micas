#Allan Stiven Ramos Lopez
#Carne 7590-25-10622
#Avance de Proyecto 05 - Pila cola ordenamientos

from collections import deque

#funcion auxiliar usada originalmente en versiones previas
#la mantenemos pero no se usa en este flujo principal
def promedio_notas(n1):
    return n1

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

#agrega un curso con su nota a la lista y registra la accion en historial y cola de revision
def agregar_curso(lista, historial, cola_revision):
    nombre = input("Ingrese el nombre del curso: ")
    if not nombre.strip():
        print("El nombre no puede estar vacio")
        return
    nota = leer_nota()
    curso = {"nombre": nombre, "nota": nota}
    lista.append(curso)
    historial.append(f"Se agrego: {nombre} - Nota: {nota}")
    cola_revision.append(nombre)
    print("Curso registrado con exito\n")

#muestra todos los cursos y sus notas si hay cursos registrados
def mostrar_cursos(lista):
    if not lista:
        print("No hay cursos registrados\n")
        return
    print("Cursos registrados:")
    for i, curso in enumerate(lista, 1):
        print(f"{i}. {curso['nombre']} - Nota: {curso['nota']}")
    print("")

#calcula el promedio general de todas las notas y lo muestra con dos decimales
def calcular_promedio_general(lista):
    if not lista:
        print("No hay cursos registrados\n")
        return
    suma = sum(c["nota"] for c in lista)
    promedio = suma / len(lista)
    print(f"Promedio general: {promedio:.2f}\n")

#cuenta cuántos cursos estan aprobados y cuántos reprobados
#se considera aprobado nota mayor o igual a 60
def contar_aprobados_reprobados(lista):
    if not lista:
        print("No hay cursos registrados\n")
        return
    aprobados = sum(1 for c in lista if c["nota"] >= 60)
    reprobados = len(lista) - aprobados
    print(f"Cursos aprobados: {aprobados}")
    print(f"Cursos reprobados: {reprobados}\n")

#busca cursos por coincidencia parcial sin importar mayusculas o minusculas
def buscar_curso(lista):
    if not lista:
        print("No hay cursos registrados\n")
        return
    nombre = input("Ingrese el nombre del curso: ").lower()
    encontrado = False
    for curso in lista:
        if nombre in curso["nombre"].lower():
            print(f"Curso encontrado: {curso['nombre']} - Nota: {curso['nota']}\n")
            encontrado = True
    if not encontrado:
        print("Curso no encontrado\n")

#actualiza la nota de un curso especifico y registra la accion en el historial
def actualizar_curso(lista, historial):
    if not lista:
        print("No hay cursos registrados\n")
        return
    nombre = input("Ingrese el nombre del curso: ")
    for curso in lista:
        if curso["nombre"].lower() == nombre.lower():
            nueva_nota = leer_nota()
            anterior = curso["nota"]
            curso["nota"] = nueva_nota
            historial.append(f"Se actualizo: {nombre} - Nota anterior: {anterior} -> Nueva nota: {nueva_nota}")
            print("Nota actualizada correctamente\n")
            return
    print("Curso no encontrado\n")

#elimina un curso despues de pedir confirmacion y registra la accion en el historial
def eliminar_curso(lista, historial):
    if not lista:
        print("No hay cursos registrados\n")
        return
    nombre = input("Ingrese el curso a eliminar: ")
    for curso in lista:
        if curso["nombre"].lower() == nombre.lower():
            confirm = input("Esta seguro que desea eliminarlo (s/n): ").lower()
            if confirm == "s":
                lista.remove(curso)
                historial.append(f"Se elimino: {nombre} - Nota: {curso['nota']}")
                print("Curso eliminado correctamente\n")
            else:
                print("Eliminacion cancelada\n")
            return
    print("Curso no encontrado\n")

#ordena los cursos por nota usando ordenamiento burbuja en orden descendente
def ordenar_burbuja(lista):
    if not lista:
        print("No hay cursos registrados\n")
        return
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j]["nota"] < lista[j + 1]["nota"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    print("Cursos ordenados por nota:")
    for i, curso in enumerate(lista, 1):
        print(f"{i}. {curso['nombre']} - Nota: {curso['nota']}")
    print("")

#ordena los cursos por nombre usando metodo de insercion y muestra el resultado
def ordenar_insercion(lista):
    if not lista:
        print("No hay cursos registrados\n")
        return
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j]["nombre"].lower() > clave["nombre"].lower():
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    print("Cursos ordenados por nombre:")
    for i, curso in enumerate(lista, 1):
        print(f"{i}. {curso['nombre']} - Nota: {curso['nota']}")
    print("")

#realiza busqueda binaria por nombre asumiendo que la lista ya esta ordenada por nombre
def busqueda_binaria(lista):
    if not lista:
        print("No hay cursos registrados\n")
        return
    nombre = input("Ingrese el nombre del curso a buscar: ").lower()
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        curso_actual = lista[medio]["nombre"].lower()
        if curso_actual == nombre:
            print(f"Curso encontrado: {lista[medio]['nombre']} - Nota: {lista[medio]['nota']}\n")
            return
        elif curso_actual < nombre:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    print("Curso no encontrado\n")

#simula una cola de solicitudes de revision y procesa cada curso en orden de llegada
def simular_cola_revision(cola_revision):
    print("Ingrese curso para revision (escriba 'fin' para terminar):")
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

#muestra el historial de cambios en orden inverso simulando una pila
def mostrar_historial(historial):
    if not historial:
        print("Historial vacio\n")
        return
    print("Historial de cambios recientes:")
    for i, accion in enumerate(reversed(historial), 1):
        print(f"{i}. {accion}")
    print("")

#funcion principal que presenta el menu y llama a las demas funciones
def main():
    cursos = []
    historial = []
    cola_revision = deque()

    while True:
        print("\nGestor de Cursos")
        print("1. Registrar nuevo curso")
        print("2. Mostrar todos los cursos y notas")
        print("3. Calcular promedio general")
        print("4. Contar cursos aprobados y reprobados")
        print("5. Buscar curso por nombre")
        print("6. Actualizar nota de un curso")
        print("7. Eliminar un curso")
        print("8. Ordenar cursos por nota (burbuja)")
        print("9. Ordenar cursos por nombre (insercion)")
        print("10. Buscar curso por nombre (busqueda binaria)")
        print("11. Simular cola de solicitudes de revision")
        print("12. Mostrar historial de cambios (pila)")
        print("13. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            agregar_curso(cursos, historial, cola_revision)
        elif opcion == "2":
            mostrar_cursos(cursos)
        elif opcion == "3":
            calcular_promedio_general(cursos)
        elif opcion == "4":
            contar_aprobados_reprobados(cursos)
        elif opcion == "5":
            buscar_curso(cursos)
        elif opcion == "6":
            actualizar_curso(cursos, historial)
        elif opcion == "7":
            eliminar_curso(cursos, historial)
        elif opcion == "8":
            ordenar_burbuja(cursos)
        elif opcion == "9":
            ordenar_insercion(cursos)
        elif opcion == "10":
            busqueda_binaria(cursos)
        elif opcion == "11":
            simular_cola_revision(cola_revision)
        elif opcion == "12":
            mostrar_historial(historial)
        elif opcion == "13":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida\n")

if __name__ == "__main__":
    main()
