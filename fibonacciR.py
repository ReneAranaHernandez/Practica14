print("Programa que dado un numero de el resultado basado en la serie de Fibonacci")
print("Hecho por Rene Arana Hernandez y Gadiel Alberto Lopez Morales")
n = int(input("Ingrese la cantidad de términos de la serie de Fibonacci (n > 1): "))

a, b = 0, 1
count = 1

if n > 1:
    print("Serie de Fibonacci:")
    print(a)

    while count < n:
        print(b) 
        a, b = b, a + b
        count += 1
else:
    print("Por favor, ingrese un número mayor que 1.")
