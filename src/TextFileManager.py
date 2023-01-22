from Serializable import Serializable

class TextFileManager:

    @classmethod
    def save(cls, serializable: Serializable, filename: str) -> None:
        file = open(filename, "a")
        file.write(serializable.saving_format())
        file.close()

    @classmethod
    def read(cls, serializable: Serializable, filename: str) -> list[object]:
        objects = list[object]()
        file = open(filename, "r")

        for line in file.readlines():
            objects.append(serializable.reading_format(line))

        file.close()
        
        return objects