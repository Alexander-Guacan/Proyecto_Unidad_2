class Filter:
    __dict = {
        "Ninguno"   : "",
        "Titulo"    : "name",
        "Director"  : "director",
        "Categoria" : "category",
    }

    def __init__(self, type: str, matching: str) -> None:
        self.type = self.__dict[type]
        self.matching = matching

    def has_select(self) -> bool:
        return self.type != ""

    @classmethod
    def filters(cls) -> list[str]:
        return list(cls.__dict.keys())