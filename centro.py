
CONTRASENA = "CHICKEN"
productos = []
# Solicitar la contraseña al inicio
contrasena = input("Ingrese la contraseña: ")
if contrasena != CONTRASENA:
    print("Contraseña incorrecta. Salir.")
else:
    # Menú principal
    while True:
        print("Programa que gestiona productos en inventario")
        print("Hecho por Rene Arana Hernandez y Gadiel Alberto Lopez Morales\n")
        print("\n1. Agregar Producto (Alta)")
        print("2. Consultar Productos (Mostrar)")
        print("3. Modificar Producto (Editar)")
        print("4. Eliminar Producto (Borrar)")
        print("5. Salir")
        opcion = input("Elija una opción: ")

        if opcion == "1":  # Agregar Producto
            nombre = input("Nombre del producto: ")
            cantidad = input("Cantidad: ")
            precio = input("Precio: ")
            producto = nombre + " - " + cantidad + " - " + precio
            productos.append(producto)
            print("Producto agregado.")

        elif opcion == "2":  # Consultar Productos
            if len(productos) == 0:
                print("No hay productos.")
            else:
                print("Producto | Cantidad | Precio unitario")
                for producto in productos:
                    print(producto)

        elif opcion == "3":  # Modificar Producto
            if len(productos) == 0:
                print("No hay productos para modificar.")
            else:
                print("Productos actuales:")
                for i, producto in enumerate(productos, 1):
                    print(f"{i}. {producto}")
                indice = int(input("¿Qué producto desea modificar? (1, 2, 3...): ")) - 1
                if 0 <= indice < len(productos):
                    nuevo_nombre = input("Nuevo nombre: ")
                    nueva_cantidad = input("Nueva cantidad: ")
                    nuevo_precio = input("Nuevo precio: ")
                    productos[indice] = nuevo_nombre + " - " + nueva_cantidad + " - " + nuevo_precio
                    print("Producto modificado.")
                else:
                    print("Producto no encontrado.")

        elif opcion == "4":  # Eliminar Producto
            if len(productos) == 0:
                print("No hay productos para eliminar.")
            else:
                print("Productos actuales:")
                for i, producto in enumerate(productos, 1):
                    print(f"{i}. {producto}")
                indice = int(input("¿Qué producto desea eliminar? (1, 2, 3...): ")) - 1
                if 0 <= indice < len(productos):
                    productos.pop(indice)
                    print("Producto eliminado.")
                else:
                    print("Producto no encontrado.")

        elif opcion == "5":  # Salir
            print("Saliendo...")
            break

        else:
            print("Opción no válida.")
