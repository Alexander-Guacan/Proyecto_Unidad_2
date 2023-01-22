from abc import ABC, abstractmethod, abstractstaticmethod

class Serializable(ABC):

    @abstractmethod
    def saving_format(self) -> str:
        pass

    @abstractmethod
    def reading_format(self, line: str) -> object:
        pass