class Client:
    """Save the clients to rent movies
        
    Attributes:
        id_card
        first_name
        last_name
        movies

    Method:
        __movies_to_string
        rent_movie
        return_rented_movie
        saving_format
        reading_format
    """

    def __init__(self) -> None:
        """Default constructor
        """
        # Initialize attributes
        self.id_card = str() # Identifier card
        self.first_name = str()
        self.last_name = str()
        self.movies = list[int]() # List of id of movies in shop

    def __eq__(self, client: "Client") -> bool:
        """Override equals operator

        Args:
            client (Client): _description_ Other object to compare of the same instance of Client class

        Returns:
            bool: _description_ True: if both have same id card
        """
        return isinstance(client, Client) and self.id_card == client.id_card
    
    def __movies_to_string(self) -> str:
        """Returns list of identifier movies like string for saving in txt file

        Returns:
            str: _description_ List of identifier movies
        """
        # All id of movies separates for '|' character
        movies_to_string = str()
        # Travels movies list
        for movie in self.movies:
            # Saving format
            movies_to_string += str(movie) + '|'

        return movies_to_string
    
    def rent_movie(self, id: int) -> bool:
        """Append new rent movie only if movie doesn't have been rented previously

        Args:
            id (int): _description_ Id of movie

        Returns:
            bool: _description_ True: new rent movie, False: yet rented movie
        """

        # If yet rented movie
        if id in self.movies:
            return False
        
        # Append new rented movie
        self.movies.append(id)
        return True
    
    def return_rented_movie(self, id: int) -> bool:
        """Remove id of rented movie

        Args:
            id (int): _description_ Id of movie

        Returns:
            bool: _description_ True: id removed, False: id doens't exist in movies list
        """

        # If id not exist in movies list
        if id not in self.movies:
            return False
        
        # Remove id of movies list
        self.movies.remove(id)
        return True
    
    def saving_format(self) -> str:
        """Format to save attributes of this class in txt file

        Returns:
            str: _description_ Attributes information separates for '|' character
        """
        return self.id_card + '|' + self.first_name + '|' + self.last_name + ';' + self.__movies_to_string() + '\n'
    
    def reading_format(self, line: str) -> "Client":
        """Initialize this object from one line of txt file

        Args:
            line (str): _description_ Line of txt file

        Returns:
            Client: _description_ Object with attributes initialized
        """

        # Separates single attributes of list of id movies
        attributes, movies = line.split(";")
        # Assign id card, first name and last name
        self.id_card, self.first_name, self.last_name = attributes.split('|')

        # Generates movies list
        for id in movies.split('|'):
            # Only append id if is numeric
            if id.isnumeric():
                # Deletes '\n' or ' ' characters and append id to movies list
                self.movies.append(int(id.rstrip()))

        return self