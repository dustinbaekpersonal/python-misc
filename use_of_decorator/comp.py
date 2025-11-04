import argparse
import logging
import random

from time_decorator import time_function

logging.basicConfig(level=logging.INFO)


def add_one(tmp: list[int]) -> list:
    return [item + 1 for item in tmp]


def subtract_one(tmp: list[int]) -> list:
    return [item - 1 for item in tmp]


# @time_function
def multiply_ten(tmp: list[int]) -> list:
    return [item * 10 for item in tmp]


@time_function
def main():
    tmp = [random.randint(-10, 10) for _ in range(100_000_00)]
    add_one_tmp = add_one(tmp)
    subtract_one_tmp = subtract_one(tmp)
    multiply_ten_tmp = multiply_ten(tmp)

    return add_one_tmp, subtract_one_tmp, multiply_ten_tmp


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "function",
        help="name of the functions where decorators will be used",
        type=str,
        nargs="+",
    )
    args = parser.parse_args()
    logging.info(f"{args.function}")

    a, b, c = main()
    logging.info(f"{a[:10]} \n {b[:10]} \n {c[:10]}")
