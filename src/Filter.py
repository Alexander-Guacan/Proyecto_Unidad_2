class Filter:
    """Filter types associated of Movie class

    Attributes:
        __dict
        type
        matching

    Methods:
        has_select
        filters
    """

    __dict = {
        "Ninguno"   : "",
        "Titulo"    : "name",
        "Director"  : "director",
        "Categoria" : "category",
    }

    def __init__(self, type: str, matching: str) -> None:
        """Default constructor

        Args:
            type (str): _description_ Key of __dict
            matching (str): _description_ Matching value to type selected
        """
        # Value of __dict
        self.type = self.__dict[type]
        # Matching value to find in list
        self.matching = matching

    def has_select(self) -> bool:
        # Verifier that filter type is different of none
        return self.type != ""

    @classmethod
    def filters(cls) -> list[str]:
        """Returns list of filters

        Returns:
            list[str]: _description_ Keys of __dict
        """
        return list(cls.__dict.keys())