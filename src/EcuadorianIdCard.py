from Card import Card

class EcuadorianIdCard(Card):
    
    def __init__(self, id: str) -> None:
        super().__init__(id)

    def verifier_algorithm(self) -> bool:
        if len(self.id) != 10:
            return False
        
        sum_odd_position = 0

        for i in range(0, len(self.id) - 1, 2):
            sum_odd_position += int(self.id[i]) * 2 if int(self.id[i]) * 2 < 10 else (int(self.id[i]) * 2) - 9

        sum_even_position = 0

        for i in range(1, len(self.id) - 2, 2):
            sum_even_position += int(self.id[i])

        verifier_digit = 0 if (sum_even_position + sum_odd_position) % 10 == 0 else 10 - (sum_even_position + sum_odd_position) % 10

        return verifier_digit == int(self.id[-1])