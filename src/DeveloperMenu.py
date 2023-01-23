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
        self.__shop = shop

    def __generate_id(self) -> int:
        file = open("../database/movies.txt")
        id = int(file.readlines()[-1].split('|')[0])
        file.close()
        return id + 1
    
    def __movies_amount(self) -> int:
        file = open("../database/movies.txt")
        id = len(file.readlines())
        file.close()
        return id

    def __select_filter(self) -> str:
        filters = Filter.filters()

        return filters[random.randint(0, len(filters) - 1)]

    def __select_category(self) -> str:
        return Categories.select(random.randint(1, 10))
    
    def __create_movie(self) -> Movie:
        movie = Movie()
        movie.id = self.__generate_id()
        movie.name = big_o.datagen.strings(20, big_o.datagen.string.ascii_lowercase)
        movie.director = big_o.datagen.strings(20, big_o.datagen.string.ascii_lowercase)
        movie.amount = random.randint(1, 999)
        movie.category = self.__select_category()
        movie.synopsis = big_o.datagen.strings(20, big_o.datagen.string.ascii_lowercase)
        movie.purchase_price = round(float(random.randint(1, 5) + random.random()), 2)
        movie.rental_price = round(movie.purchase_price / 2, 2)
        
        return movie
    
    def __create_client(self) -> Client:
        client = Client()
        client.id_card = big_o.datagen.strings(10, big_o.datagen.string.digits)
        client.first_name = big_o.datagen.strings(20, big_o.datagen.string.ascii_lowercase)
        client.last_name = big_o.datagen.strings(20, big_o.datagen.string.ascii_lowercase)

        return client
    
    def __select_movie(self) -> Movie:
        movie = Movie()
        movie.id = random.randint(1, self.__movies_amount())

        return movie

    @profile(precision=1)
    def list_filter(self) -> None:
        filter = self.__select_filter()
        matching = str()
        filter_object = lambda _: Filter(filter, matching)
        best, others = big_o.big_o(self.__shop.print_movies_list, filter_object)
        print(f"[FUNCION FILTRO DE LISTA] Time complexity: {best}")

    @profile
    def save_movie_information(self) -> None:
        movie_sample = lambda _: self.__create_movie()
        best, others = big_o.big_o(MovieTextFileManager.save, movie_sample)
        print(f"[FUNCION GUARDAR PELICULA EN TXT] Time complexity: {best}")

    @profile
    def create_movie(self) -> None:
        start_time = timeit.timeit()
        self.__create_movie()
        end_time = timeit.timeit()
        print(f"[FUNCION CREAR PELICULA] Time complexity: {end_time - start_time:e}")

    @profile
    def add_movie(self) -> None:
        movie = Movie()
        movie.id = random.randint(1, self.__movies_amount())
        movie.amount = random.randint(1, 999)
        movie_sample = lambda _: movie
        best, others = big_o.big_o(self.__shop.add_movie, movie_sample)
        print(f"[FUNCION ADQUISICION DE PELICULA A LA TIENDA] Time complexity: {best}")

    @profile
    def sell_movie(self) -> None:
        movie = Movie()
        movie.id = random.randint(1, self.__movies_amount())
        movie_sample = lambda _: movie
        best, others = big_o.big_o(self.__shop.sell_movie, movie_sample)
        print(f"[FUNCION VENDER PELICULA] Time complexity: {best}")

    @profile
    def print_movie_information(self) -> None:
        movie_sample = lambda _: random.randint(1, self.__movies_amount())
        best, others = big_o.big_o(self.__shop.search, movie_sample)
        print(f"[FUNCION BUSQUEDA DE INFORMACION DE PELICULA] Time complexity: {best}")

    @profile
    def rent_movie(self) -> None:
        start_time = timeit.timeit()
        self.__shop.rent_movie(self.__select_movie(), self.__create_client())
        end_time = timeit.timeit()
        print(f"[FUNCION REGISTRAR LA ALQUILACION DE PELICULA] Time complexity: {end_time - start_time:e}")

    @profile
    def verify_credit_card(self) -> None:
        credit_card_generator = lambda _: CreditCard(big_o.datagen.strings(16, big_o.datagen.string.digits))
        best, others = big_o.big_o(Verifier.card, credit_card_generator)
        print(f"[FUNCION VERIFICADORA DE TARJETA DE CREDITO] Time complexity: {best}")

    def print(self) -> None:
        while True:
            console.system("cls")

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

            option = Input.string("Opcion: ", lambda char: char >= '1' and char <= '9', 1, 1)

            console.system("cls")

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

            console.system("pause > nul")