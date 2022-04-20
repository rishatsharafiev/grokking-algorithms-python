def line(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("------------> ", result)
        return result

    return wrapper


@line
def binary_search(items, item):
    low = 0
    high = len(items) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = items[mid]

        print(guess, item, low, high, mid)
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


assert binary_search([1, 2, 3, 4, 5, 7], 2) == 1
assert binary_search([1, 2, 3, 4, 5, 7], 2) == 1
assert binary_search([1, 2, 3, 4, 5, 7], 7) == 5
assert binary_search([1, 2, 3, 4, 5, 7], -1) == None
