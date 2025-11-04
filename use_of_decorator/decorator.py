import time
import random


def time_function(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(f"Time taken : {end - start :3f}")
        return result

    return wrapper


@time_function
def create_list(length: int):
    return [num for num in range(length)]


if __name__ == "__main__":
    list_a = create_list(100_000_000)
