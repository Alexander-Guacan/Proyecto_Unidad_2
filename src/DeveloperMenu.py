from Shop import Shop, MovieTextFileManager, Movie, Client, Filter
from Input import Input
import os as console
from Categories import Categories
import big_o
from memory_profiler import profile
import random
import timeit
from Verifier import Verifier
from CreditCard import CreditCard

class DeveloperMenu:
    def __init__(self, shop: Shop) -> None:
        """Default constructor

        Args:
            shop (Shop): _description_
        """
        self.__shop = shop

    def __generate_id(self) -> int:
        """Returns last id save in txt file + 1

        Returns:
            int: _description_ New id movie
        """
        # Open movies file in read mode
        file = open("../database/movies.txt", "r")
        # Last id generated
        id = int(file.readlines()[-1].split('|')[0])
        # Close txt file
        file.close()

        # New id
        return id + 1
    
    def __movies_amount(self) -> int:
        """Returns of movies amount in txt file

        Returns:
            int: _description_ Movies amount in txt file
        """
        # Open file in read mode
        file = open("../database/movies.txt", "r")
        # Amount of lines in txt file
        amount = len(file.readlines())
        # Close txt file
        file.close()

        return amount

    def __select_filter(self) -> str:
        """Select random filter

        Returns:
            str: _description_ Random filter name
        """
        filters = Filter.filters()

        return filters[random.randint(0, len(filters) - 1)]

    def __select_category(self) -> str:
        """Select random category

        Returns:
            str: _description_ Random category name
        """
        return Categories.select(random.randint(1, 10))
    
    def __create_movie(self) -> Movie:
        """Create random movie

        Returns:
            Movie: _description_ Random movie
        """
        # Movie object
        movie = Movie()
        # New id
        movie.id = self.__generate_id()
        # Random name
        movie.name = big_o.datagen.strings(20, big_o.datagen.string.ascii_lowercase)
        # Random director
        movie.director = big_o.datagen.strings(20, big_o.datagen.string.ascii_lowercase)
        # Random amount
        movie.amount = random.randint(1, 999)
        # Random category
        movie.category = self.__select_category()
        # Random synopsis
        movie.synopsis = big_o.datagen.strings(20, big_o.datagen.string.ascii_lowercase)
        # Random purchase price
        movie.purchase_price = round(float(random.randint(1, 5) + random.random()), 2)
        # Random rental price
        movie.rental_price = round(movie.purchase_price / 2, 2)
        
        return movie
    
    def __create_client(self) -> Client:
        """Create random client

        Returns:
            Client: _description_ random client
        """
        # Client object
        client = Client()
        # Random id card
        client.id_card = big_o.datagen.strings(10, big_o.datagen.string.digits)
        # Random first name
        client.first_name = big_o.datagen.strings(20, big_o.datagen.string.ascii_lowercase)
        # Random last name
        client.last_name = big_o.datagen.strings(20, big_o.datagen.string.ascii_lowercase)

        return client
    
    def __select_movie(self) -> Movie:
        """Returns random movie with random id

        Returns:
            Movie: _description_ Random movie
        """
        movie = Movie()
        # Random id inside of range of movies list
        movie.id = random.randint(1, self.__movies_amount())

        return movie

    @profile
    def list_filter(self) -> None:
        """Measure time and space complexity of list filter
        """
        # Random filter
        filter = self.__select_filter()
        # Empty string
        matching = str()
        # Random filter object contained in lambda function
        filter_object = lambda _: Filter(filter, matching)
        # Measure time complexity
        best, others = big_o.big_o(self.__shop.print_movies_list, filter_object)
        # Results of time complexity
        print(f"[FUNCION FILTRO DE LISTA] Time complexity: {best}")

    @profile
    def save_movie_information(self) -> None:
        """Measure time and space complexity of save movie in txt file function
        """
        # Random filter object contained in lambda function
        movie_sample = lambda _: self.__create_movie()
        # Measure time complexity
        best, others = big_o.big_o(MovieTextFileManager.save, movie_sample)
        # Results of time complexity
        print(f"[FUNCION GUARDAR PELICULA EN TXT] Time complexity: {best}")

    @profile
    def create_movie(self) -> None:
        """Measure time and space complexity of create movie function
        """
        # Start time before execute create movie function
        start_time = timeit.timeit()
        # Execute create movie function
        self.__create_movie()
        # End time after execute create movie function
        end_time = timeit.timeit()
        # Results of time complexity
        print(f"[FUNCION CREAR PELICULA] Time complexity: {end_time - start_time:e}")

    @profile
    def add_movie(self) -> None:
        """Measure time and space complexity of add movie function
        """
        # Random movie
        movie = Movie()
        # Random id
        movie.id = random.randint(1, self.__movies_amount())
        # Random amount to append
        movie.amount = random.randint(1, 999)
        # Random movie contained in lambda function
        movie_sample = lambda _: movie
        # Measure time complexity
        best, others = big_o.big_o(self.__shop.add_movie, movie_sample)
        # Results of time complexity
        print(f"[FUNCION ADQUISICION DE PELICULA A LA TIENDA] Time complexity: {best}")

    @profile
    def sell_movie(self) -> None:
        """Measure time and space complexity of sell movie function
        """
        # Random movie contained in lambda function
        movie_sample = lambda _: self.__select_movie()
        # Measure time complexity
        best, others = big_o.big_o(self.__shop.sell_movie, movie_sample)
        # Results of time complexity
        print(f"[FUNCION VENDER PELICULA] Time complexity: {best}")

    @profile
    def print_movie_information(self) -> None:
        """Measure time and space complexity of print movie information function
        """
        # Random movie id cotain in lambda function
        movie_id_sample = lambda _: random.randint(1, self.__movies_amount())
        # Measure time complexity
        best, others = big_o.big_o(self.__shop.search, movie_id_sample)
        # Results of time complexity
        print(f"[FUNCION BUSQUEDA DE INFORMACION DE PELICULA] Time complexity: {best}")

    @profile
    def rent_movie(self) -> None:
        """Measure time and space complexity of rent movie function
        """
        # Start time before execute rent movie function
        start_time = timeit.timeit()
        # Execute rent movie function
        self.__shop.rent_movie(self.__select_movie(), self.__create_client())
        # End time after execute rent movie function
        end_time = timeit.timeit()
        # Results of time complexity
        print(f"[FUNCION REGISTRAR LA ALQUILACION DE PELICULA] Time complexity: {end_time - start_time:e}")

    @profile
    def verify_credit_card(self) -> None:
        """Measure time and space complexity of rent movie function
        """
        # Random credit card generator containe din lambda function
        credit_card_generator = lambda _: CreditCard(big_o.datagen.strings(16, big_o.datagen.string.digits))
        # Measure time complexity
        best, others = big_o.big_o(Verifier.card, credit_card_generator)
        # Results of time complexity
        print(f"[FUNCION VERIFICADORA DE TARJETA DE CREDITO] Time complexity: {best}")

    def print(self) -> None:
        """Menu of developer mode
        """
        while True:
            # Clean console screen
            console.system("cls")
            # Options of menu
            print(
                "[ MODO DESARROLLADOR ]\n",
                "1.- Funcion filtrar lista por (director, nombre o genero)\n",
                "2.- Funcion guardar informacion en txt\n",
                "3.- Funcion ingresar informacion de pelicula\n",
                "4.- Funcion comprar pelicula\n",
                "5.- Funcion vender pelicula\n",
                "6.- Funcion buscar pelicula\n",
                "7.- Funcion alquilar pelicula\n",
                "8.- Funcion validar tarjeta de credito\n",
                "9.- Salir\n",
                sep=''
            )
            
            # Enter option
            option = Input.string("Opcion: ", lambda char: char >= '1' and char <= '9', 1, 1)
            
            # Clean console screen
            console.system("cls")
            
            # Select option
            match option:

                case '1':
                    self.list_filter()

                case '2':
                    self.save_movie_information()

                case '3':
                    self.create_movie()

                case '4':
                    self.add_movie()

                case '5':
                    self.sell_movie()

                case '6':
                    self.print_movie_information()

                case '7':
                    self.rent_movie()

                case '8':
                    self.verify_credit_card()

                case '9':
                    break

                case _:
                    continue

            # Pause execution of program
            console.system("pause > nul")