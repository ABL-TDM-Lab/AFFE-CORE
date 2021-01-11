from abc import ABC, abstractmethod


class ConsoleAction(ABC):
    serial: int
    desc: str

    def __init__(self, *, serial: int):
        self.serial = serial
        setattr(self, 'desc', getattr(self, 'desc', f'<{self.__class__.__name__}>'))

    @abstractmethod
    def __call__(self, *args, **kwargs) -> str:
        pass

    def __repr__(self):
        return f'{self.serial}. {self.desc}'
