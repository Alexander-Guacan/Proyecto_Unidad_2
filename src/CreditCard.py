from Card import Card

class CreditCard(Card):

    def __init__(self, id: str) -> None:
        """Default constructor

        Args:
            id (str): _description_ Code to identify the card type
        """
        super().__init__(id)

    def verifier_algorithm(self) -> bool:
        """Returns true if id is valid or false otherwise

        Returns:
            bool: _description_ True: id valid, False: id not valid
        """
        # Invalid id if lenght not equals to 16
        if len(self.id) != 16:
            return False
        
        # Sum each value in odd positions of id
        sum_odd_position = 0
        # Travels odd positions of id
        for i in range(0, len(self.id), 2):
            # Multiply each position by 2 and if it is greater than 9 add the two digits that make it up
            sum_odd_position += int(self.id[i]) * 2 if int(self.id[i]) < 5 else int(self.id[i]) - (9 - int(self.id[i]))

        # Sum each value in even positions of id
        sum_even_position = 0
        # Travels even positions of id
        for i in range(1, len(self.id), 2):
            # Sum each value
            sum_even_position += int(self.id[i])
        
        # Id valid if module of sum_even_position plus sum_odd_position equals to zero
        return (sum_even_position + sum_odd_position) % 10 == 0