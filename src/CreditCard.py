from Card import Card

class CreditCard(Card):

    def __init__(self, id: str) -> None:
        super().__init__(id)

    def verifier_algorithm(self) -> bool:
        if len(self.id) != 16:
            return False
        
        sum_odd_position = 0
        for i in range(0, len(self.id), 2):
            sum_odd_position += int(self.id[i]) * 2 if int(self.id[i]) < 5 else int(self.id[i]) - (9 - int(self.id[i]))

        sum_even_position = 0
        for i in range(1, len(self.id), 2):
            sum_even_position += int(self.id[i])

        return (sum_even_position + sum_odd_position) % 10 == 0