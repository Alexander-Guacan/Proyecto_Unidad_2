from abc import ABC, abstractmethod

class Card(ABC):

    def __init__(self, id: str) -> None:
        self.id = id

    @abstractmethod
    def verifier_algorithm(self) -> bool:
        pass