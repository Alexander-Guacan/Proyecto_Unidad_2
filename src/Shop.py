from MovieTextFileManager import MovieTextFileManager, Movie
from ClientTextFileManager import ClientTextFileManager, Client
from Filter import Filter

class Shop:
    """Shop that manager the stock of movies and clients information

    Attributes:
        movies
        clients

    Methods:
        exist
        has_stock
        register_movie
        add_movie
        sell_movie
        rent_movie
        return_movie
        search
        print
        print_movies_list
    """

    def __init__(self) -> None:
        """Default constructor
        """
        # Load movies of txt file
        self.movies = MovieTextFileManager.read()
        # Load clients of txt file
        self.clients = ClientTextFileManager.read()

    def exist(self, movie: Movie) -> bool:
        """Returns true if movie exist in movies list

        Args:
            movie (Movie): _description_ Movie to verify if exist

        Returns:
            bool: _description_ True: exist, False: doesn't exist
        """
        return movie in self.movies or movie.id >= 1 and movie.id <= len(self.movies)
    
    def has_stock(self, movie: Movie) -> bool:
        """Returns true if amount of movie is greather or equals than 1

        Args:
            movie (Movie): _description_ Movie to find in movies list

        Returns:
            bool: _description_ True: amount is greather or equals than 1, False: otherwise
        """
        return movie.id >= 1 and self.movies[movie.id - 1].amount >= 1

    def register_movie(self, movie: Movie) -> bool:
        """Append movie to movies list and txt file

        Args:
            movie (Movie): _description_ Movie to save

        Returns:
            bool: _description_ True: successful operation, False: otherwise
        """
        # Can't register an existent movie
        if self.exist(movie):
            return False
        
        # Append movie to movies list
        self.movies.append(movie)
        # Generate id
        movie.id = len(self.movies)
        
        # save movie in txt file
        MovieTextFileManager.save(movie)

        return True

    def add_movie(self, movie: Movie) -> bool:
        """Increment amount of specific movie in movies list and txt file

        Args:
            movie (Movie): _description_ Movie to increment amount

        Returns:
            bool: _description_ True: successful operation, False: otherwise
        """

        # Can't increment amount if movie doesn't exist in shop
        if not self.exist(movie):
            return False
        
        # Increment amount of specified movie searched by id
        self.movies[movie.id - 1].amount += movie.amount

        # Update txt file
        MovieTextFileManager.update(self.movies)

        return True

    def sell_movie(self, movie: Movie) -> bool:
        """Decrement amount of specific movie in movies list and txt file

        Args:
            movie (Movie): _description_ Movie to decrement amount

        Returns:
            bool: _description_ True: successful operation, False: otherwise
        """

        # Can't sell movie if not exist or not exist stock in shop
        if not self.exist(movie) or not self.has_stock(movie):
            return False
        
        # Decrement amount of specified movie searched by id
        self.movies[movie.id - 1].amount -= 1

        # Update txt file
        MovieTextFileManager.update(self.movies)

        return True

    def rent_movie(self, movie: Movie, client: Client) -> bool:
        """Decrement amount of specific movie in movies list and txt file and register client in system and txt file

        Args:
            movie (Movie): _description_ Movie to decrement amount

        Returns:
            bool: _description_ True: successful operation, False: otherwise
        """
        # Can't rent movie if hasn't stock in shop
        if not self.has_stock(movie):
            return False
        
        # Verify if client hasn't rent movie specified
        is_new_movie = True

        # If client exist in system
        if client in self.clients:
            # Verify if client can rent the movie
            is_new_movie = self.clients[self.clients.index(client)].rent_movie(movie.id)
            # If can't rent movie
            if not is_new_movie:
                return False
            else:
                # Update movies rent list in txt file
                ClientTextFileManager.update(self.clients)
        else:
            # Add movie to movies rent list
            client.rent_movie(movie.id)
            # Add client to system
            self.clients.append(client)
            # Save client in txt file
            ClientTextFileManager.save(client)

        # Decrement stock in shop
        self.sell_movie(movie)
        # Update movies stock
        MovieTextFileManager.update(self.movies)

        return True
    
    def return_movie(self, movie: Movie, client: Client) -> bool:
        """Return rent movie to shop

        Args:
            movie (Movie): _description_ movie rent for client
            client (Client): _description_ client that rent the movie

        Returns:
            bool: _description_ True: successful operation, False: otherwise
        """
        # Can't return movie if doesn't exist in shop or client not has been registered
        if not self.exist(movie) or client not in self.clients:
            return False
        
        # Verify if movie to return exist in list of client
        is_successful_return = self.clients[self.clients.index(client)].return_rented_movie(movie.id)

        # If can't return movie
        if not is_successful_return:
            return False
        
        # Increment stock of specified movie
        self.movies[movie.id - 1].amount += 1

        # Update movies list
        MovieTextFileManager.update(self.movies)
        # Update clients list
        ClientTextFileManager.update(self.clients)

        return True

    def search(self, id: int) -> None|Movie:
        """Searchs a specified movie and return it

        Args:
            id (int): _description_ id of movie

        Returns:
            None|Movie: _description_ None: movie doesn't exist, Movie: movie exist in shop
        """
        if id < 1 or id > len(self.movies):
            return None
        
        return self.movies[id - 1]

    def print_movies_list(self, filter: Filter) -> None:
        """Print movies list with a filter

        Args:
            filter (Filter): _description_ Filter object that search movie by attribute and matching value of attribute
        """
        # Measures of table
        id_width, name_width, director_width, category_width, amount_width, purchase_price_width, rental_price_width, gap, columns, border =  3, 30, 20, 20, 8, 15, 18, ' '*3, 6, 2
        width_table = id_width + name_width + director_width + category_width + amount_width + purchase_price_width + rental_price_width + border + len(gap) * columns
        
        # Format of title table
        title = '|' + '-'*width_table + '|\n'\
            + f"|{'STOCK':^{width_table}}|\n"\
            + '|' + '-'*width_table + '|\n'\
            + f"| {'Id.':<{id_width}}{gap}{'PELICULA':<{name_width}}{gap}{'DIRECTOR':<{director_width}}{gap}{'CATEGORIA':<{category_width}}{gap}{'CANTIDAD':<{amount_width}}{gap}{'PRECIO DE VENTA':<{purchase_price_width}}{gap}{'PRECIO DE ALQUILER':<{rental_price_width}} |\n"\
            + '|' + '-'*width_table + '|'
        
        # Print title of table
        print(title)

        # Travels movies list
        for movie in self.movies:
            # Filter is active and matching value don't match with attribute type value specified
            if filter.has_select() and not str(movie.__getattribute__(filter.type)).startswith(filter.matching):
                # Not print movie
                continue

            # Print attributes of movie formatted
            print(f"| {movie.id:^{id_width}d}{gap}{movie.name:<{name_width}s}{gap}{movie.director:<{director_width}}{gap}{movie.category:<{category_width}s}{gap}{movie.amount:^{amount_width}d}{gap}{movie.purchase_price:^{purchase_price_width}.2f}{gap}{movie.rental_price:^{rental_price_width}.2f} |\n"\
                + '|' + '-'*width_table + '|')