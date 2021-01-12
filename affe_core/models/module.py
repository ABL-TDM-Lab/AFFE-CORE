import sys
from abc import ABC
from logging import Logger, getLogger, INFO, basicConfig


class Module(ABC):
    _name: str
    _logger: Logger

    def __init__(self, name: str):
        self._name = name
        self._logger = getLogger(name)

    def __enter__(self):
        self._logger.log(INFO, f">>> Entering {self._name} >>>")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._logger.log(INFO, f">>> Exiting {self._name} >>>")


class DemoModule(Module):
    pass


if __name__ == "__main__":
    basicConfig(level=INFO, stream=sys.stdout)
    with DemoModule("Demo Module") as demo_module:
        print("Processing")
