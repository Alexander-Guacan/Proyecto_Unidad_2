from MovieTextFileManager import MovieTextFileManager, Movie
from ClientTextFileManager import ClientTextFileManager, Client
from Filter import Filter

class Shop:

    def __init__(self) -> None:
        self.movies = MovieTextFileManager.read()
        self.clients = ClientTextFileManager.read()

    def exist(self, movie: Movie) -> bool:
        return movie in self.movies or movie.id >= 1 and movie.id <= len(self.movies)
    
    def has_stock(self, movie: Movie) -> bool:
        return self.movies[movie.id - 1].amount >= 1

    def register_movie(self, movie: Movie) -> bool:
        if self.exist(movie):
            return False
        
        self.movies.append(movie)
        movie.id = len(self.movies)

        MovieTextFileManager.save(movie)

        return True

    def add_movie(self, movie: Movie) -> bool:
        if not self.exist(movie):
            return False
        
        self.movies[movie.id - 1].amount += movie.amount

        MovieTextFileManager.update(self.movies)

        return True

    def sell_movie(self, movie: Movie) -> bool:
        if not self.exist(movie) or not self.has_stock(movie):
            return False
        
        self.movies[movie.id - 1].amount -= 1

        MovieTextFileManager.update(self.movies)

        return True

    def rent_movie(self, movie: Movie, client: Client) -> bool:
        if not self.has_stock(movie):
            return False
        
        is_new_movie = True

        if client in self.clients:
            is_new_movie = self.clients[self.clients.index(client)].rent_movie(movie.id)
            if not is_new_movie:
                return False
            else:
                ClientTextFileManager.update(self.clients)
        else:
            client.rent_movie(movie.id)
            self.clients.append(client)
            ClientTextFileManager.save(client)

        self.sell_movie(movie)
        MovieTextFileManager.update(self.movies)

        return True
    
    def return_movie(self, movie: Movie, client: Client) -> bool:
        if not self.exist(movie) or client not in self.clients:
            return False
        
        is_successful_pay = self.clients[self.clients.index(client)].pay_for_rented_movie(movie.id)

        if not is_successful_pay:
            return False
        
        self.movies[movie.id - 1].amount += 1

        MovieTextFileManager.update(self.movies)
        ClientTextFileManager.update(self.clients)

        return True

    def search(self, id: int) -> None|Movie:
        if id < 1 or id > len(self.movies):
            return None
        
        return self.movies[id - 1]

    def print_movies_list(self, filter: Filter) -> None:

        id_width, name_width, director_width, category_width, amount_width, purchase_price_width, rental_price_width, gap, columns, border =  3, 30, 20, 20, 8, 15, 18, ' '*3, 6, 2
        width_table = id_width + name_width + director_width + category_width + amount_width + purchase_price_width + rental_price_width + border + len(gap) * columns
        
        title = '|' + '-'*width_table + '|\n'\
            + f"|{'STOCK':^{width_table}}|\n"\
            + '|' + '-'*width_table + '|\n'\
            + f"| {'Id.':<{id_width}}{gap}{'PELICULA':<{name_width}}{gap}{'DIRECTOR':<{director_width}}{gap}{'CATEGORIA':<{category_width}}{gap}{'CANTIDAD':<{amount_width}}{gap}{'PRECIO DE VENTA':<{purchase_price_width}}{gap}{'PRECIO DE ALQUILER':<{rental_price_width}} |\n"\
            + '|' + '-'*width_table + '|'
        
        print(title)
        for movie in self.movies:
            if filter.has_select() and not str(movie.__getattribute__(filter.type)).startswith(filter.matching):
                continue

            print(f"| {movie.id:^{id_width}d}{gap}{movie.name:<{name_width}s}{gap}{movie.director:<{director_width}}{gap}{movie.category:<{category_width}s}{gap}{movie.amount:^{amount_width}d}{gap}{movie.purchase_price:^{purchase_price_width}.2f}{gap}{movie.rental_price:^{rental_price_width}.2f} |\n"\
                + '|' + '-'*width_table + '|')