from ShopMenu import ShopMenu, Shop
from DeveloperMenu import DeveloperMenu
import os as console
from Input import Input

def main() -> None:
    shop = Shop()
    shop_menu = ShopMenu(shop)
    developer_menu = DeveloperMenu(shop)

    while True:
        console.system("cls")

        print(
            "[ PLAY-MOVIE ]\n",
            "1.- Administrador\n",
            "2.- Desarrollador\n",
            "3.- Salir\n",
            sep=''
        )

        option = Input.numeric("Modo: ", 1, 1)

        console.system("cls")

        match option:

            case '1':
                shop_menu.print()

            case '2':
                developer_menu.print()

            case '3':
                break

            case _:
                continue

if __name__ == "__main__":
    main()