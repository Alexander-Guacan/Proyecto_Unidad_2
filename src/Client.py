class Client:
    def __init__(self) -> None:
        self.id_card = str()
        self.first_name = str()
        self.last_name = str()
        self.movies = list[int]()

    def __eq__(self, client: "Client") -> bool:
        return isinstance(client, Client) and self.id_card == client.id_card
    
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