class Categories:
    """Movie categories

    Returns:
        _type_: _description_
    """

    # Movie categories
    __categories = ["accion", "terror", "aventura", "ciencia ficcion",
            "comedia", "documental", "drama", "fantasia", "musical", "animacion"]
    
    @classmethod
    def is_valid(cls, option: int) -> bool:
        """Returns true if option is inside of options to __categories

        Args:
            option (int): _description_ Position of __categories array

        Returns:
            bool: _description_ True: option between 0 and len(__categories), False: option out of range
        """
        return option > 0 and option <= len(cls.__categories)

    @classmethod
    def print(cls) -> None:
        """Prints the list of categories
        """
        # Title
        print("[CATEGORIA]")
        # Identifier of category
        i = 1
        for category in cls.__categories:
            # Print each category in categories
            print(f"{i}.- {category}")
            # Update identifier
            i += 1
    
    @classmethod
    def select(cls, option: int) -> str:
        """Returns string in position - 1 of option of __categories

        Args:
            option (int): _description_ Position in __categories array

        Returns:
            str: _description_ Categorie name
        """
        return cls.__categories[option - 1]