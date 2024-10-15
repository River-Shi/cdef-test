from dataclasses import dataclass

@dataclass(slots=True)
class BookL1:
    exchange: str
    symbol: str
    bid: float
    ask: float
    bid_size: float
    ask_size: float
