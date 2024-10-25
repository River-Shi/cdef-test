from dataclasses import dataclass
from msgspec import Struct

@dataclass(slots=True)
class BookL1:
    exchange: str
    symbol: str
    bid: float
    ask: float
    bid_size: float
    ask_size: float


class BookL1Struct(Struct,gc=False):
    exchange: str
    symbol: str
    bid: float
    ask: float
    bid_size: float
    ask_size: float
