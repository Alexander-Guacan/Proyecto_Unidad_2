class Categories:
    __categories = ["accion", "terror", "aventura", "ciencia ficcion",
            "comedia", "documental", "drama", "fantasia", "musical", "animacion"]
    
    @classmethod
    def is_valid(cls, option: int) -> bool:
        return option > 0 and option <= len(cls.__categories)

    @classmethod
    def print(cls) -> None:
        print("[CATEGORIA]")
        i = 1
        for category in cls.__categories:
            print(f"{i}.- {category}")
            i += 1
    
    @classmethod
    def select(cls, option: int) -> str:
        return cls.__categories[option - 1]