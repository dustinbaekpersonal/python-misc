
import bisect
import random


def binary_search(element: int, data: list[int]) -> int:
    """
    Find an index of an element.
    
    If it doesn't exist, find where to put.
    """
    low, high = 0, len(data) - 1

    while low <= high:

        mid = (low + high) // 2

        ele = data[mid]
        if element < ele:
            high = mid - 1
        elif element > ele:
            low = mid + 1
        else:
            return mid
    raise ValueError(f"element {element} doesn't exist in data.")

if __name__ == "__main__":
    data = [1,5,7,10, 100, 300, 400] 
    output = binary_search(1, data)
    data = [random.randint(0, 10) for _ in range(5)]
    print(data)
    output = bisect.bisect_left(data, 4)
    print(output)
        

