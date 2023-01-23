class Movie:

    def __init__(self) -> None:
        self.id = int()
        self.name = str()
        self.director = str()
        self.synopsis = str()
        self.amount = int(1)
        self.category = str()
        self.purchase_price = float()
        self.rental_price = float()

    def saving_format(self) -> str:
        return str(self.id) + '|' + self.name + '|' + self.director + '|' + self.category + '|' + str(self.amount) + '|' + str(self.purchase_price) + '|' + str(self.rental_price) + '|' + self.synopsis + '\n'
    
    def reading_format(self, line: str) -> "Movie":
        id, self.name, self.director, self.category, amount, purchase_price, rental_price, self.synopsis = line.split('|')
        self.id = int(id)
        self.amount = int(amount)
        self.purchase_price = float(purchase_price)
        self.rental_price = float(rental_price)
        self.synopsis = self.synopsis.rstrip()
        return self

    def __eq__(self, movie: "Movie") -> bool:
        return isinstance(movie, Movie) and self.id == movie.id
    
    def __repr__(self) -> str:
        attributes_width = 8
        return '[ ' + self.name.upper() + ' ]'\
            + '\n' + '-'*attributes_width + ">ID: " + str(self.id)\
            + '\n' + '-'*attributes_width + '>Director: ' + self.director\
            + '\n' + '-'*attributes_width + '>Sinopsis: ' + self.synopsis\
            + '\n' + '-'*attributes_width + '>Cantidad: ' + str(self.amount)\
            + '\n' + '-'*attributes_width + '>Precio de venta: ' + str(self.purchase_price)\
            + '\n' + '-'*attributes_width + '>Precio de renta: ' + str(self.rental_price) + '\n'