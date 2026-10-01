from util import Mostrar_menu

comidaa = ["Pizza", "Hamburguesa", "Pancho", "Pollo Frito", "Papas Fritas", "Tacos", "Sushi", "Sandwich", "Salir"]

print("Bienvenido al menú de comida rápida. Por favor, elegí una opción:")

while True:
    elegida = Mostrar_menu(comidaa)

    if elegida == "Salir":
        print("¡Hasta luego!")
        break

    print("Elegiste:", elegida)