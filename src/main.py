from ShopMenu import ShopMenu, Shop
from DeveloperMenu import DeveloperMenu
import os as console
from Input import Input

def help_mode() -> None:
    """
        Show help about of program mode
    """
    # Print help information
    print(
        """
        [ AYUDA ]
        Modo Administrador: Gestionamiento de la tienda de peliculas
        Modo Desarrollador: Testing de algoritmos. Pruebas de complejidad espacial y temporal.
        """
    )
    # Pause execution of program
    console.system("pause > nul")

def main() -> None:
    shop = Shop()
    shop_menu = ShopMenu(shop)
    developer_menu = DeveloperMenu(shop)

    while True:
        console.system("cls")
        print(
            "[MODO DE ACCESO]\n",
            "1.- Administrador\n",
            "2.- Desarrollador\n",
            "3.- Ayuda\n"
            "4.- Salir\n",
            "Aplicación creada por: KRAMER\n",
            sep=''
        )

        option = Input.numeric("Opcion: ", 1, 1)

        match option:

            case '1':
                shop_menu.print()

            case '2':
                developer_menu.print()

            case '3':
                help_mode()

            case '4':
                break

            case _:
                continue

if __name__ == "__main__":
    main()