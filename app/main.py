from typing import Callable


def cache(func: Callable) -> Callable:
    saving_cache = {}
    def wrapper(*args):
        if args in saving_cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            saving_cache[args] = func(*args)
        return saving_cache[args]
    return wrapper
