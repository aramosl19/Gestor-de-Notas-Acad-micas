# Allan Stiven Ramos López
# Carné: 7590-25-10622
# Avance Proyecto 03 - Condicionales, contadores, búsqueda lineal y actualización de datos

# Función para calcular promedio
def promedio_notas(n1, n2, n3):
    return (n1 + n2 + n3) / 3

# Subproceso para leer notas con validación
def leer_notas():
    while True:
        n1 = int(input("Ingrese nota 1 condicion de (0 a 100): "))
        if 0 <= n1 <= 100:
            break
    while True:
        n2 = int(input("Ingrese nota 2 condicion de (0 a 100): "))
        if 0 <= n2 <= 100:
            break
    while True:
        n3 = int(input("Ingrese nota 3 condicion de (0 a 100): "))
        if 0 <= n3 <= 100:
            break
    return n1, n2, n3

# Programa principal
def main():
    n = int(input("Ingrese la cantidad de alumnos: "))
    for i in range(1, n + 1):
        n1, n2, n3 = leer_notas()   
        promindi = promedio_notas(n1, n2, n3)
        print("Estudiante", i, "promedio:", round(promindi, 2))

if __name__ == "__main__":
    main()
