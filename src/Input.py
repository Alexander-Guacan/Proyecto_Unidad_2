import keyboard

class Input:

    @classmethod
    def integer(cls, message: str, min: int, max: int, signed = True) -> int:
        print(message, end='', flush=True)

        value = str()
        key_press = str()
        
        while key_press != "enter" or len(value) < min:
            key_press = str(keyboard.read_key(suppress=True))

            if len(key_press) == 1 and (key_press.isnumeric() or (key_press == '-' and signed and len(value) == 0)) and len(value) < max:
                if key_press == '-':
                    min += 1
                    max += 1

                value += key_press
                print(key_press, end='', flush=True)
            elif key_press == "backspace" and len(value) >= 1:
                if value[-1] == '-':
                    min -= 1
                    max -= 1

                value = value.removesuffix(value[-1])
                print('\b \b', end='', flush=True)

            key_press = keyboard.read_key(suppress=True)

        print()

        return int(value)
    
    @classmethod
    def floating(cls, message: str, min: int, max: int, signed=True) -> float:
        print(message, end='', flush=True)

        value = str()
        key_press = str()
        
        while key_press != "enter" or len(value) < min:
            key_press = str(keyboard.read_key(suppress=True))

            if len(key_press) == 1 and key_press.isnumeric() and len(value) < max:
                value += key_press
                print(key_press, end='', flush=True)
            elif (key_press == '-' and len(value) == 0 and signed) or (key_press == '.' and '.' not in value):
                min += 1
                max += 1

                value += key_press
                print(key_press, end='', flush=True)
            elif key_press == "backspace" and len(value) >= 1:
                if value[-1] == '-' or value[-1] == '.':
                    min -= 1
                    max -= 1

                value = value.removesuffix(value[-1])
                print('\b \b', end='', flush=True)

            key_press = keyboard.read_key(suppress=True)

        print()

        return float(value)
    
    @classmethod
    def string(cls, message: str, characters, min: int, max: int, space= False, mask="") -> str:
        print(message, end='', flush=True)

        string = str()
        key_press = str()
        
        while key_press != "enter" or len(string) < min:
            key_press = str(keyboard.read_key(suppress=True))

            if len(key_press) == 1 and characters(key_press) and len(string) < max:
                string += key_press
                print(key_press if len(mask) == 0 else mask, end='', flush=True)

            elif key_press == "space" and space and len(string) < max:
                string += ' '
                print(' ', end='', flush=True)

            elif key_press == "backspace" and len(string) >= 1:
                string = string.removesuffix(string[-1])
                print('\b \b', end='', flush=True)

            key_press = keyboard.read_key(suppress=True)

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