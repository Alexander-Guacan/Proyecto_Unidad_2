# Import module to create abstract basic class
from abc import ABC, abstractmethod

class Card(ABC):
    """Abstract basic class that represent any card with ids

    Methods:
        verifier_algorithm

    Attributes:
        id: str
    """

    def __init__(self, id: str) -> None:
        """Default constructor

        Args:
            id (str): _description_ Code to identify the card type
        """
        # Initialize attributes
        self.id = id

    @abstractmethod
    def verifier_algorithm(self) -> bool:
        """Returns true if id is valid or false otherwise

        Returns:
            bool: _description_ True: id valid, False: id not valid
        """