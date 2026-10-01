def Mostrar_menu(lista):
    print("Bienvenido al menú de comida rápida. Por favor, elegí una opción:")
    for xd in range(len(lista)):
        print(f"{xd + 1}. {lista[xd]}")

    opcion = input("Elegí una opción: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > len(lista):
        print("Opción no válida, probá de nuevo.")
        opcion = input("Elegí una opción: ")

    return lista[int(opcion) - 1]
