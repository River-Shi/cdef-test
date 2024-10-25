cimport cython

@cython.freelist(128)
cdef class BookL1:
    cdef readonly str exchange
    cdef readonly str symbol
    cdef readonly double bid
    cdef readonly double ask
    cdef readonly double bid_size
    cdef readonly double ask_size

    def __init__(self, str exchange, str symbol, double bid, double ask, double bid_size, double ask_size):
        self.exchange = exchange
        self.symbol = symbol
        self.bid = bid
        self.ask = ask
        self.bid_size = bid_size
        self.ask_size = ask_size
    
    def __repr__(self) -> str:
        return f"BookL1(exchange={self.exchange}, symbol={self.symbol}, bid={self.bid}, ask={self.ask}, bid_size={self.bid_size}, ask_size={self.ask_size})"
    
    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, BookL1):
            return False
        return self.exchange == __o.exchange and self.symbol == __o.symbol and self.bid == __o.bid and self.ask == __o.ask and self.bid_size == __o.bid_size and self.ask_size == __o.ask_size
