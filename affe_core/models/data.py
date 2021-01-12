from abc import ABC


class BaseData(ABC):
    pass


class RawData(BaseData, ABC):
    pass


class SonicRawData(RawData):
    pass


class AmmoniaRawData(RawData):
    pass
