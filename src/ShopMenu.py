import os as console
from Input import Input
from Categories import Categories
from Shop import Shop, Movie, Client, Filter
from Verifier import Verifier
from EcuadorianIdCard import EcuadorianIdCard
from CreditCard import CreditCard

class ShopMenu:
    def __init__(self, shop: Shop) -> None:
        self.__shop = shop
        pass

    def __select_category(self) -> str:
        is_valid_category = False
        category = int()
        while not is_valid_category:
            console.system("cls")
            Categories.print()
            category = Input.integer("Categoria: ", 1, 2, signed=False)
            is_valid_category = Categories.is_valid(category)

            if not is_valid_category:
                print("Categoria no valida")
                console.system("pause > nul")

        return Categories.select(category)
    
    def __create_movie(self) -> Movie:
        print("[INFORMACION DE LA PELICULA]")
        movie = Movie()
        movie.name = Input.alphanumeric("Titulo: ", 3, 30).lower()
        movie.director = Input.alphabetic("Director: ", 3, 20).lower()
        movie.amount = Input.integer("Cantidad: ", 1, 3, signed=False)
        movie.category = self.__select_category()
        movie.synopsis = Input.alphanumeric("Sinopsis: ", 10, 100)
        movie.purchase_price = Input.floating("Precio venta: ", 1, 6, signed=False)
        movie.rental_price = movie.purchase_price / 2
        
        return movie
    
    def __pay_movie(self) -> Client|None:
        print("[INFORMACION DEL CLIENTE]")
        client = Client()
        client.first_name = Input.alphabetic("Nombre: ", 3, 10, space=False).lower()
        client.last_name = Input.alphabetic("Apellido: ", 3, 10, space=False).lower()
        client.id_card = Input.numeric("Cedula: ", 10, 10)

        while not Verifier.card(EcuadorianIdCard(client.id_card)):
            print("Cedula no valida")
            if Input.string("Desea reintentar (s\\n): ", lambda char: char == 's' or char == 'n', 1, 1) == 's':
                client.id_card = Input.numeric("Cedula: ", 10, 10)
            else:
                return None

        while not Verifier.card(CreditCard(Input.numeric("Tarjeta de credito: ", 16, 16))):
            print("Tarjeta de credito no valida")
            if Input.string("Desea reintentar (s\\n): ", lambda char: char == 's' or char == 'n', 1, 1) == 'n':
                return None

        return client

    def __register_movie(self) -> None:
        movie = self.__create_movie()

        if self.__shop.exist(movie):
            return print("Pelicula ya existe en la tienda")
        
        self.__shop.register_movie(movie)
        print("Pelicula registrada correctamente")

    def __add_movie(self) -> None:
        movie = Movie()
        movie.id = Input.integer("ID de la pelicula: ", 1, 3, signed=False)

        if not self.__shop.exist(movie):
            print("Pelicula no existe en la tienda")
        else:
            movie.amount = Input.integer("Cantidad: ", 1, 3, signed=False)
            self.__shop.add_movie(movie)
            print("Cantidad de peliculas agregada correctamente")

    def __print_movies_list(self) -> None:
        filters = Filter.filters()
        option = len(filters) + 1

        while option > len(filters):
            console.system("cls")
            i = 1
            for filter in filters:
                print(f"{i}.- {filter}")
                i += 1

            option = Input.integer("Filtro: ", 1, 1, signed=False)

        filter = filters[option - 1]

        matching = str()

        match filter:
            case "category":
                matching = self.__select_category()
            
            case "Ninguno":
                pass
                
            case _:
                matching = Input.alphanumeric(f"{filters[option - 1]}: ", 3, 30).lower()

        console.system("cls")
        self.__shop.print_movies_list(Filter(filter, matching))

    def __search_movie(self) -> None:
        position = Input.integer("ID de pelicula: ", 1, 3, signed=False)
        movie = self.__shop.search(position)
        print(movie if movie != None else "Pelicula no existe")

    def __sell_movie(self) -> None:
        movie = Movie()
        movie.id = Input.integer("ID de pelicula: ", 1, 3, signed=False)

        if not self.__shop.exist(movie) or not self.__shop.has_stock(movie):
            return print("ID no existente o no hay stock de la pelicula especificada")

        is_successful_pay = not self.__pay_movie() == None

        if not is_successful_pay:
            return print("Transaccion no exitosa")
        
        if self.__shop.sell_movie(movie):
            print(f"Transaccion exitosa, se le cobra {self.__shop.movies[movie.id - 1].purchase_price}")

    def __rent_movie(self) -> None:
        movie = Movie()
        movie.id = Input.integer("ID de pelicula: ", 1, 3, signed=False)

        if not self.__shop.exist(movie):
            return print("ID no existente o no hay stock de la pelicula especificada")
        
        client = self.__pay_movie()

        if client == None:
            return print("Transaccion fallida")
        
        if self.__shop.rent_movie(movie, client):
            print(f"Transaccion exitosa, se le cobra {self.__shop.movies[movie.id - 1].rental_price}")
        else:
            print("Transaccion fallida: ya ha rentado la pelicula especificada")

    def __return_rent_movie(self) -> None:
        movie = Movie()
        movie.id = Input.integer("Id de pelicula: ", 1, 3, signed=False)

        if not self.__shop.exist(movie):
            return print("Pelicula no existe en la tienda")

        client = Client()
        client.id_card = Input.numeric("Cedula: ", 10, 10)

        while not Verifier.card(EcuadorianIdCard(client.id_card)):
            print("Cedula no valida")
            if Input.string("Desea reintentar (s\\n): ", lambda char: char == 's' or char == 'n', 1, 1) == 's':
                client.id_card = Input.numeric("Cedula: ", 10, 10)
            else:
                return None
        
        if self.__shop.return_movie(movie, client):
            print("Transaccion exitosa")
        else:
            print("Transaccion fallida: [La pelicula no ha sido rentada por el cliente o el cliente no se encuentra en la base de datos]")

    def print(self) -> None:
        while True:
            console.system("cls")

            print(
                "[ TIENDA DE PELICULAS ]",
                "1.- Registrar pelicula\n",
                "2.- Agregar pelicula\n",
                "3.- Lista de peliculas\n",
                "4.- Buscar pelicula\n",
                "5.- Vender pelicula\n",
                "6.- Rentar pelicula\n",
                "7.- Devolver pelicula\n",
                "8.- Salir\n",
                sep=''
            )

            option = Input.numeric("Opcion: ", 1, 1)

            console.system("cls")

            match option:

                case '1':
                    self.__register_movie()

                case '2':
                    self.__add_movie()

                case '3':
                    self.__print_movies_list()

                case '4':
                    self.__search_movie()

                case '5':
                    self.__sell_movie()

                case '6':
                    self.__rent_movie()

                case '7':
                    self.__return_rent_movie()

                case '8':
                    break

                case _:
                    continue

            console.system('pause > nul')