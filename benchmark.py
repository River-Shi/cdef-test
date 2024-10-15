from trade_types import BookL1 as CBookL1
from utils import BookL1
import timeit

def create_book_l1():
    return BookL1("binance", "BTC/USDT", 30000.0, 30001.0, 1.5, 2.0)

def create_cbook_l1():
    return CBookL1("binance", "BTC/USDT", 30000.0, 30001.0, 1.5, 2.0)


def access_book_l1(book):
    exchange = book.exchange
    symbol = book.symbol
    bid = book.bid
    ask = book.ask
    bid_size = book.bid_size
    ask_size = book.ask_size
    return exchange, symbol, bid, ask, bid_size, ask_size

def run_benchmark(class_type, create_func, iterations=1000000):
    creation_time = timeit.timeit(create_func, number=iterations)
    
    instance = create_func()
    access_time = timeit.timeit(lambda: access_book_l1(instance), number=iterations)
    
    print(f"{class_type} Benchmark Results:")
    print(f"Creation time: {creation_time:.6f} seconds")
    print(f"Access time:   {access_time:.6f} seconds")
    print()

if __name__ == "__main__":
    run_benchmark("Python BookL1", create_book_l1)
    run_benchmark("Cython CBookL1", create_cbook_l1)
