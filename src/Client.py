class Client:
    def __init__(self) -> None:
        self.id_card = str()
        self.first_name = str()
        self.last_name = str()
        self.movies = list[int]()

    def __eq__(self, client: "Client") -> bool:
        return isinstance(client, Client) and self.id_card == client.id_card
    
    def __movies_to_string(self) -> str:
        movies_to_string = str()
        for movie in self.movies:
            movies_to_string += str(movie) + '|'

        return movies_to_string
    
    def rent_movie(self, id: int) -> bool:
        if id in self.movies:
            return False
        
        self.movies.append(id)
        return True
    
    def pay_for_rented_movie(self, id: int) -> bool:
        if id not in self.movies:
            return False
        
        self.movies.remove(id)
        return True
    
    def saving_format(self) -> str:
        return self.id_card + '|' + self.first_name + '|' + self.last_name + ';' + self.__movies_to_string() + '\n'
    
    def reading_format(self, line: str) -> "Client":
        attributes, movies = line.split(";")
        self.id_card, self.first_name, self.last_name = attributes.split('|')

        for id in movies.split('|'):
            if id.isnumeric():
                self.movies.append(int(id.rstrip()))

        return self