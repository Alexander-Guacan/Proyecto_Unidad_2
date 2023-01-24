import os as console
from Input import Input
from Categories import Categories
from Shop import Shop, Movie, Client, Filter
from Verifier import Verifier
from EcuadorianIdCard import EcuadorianIdCard
from CreditCard import CreditCard

class ShopMenu:
    """Manage the options of shop through menu

    Attributes:
        shop: Database of movie shop

    Methods:
        __select_category
        __create_movie
        __pay_movie
        __register_movie
        __add_movie
        __print_movie_list
        __sell_movie
        __search_movie
        __rent_movie
        __return_rent_movie
        help_shop
        print
    """

    def __init__(self, shop: Shop) -> None:
        """Default constructor

        Args:
            shop (Shop): _description_
        """
        self.__shop = shop

    def __select_category(self) -> str:
        """Select category of Cagories class

        Returns:
            str: _description_ Category type
        """
        # Verify if category option select exist
        is_valid_category = False
        # Save category option select
        category = int()
        # Enter category until has been valid
        while not is_valid_category:
            # Clear console screen
            console.system("cls")
            # Show categories on console
            Categories.print()
            # Input category option
            category = Input.integer("Categoria: ", 1, 2, signed=False)
            # Verify if is a valid option
            is_valid_category = Categories.is_valid(category)

            # Invalid option
            if not is_valid_category:
                # Print error information
                print("Categoria no valida")
                # Pause execution of program until press any key
                console.system("pause > nul")

        return Categories.select(category)
    
    def __create_movie(self) -> Movie:
        """Enter information about movie and returns a movie object

        Returns:
            Movie: _description_ Movie object with all information entered
        """
        # Print title
        print("[INFORMACION DE LA PELICULA]")
        # Create movie object
        movie = Movie()
        # Enter name of movie
        movie.name = Input.alphanumeric("Titulo: ", 3, 30).lower()
        # Enter director of movie
        movie.director = Input.alphabetic("Director: ", 3, 20).lower()
        # Enter amount of movie
        movie.amount = Input.integer("Cantidad: ", 1, 3, signed=False)
        # Enter category of movie
        movie.category = self.__select_category()
        # Enter synopsis of movie
        movie.synopsis = Input.alphanumeric("Sinopsis: ", 10, 100)
        # Enter purchase price of movie
        movie.purchase_price = Input.floating("Precio venta: ", 1, 6, signed=False)
        # Enter rental price of movie
        movie.rental_price = movie.purchase_price / 2
        
        return movie
    
    def __pay_movie(self) -> Client|None:
        """Process a buy of movie. Enter client information

        Returns:
            Client|None: _description_ Client: successful transaction, None: fail transaction
        """
        # Print title
        print("[INFORMACION DEL CLIENTE]")
        # Create client object
        client = Client()
        # Enter first name of client
        client.first_name = Input.alphabetic("Nombre: ", 3, 10, space=False).lower()
        # Enter last name of client
        client.last_name = Input.alphabetic("Apellido: ", 3, 10, space=False).lower()
        # Enter identify card of client
        client.id_card = Input.numeric("Cedula: ", 10, 10)

        # Verify if is a valid ecuadorian id card
        while not Verifier.card(EcuadorianIdCard(client.id_card)):
            # Print error information
            print("Cedula no valida")
            # Ask if want retry enter id card
            if Input.string("Desea reintentar (s\\n): ", lambda char: char == 's' or char == 'n', 1, 1) == 's':
                # Enter identify card of client
                client.id_card = Input.numeric("Cedula: ", 10, 10)
            # No want retry enter id card
            else:
                # Fail transaction
                return None

        
        # Verify if is a valid credit card
        while not Verifier.card(CreditCard(Input.numeric("Tarjeta de credito: ", 16, 16))):
            # Print error information
            print("Tarjeta de credito no valida")
            # Ask if want retry enter credir card
            if Input.string("Desea reintentar (s\\n): ", lambda char: char == 's' or char == 'n', 1, 1) == 'n':
                # Fail transaction
                return None

        # Succesful transaction
        return client

    def __register_movie(self) -> None:
        """Append a new movie to shop
        """

        movie = self.__create_movie()

        if self.__shop.exist(movie):
            return print("Pelicula ya existe en la tienda")
        
        self.__shop.register_movie(movie)
        print("Pelicula registrada correctamente")

    def __add_movie(self) -> None:
        """Adds stock to existent movie
        """
        # Create movie object
        movie = Movie()
        # Enter id of movie
        movie.id = Input.integer("ID de la pelicula: ", 1, 3, signed=False)
        
        # Verify if movie exist in shop
        if not self.__shop.exist(movie):
            # Print error information
            print("Pelicula no existe en la tienda")
        # Movie doesn't exist in shop
        else:
            # Enter amount of movie to add
            movie.amount = Input.integer("Cantidad: ", 1, 3, signed=False)
            # Enter amount to shop
            self.__shop.add_movie(movie)
            # Successful operation
            print("Cantidad de peliculas agregada correctamente")

    def __print_movies_list(self) -> None:
        """Print movies list using a filter
        """
        # Get filters list
        filters = Filter.filters()
        # Invalid option
        option = len(filters) + 1

        # Enter filter until has been a valid option
        while option > len(filters):
            # Clear screen
            console.system("cls")
            # Option count
            i = 1
            # Print each filter of filters list
            for filter in filters:
                # Print name filter
                print(f"{i}.- {filter}")
                # Increment option count
                i += 1
            
            # Enter filter option
            option = Input.integer("Filtro: ", 1, 1, signed=False)

        # Select filter type
        filter = filters[option - 1]
        
        # Matching value for filter
        matching = str()

        # Enter matching value which filter type
        match filter:
            case "Categoria":
                matching = self.__select_category()
            
            case "Ninguno":
                pass
                
            case _:
                matching = Input.alphanumeric(f"{filters[option - 1]}: ", 3, 30).lower()

        # Clear screen
        console.system("cls")
        # Print movies with filter
        self.__shop.print_movies_list(Filter(filter, matching))

    def __search_movie(self) -> None:
        """Search an specific movie in shop
        """
        # Enter id of movie
        position = Input.integer("ID de pelicula: ", 1, 3, signed=False)
        # Search movie in shop
        movie = self.__shop.search(position)
        # Print movie if exist
        print(movie if movie != None else "Pelicula no existe")

    def __sell_movie(self) -> None:
        """Process a sell of movie
        """
        # Create movie object
        movie = Movie()
        # Enter id movie
        movie.id = Input.integer("ID de pelicula: ", 1, 3, signed=False)

        # Verify if movie exist in shop and had stock
        if not self.__shop.exist(movie) or not self.__shop.has_stock(movie):
            # Print error information
            return print("ID no existente o no hay stock de la pelicula especificada")

        # Verify is pay for movie was successful
        is_successful_pay = not self.__pay_movie() == None

        # Fail pay of movie
        if not is_successful_pay:
            # Error information
            return print("Transaccion no exitosa")

        # Register sell of movie in shop        
        if self.__shop.sell_movie(movie):
            # Print successful transaction information
            print(f"Transaccion exitosa, se le cobra {self.__shop.movies[movie.id - 1].purchase_price}")

    def __rent_movie(self) -> None:
        """Register a rent of movie in shop
        """
        # Create movie object
        movie = Movie()
        # Enter movie id
        movie.id = Input.integer("ID de pelicula: ", 1, 3, signed=False)

        # If movie doesn't exist in shop
        if not self.__shop.exist(movie):
            # Error information
            return print("ID no existente o no hay stock de la pelicula especificada")
        
        # Register pay of client
        client = self.__pay_movie()

        # Fail pay
        if client == None:
            # Error information
            return print("Transaccion fallida")
        
        # Successful pay
        if self.__shop.rent_movie(movie, client):
            # Successful pay information
            print(f"Transaccion exitosa, se le cobra {self.__shop.movies[movie.id - 1].rental_price}")
        else:
            # Fail pay information
            print("Transaccion fallida: ya ha rentado la pelicula especificada")

    def __return_rent_movie(self) -> None:
        """Register a return of rental movie to shop
        """
        # Create movie object
        movie = Movie()
        # Enter id of movie
        movie.id = Input.integer("Id de pelicula: ", 1, 3, signed=False)

        # Movie doesn't exist in shop
        if not self.__shop.exist(movie):
            # Error information
            return print("Pelicula no existe en la tienda")

        # Create client object
        client = Client()
        # Enter id card of client
        client.id_card = Input.numeric("Cedula: ", 10, 10)

        # Verify if id card is valid
        while not Verifier.card(EcuadorianIdCard(client.id_card)):
            # Error information
            print("Cedula no valida")
            # Retry enter id card
            if Input.string("Desea reintentar (s\\n): ", lambda char: char == 's' or char == 'n', 1, 1) == 's':
                # Enter id card of client
                client.id_card = Input.numeric("Cedula: ", 10, 10)
            else:
                # Transaccion fail
                return None
        
        # Successful return movie to shop
        if self.__shop.return_movie(movie, client):
            # Successful return information
            print("Transaccion exitosa")
        # Fail return movie to shop
        else:
            # Fail return information
            print("Transaccion fallida: [La pelicula no ha sido rentada por el cliente o el cliente no se encuentra en la base de datos]")

    def help_shop(self) -> None:
        """Show information about each option in shop menu
        """
        # Help information
        print(
            """
            [Registrar pelicula]: Agrega una nueva pelicula a la tienda. Si la pelicula ya existe la función no continuará, en ese caso use la funcion de agregar pelicula.

            [Agregar pelicula]: Agrega stock de una pelicula existente en la tienda.

            [Lista de peliculas]: Despliega el listado de peliculas existente y registradas en la tienda. Puede utilizar distintos filtros para busquedas mas concretas.
            Filtros:
            - Ninguno: Desplegará el listado completo
            - Titulo: Despliega todas las películas que comienzen por el titulo especificado
            - Director: Despliega todas las peliculas que su nombre de director comienzen por el especificado
            - Categoria: Despliega todas las peliculas coincidentes con la categoria seleccionada

            [Buscar pelicula]: Busca una pelicula en especifico por el Id. El Id lo puede encontrar al desplegar el listado de peliculas en la opcion [Lista de peliculas].

            [Vender pelicula]: Opera la transaccion de la venta de una pelicula. Se requiere cedula y la tarjeta de credito del comprador para validar la compra.

            [Rentar pelicula]: Registra la alquilacion de una pelicula. El cliente que la alquila requiere de cedula y tarjeta de credito para poder alquilarla. Su nombre, apellido y cedula quedaran registrados en el sistema para validar nuevas alquilaciones o devoluciones a la tienda.

            [Devolver pelicula]: Registra la devolucion de una pelicula rentada. El cliente que la devuelva requiere el mismo numero de cedula con el que fue registrado su alquilacion.
            """
        )

    def print(self) -> None:
        """Print menu shop
        """

        # Infinite execution
        while True:
            # Clear screen
            console.system("cls")
            
            # Print options of menu
            print(
                "[ TIENDA DE PELICULAS ]\n",
                "1.- Registrar pelicula\n",
                "2.- Agregar pelicula\n",
                "3.- Lista de peliculas\n",
                "4.- Buscar pelicula\n",
                "5.- Vender pelicula\n",
                "6.- Rentar pelicula\n",
                "7.- Devolver pelicula\n",
                "8.- Ayuda\n"
                "9.- Salir\n",
                sep=''
            )

            # Enter option of menu
            option = Input.numeric("Opcion: ", 1, 1)
            
            # Clear screen
            console.system("cls")

            # Matching option
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
                    self.help_shop()

                case '9':
                    break

                case _:
                    continue
            
            # Pause execution of program
            console.system('pause > nul')