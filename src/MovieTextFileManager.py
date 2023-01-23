from Movie import Movie

class MovieTextFileManager:
    """Manager of text file that saves movie information

    Attributes:
        __filename: path and name of movies txt file
    """

    __filename = "../database/Movies.txt"

    @classmethod
    def save(cls, movie: Movie) -> None:
        """Append movie information to txt file

        Args:
            movie (Movie): Movie object
        """
        # Open file in append mode
        file = open(cls.__filename, "a")
        # Saving movie information
        file.write(movie.saving_format())
        # Close txt file
        file.close()

    @classmethod
    def read(cls) -> list[Movie]:
        """Returns of list of all movies saving in txt file

        Returns:
            list[Movie]: _description_ Clients with information in txt file
        """
        movies = list[Movie]()

        try:
            # Open file on read mode
            file = open(cls.__filename, "r")
        except FileNotFoundError as exception:
            # Returns empty movies list
            return movies

        # Read line by line of txt file
        for line in file.readlines():
            # Movie object where will saving information
            movie = Movie()
            # Append movie to movies list
            movies.append(movie.reading_format(line))

        # Close txt file
        file.close()
        
        return movies
    
    @classmethod
    def update(cls, movies: list[Movie]) -> None:
        """Overwrite all information in txt file with updates in list movie of shop

        Args:
            movies (list[Movie]): _description_ Clients list of shop
        """
        # Open file in write function
        file = open(cls.__filename, "w")

        # Travels movies list
        for movie in movies:
            # Write movie attributes in txt file
            file.write(movie.saving_format())

        # Close txt file
        file.close()