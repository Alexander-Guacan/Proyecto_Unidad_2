from Movie import Movie

class MovieTextFileManager:
    __filename = "../database/Movies.txt"

    @classmethod
    def save(cls, movie: Movie) -> None:
        file = open(cls.__filename, "a")
        file.write(movie.saving_format())
        file.close()

    @classmethod
    def read(cls) -> list[Movie]:
        movies = list[Movie]()
        file = open(cls.__filename, "r")

        for line in file.readlines():
            movie = Movie()
            movies.append(movie.reading_format(line))

        file.close()
        
        return movies
    
    @classmethod
    def update(cls, movies: list[Movie]) -> None:
        file = open(cls.__filename, "w")

        for movie in movies:
            file.write(movie.saving_format())

        file.close()