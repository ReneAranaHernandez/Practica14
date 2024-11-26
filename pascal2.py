print("Programa que genera el Triángulo de Pascal.")
print("Hecho por Rene Arana Hernandez y Gadiel Alberto Lopez Morales")

filas = int(input("Introduce el número de filas para el Triángulo de Pascal: "))

triangulo = []

for i in range(filas):
    fila = []
    for j in range(i + 1):
        if j == 0 or j == i:
            fila.append(1)
        else:
            fila.append(triangulo[i-1][j-1] + triangulo[i-1][j])
    triangulo.append(fila)

for fila in triangulo:
    print(" ".join(map(str, fila)).center(filas * 3))