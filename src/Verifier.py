from Card import Card

class Verifier:
    
    @classmethod
    def card(cls, type_card: Card) -> bool:
        return type_card.verifier_algorithm()