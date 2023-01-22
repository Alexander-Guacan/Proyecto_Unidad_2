from Client import Client

class ClientTextFileManager:
    __filename = "../database/Clients.txt"

    @classmethod
    def save(cls, client: Client) -> None:
        file = open(cls.__filename, "a")
        file.write(client.saving_format())
        file.close()

    @classmethod
    def read(cls) -> list[Client]:
        clients = list[Client]()

        try:
            file = open(cls.__filename, "r")
        except FileNotFoundError as exception:
            return clients

        for line in file.readlines():
            client = Client()
            clients.append(client.reading_format(line))

        file.close()
        
        return clients
    
    @classmethod
    def update(cls, clients: list[Client]) -> None:
        file = open(cls.__filename, "w")

        for client in clients:
            file.write(client.saving_format())

        file.close()