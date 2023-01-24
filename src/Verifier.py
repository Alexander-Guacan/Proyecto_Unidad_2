from Card import Card

class Verifier:
    """Class that use verifier_algorithm of Card classes

    Methods:
        card
    """
    
    @classmethod
    def card(cls, type_card: Card) -> bool:
        """Returns true if is a valid card or false in otherwise

        Args:
            type_card (Card): _description_ Any child class of Card abstract class

        Returns:
            bool: _description_ True: valid card, False: invalid card
        """
        return type_card.verifier_algorithm()