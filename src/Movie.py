class Movie:
    """Movie of shop
    
    Attributes:
        id
        name
        director
        synopsis
        amount
        category
        purchase_price
        rental_price
    """

    def __init__(self) -> None:
        """Default costructor
        """
        # Initialize attributes
        self.id = int()
        self.name = str()
        self.director = str()
        self.synopsis = str()
        self.amount = int(1)
        self.category = str()
        self.purchase_price = float()
        self.rental_price = float()

    def saving_format(self) -> str:
        """Format to save attributes of this class in txt file

        Returns:
            str: _description_ Attributes information separates for '|' character
        """
        return str(self.id) + '|' + self.name + '|' + self.director + '|' + self.category + '|' + str(self.amount) + '|' + str(self.purchase_price) + '|' + str(self.rental_price) + '|' + self.synopsis + '\n'
    
    def reading_format(self, line: str) -> "Movie":
        """Initialize this object from one line of txt file

        Args:
            line (str): _description_ Line of txt file

        Returns:
            Movie: _description_ Object with attributes initialized
        """
        # Split each attribute on line of txt file
        id, self.name, self.director, self.category, amount, purchase_price, rental_price, self.synopsis = line.split('|')
        # Transforms string attributes to numeric values
        self.id = int(id)
        self.amount = int(amount)
        self.purchase_price = float(purchase_price)
        self.rental_price = float(rental_price)
        # Removes '\n' and ' ' characters
        self.synopsis = self.synopsis.rstrip()
        return self

    def __eq__(self, movie: "Movie") -> bool:
        """Override equals operator

        Args:
            movie (Movie): _description_ Other object to compare of the same instance of Movie class

        Returns:
            bool: _description_ True: if both have same name and director
        """
        return isinstance(movie, Movie) and self.name == movie.name and self.director == movie.director
    
    def __repr__(self) -> str:
        """Override print in string format

        Returns:
            str: _description_ Representation in string
        """
        # Amount of guide lines to separate attributes of movie
        attributes_width = 8
        return '[ ' + self.name.upper() + ' ]'\
            + '\n' + '-'*attributes_width + ">ID: " + str(self.id)\
            + '\n' + '-'*attributes_width + '>Director: ' + self.director\
            + '\n' + '-'*attributes_width + '>Sinopsis: ' + self.synopsis\
            + '\n' + '-'*attributes_width + '>Cantidad: ' + str(self.amount)\
            + '\n' + '-'*attributes_width + '>Precio de venta: ' + str(self.purchase_price)\
            + '\n' + '-'*attributes_width + '>Precio de renta: ' + str(self.rental_price) + '\n'