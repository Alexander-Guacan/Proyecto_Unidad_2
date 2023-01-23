from Card import Card

class EcuadorianIdCard(Card):
    """Class that cotain id of ecuadorian id card and can verify if is valid

    Attributes:
        id

    Methods:
        verifier_algorithm
    """
    
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
        # Id invalid if lenght isn't equals to 10
        if len(self.id) != 10:
            return False
        
        # Sum of each value in odd positions
        sum_odd_position = 0

        # Travels id in odd positions except the last positions
        for i in range(0, len(self.id) - 1, 2):
            # Add each value multiplied by 2 and subtract 9 if it exceeded the value of 10
            sum_odd_position += int(self.id[i]) * 2 if int(self.id[i]) * 2 < 10 else (int(self.id[i]) * 2) - 9

        # Sum of each value in even positions
        sum_even_position = 0

        # Travels id in even positions except the last position
        for i in range(1, len(self.id) - 2, 2):
            # Add each value to sum_even_position
            sum_even_position += int(self.id[i])
        
        # check digit is 10 minus the modulus of the sum of even and odd values, if the result of the modulus is 0, the check digit is 0
        verifier_digit = 0 if (sum_even_position + sum_odd_position) % 10 == 0 else 10 - (sum_even_position + sum_odd_position) % 10

        return verifier_digit == int(self.id[-1])