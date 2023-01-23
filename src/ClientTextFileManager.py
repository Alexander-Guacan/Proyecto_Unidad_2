# Import client class
from Client import Client

class ClientTextFileManager:
    """Manager of text file that saves client information

    Attributes:
        __filename: path and name of clients txt file
        
    Methods:
        save
        read
        update
    """

    __filename = "../database/Clients.txt"

    @classmethod
    def save(cls, client: Client) -> None:
        """Append client information to txt file

        Args:
            client (Client): Client object
        """
        # Open file in append mode
        file = open(cls.__filename, "a")
        # Saving client information
        file.write(client.saving_format())
        # Close txt file
        file.close()

    @classmethod
    def read(cls) -> list[Client]:
        """Returns of list of all clients saving in txt file

        Returns:
            list[Client]: _description_ Clients with information in txt file
        """
        clients = list[Client]()

        try:
            # Open file on read mode
            file = open(cls.__filename, "r")
        except FileNotFoundError:
            # Returns empty clients list
            return clients

        # Read line by line of txt file
        for line in file.readlines():
            # Client object where will saving information
            client = Client()
            # Append client to clients list
            clients.append(client.reading_format(line))

        # Close txt file
        file.close()
        
        return clients
    
    @classmethod
    def update(cls, clients: list[Client]) -> None:
        """Overwrite all information in txt file with updates in list client of shop

        Args:
            clients (list[Client]): _description_ Clients list of shop
        """
        # Open file in write function
        file = open(cls.__filename, "w")

        # Travels clients list
        for client in clients:
            # Write client attributes in txt file
            file.write(client.saving_format())

        # Close txt file
        file.close()