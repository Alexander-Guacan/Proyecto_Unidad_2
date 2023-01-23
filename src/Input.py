import keyboard

class Input:

    @classmethod
    def integer(cls, message: str, min: int, max: int, signed = True) -> int:
        """Input characters: 0-9 and '-' if signed parameter is true

        Args:
            message (str): _description_ Message to print before input data
            min (int): _description_ Minimum digits for a valid number
            max (int): _description_ Maximum digits for a valid number
            signed (bool, optional): _description_. Defaults to True. True: enable '-' character, False: disable '-' character

        Returns:
            int: _description_ string input casting to integer value
        """
        # Print message without new line and force flush print
        print(message, end='', flush=True)
        
        # String that contains the input
        value = str()
        # String that save each key press
        key_press = str()
        
        # An string not is valid until press Enter key and input the minimum characters
        while key_press != "enter" or len(value) < min:
            # Save key press on the keyboard
            key_press = str(keyboard.read_key(suppress=True))

            # If key press is numeric or press the '-' character at begin of string
            if len(key_press) == 1 and (key_press.isnumeric() or (key_press == '-' and signed and len(value) == 0)) and len(value) < max:
                # '-' character not count like a digit
                if key_press == '-':
                    min += 1
                    max += 1
                # Concatenates key press
                value += key_press
                # Print key press valid
                print(key_press, end='', flush=True)
            # If press backspace key and exist characters to erase
            elif key_press == "backspace" and len(value) >= 1:
                # '-' character has been erase
                if value[-1] == '-':
                    min -= 1
                    max -= 1
                
                # Pop last character
                value = value.removesuffix(value[-1])
                # Simulates erase of backspace key
                print('\b \b', end='', flush=True)
            
            # Release flush
            keyboard.read_key(suppress=True)
        
        # Simulates enter key
        print()

        return int(value)
    
    @classmethod
    def floating(cls, message: str, min: int, max: int, signed=True) -> float:
        """Input characters: 0-9 and '-' if signed is true

        Args:
            message (str): _description_ Message to print before input data
            min (int): _description_ Minimum digits for a valid number
            max (int): _description_ Maximum digits for a valid number
            signed (bool, optional): _description_. Defaults to True. True: enable '-' character, False: disable '-' character

        Returns:
            float: _description_ string input casting to floating value
        """
        # Print message without new line and force flush print
        print(message, end='', flush=True)
        
        # String that contains the input
        value = str()
        # String that save each key press
        key_press = str()
        
        # An string not is valid until press Enter key and input the minimum characters
        while key_press != "enter" or len(value) < min:
            # Save key press on the keyboard
            key_press = str(keyboard.read_key(suppress=True))
            
            # Key press is numeric
            if len(key_press) == 1 and key_press.isnumeric() and len(value) < max:
                # Concatenates characters to output
                value += key_press
                # Print key press valid
                print(key_press, end='', flush=True)
            # Key press is '-' and is the first character or '.' character if enter once time
            elif (key_press == '-' and len(value) == 0 and signed) or (key_press == '.' and '.' not in value):
                # '.' or '-' not count like digit
                min += 1
                max += 1
                
                # Concatenates characters to output
                value += key_press
                # Print key press valid
                print(key_press, end='', flush=True)
            # If press backspace key and exist characters to erase
            elif key_press == "backspace" and len(value) >= 1:
                if value[-1] == '-' or value[-1] == '.':
                    min -= 1
                    max -= 1

                # Pop last character
                value = value.removesuffix(value[-1])
                # Print key press valid
                print('\b \b', end='', flush=True)

            # Release flush
            keyboard.read_key(suppress=True)

        # Simulates enter key
        print()

        return float(value)
    
    @classmethod
    def string(cls, message: str, characters, min: int, max: int, space= False, mask="") -> str:
        """_summary_

        Args:
            message (str): _description_
            characters (_type_): _description_ lambda function that indicates valid characters. Example. lambda char: char >= 'a' and char <= 'z' (Only can input characters between a and z in lowercase). 
            min (int): _description_ Minimum characters for a valid string
            max (int): _description_ Maximum characters for a valid string
            space (bool, optional): _description_. Defaults to False. Active space key to print
            mask (str, optional): _description_. Defaults to "". Replace characters output for a specified character. Example. mask=*. If input "1234" the output in console is "****", only change the view, the string output is the same.

        Returns:
            str: _description_ Input like a string
        """
        # Print message without new line and force flush print
        print(message, end='', flush=True)

        # String that contains the input
        string = str()
        # String that save each key press
        key_press = str()
        
        # An string not is valid until press Enter key and input the minimum characters
        while key_press != "enter" or len(string) < min:
            # Save key press on the keyboard
            key_press = str(keyboard.read_key(suppress=True))
            
            # If character is the specified in characters function
            if len(key_press) == 1 and characters(key_press) and len(string) < max:
                # Concatenates characters to output
                string += key_press
                # Print key press valid
                print(key_press if len(mask) == 0 else mask, end='', flush=True)

            # If key press is space
            elif key_press == "space" and space and len(string) < max:
                # Concatenates characters to output
                string += ' '
                # Print key press valid
                print(' ', end='', flush=True)

            # If press backspace key and exist characters to erase
            elif key_press == "backspace" and len(string) >= 1:
                # Pop last character
                string = string.removesuffix(string[-1])
                # Print key press valid
                print('\b \b', end='', flush=True)

            # Release flush
            keyboard.read_key(suppress=True)

        # Simulates enter key
        print()

        return string
    
    @classmethod
    def numeric(cls, message: str, min: int, max: int) -> str:
        return cls.string(message, lambda char: char.isnumeric(), min, max)
    
    @classmethod
    def alphabetic(cls, message: str, min: int, max: int, space=True) -> str:
        return cls.string(message, lambda char: char.isalpha(), min, max, space)
    
    @classmethod
    def alphanumeric(cls, message: str, min: int, max: int, space=True) -> str:
        return cls.string(message, lambda char: char.isalnum(), min, max, space)