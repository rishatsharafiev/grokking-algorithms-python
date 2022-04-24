def sum(items):
    if len(items) == 0:
        return 0
    else:
        return items[0] + sum(items[1:])


assert sum([]) == 0
assert sum([7]) == 7
assert sum([2, 3, 4]) == 9


def count(items):
    if len(items) == 0:
        return 0
    else:
        return 1 + count(items[1:])


assert count([]) == 0
assert count([7]) == 1
assert count([2, 3, 4]) == 3


def raw_max(items):
    if len(items) == 1:
        return items[0]
    elif len(items) == 0:
        return None
    else:
        m = raw_max(items[1:])
        return m if m > items[0] else items[0]


assert raw_max([]) == None
assert raw_max([7]) == 7
assert raw_max([2, 3, 4]) == 4


# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):

    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return None


items = [1, 2, 3, 4, 5, 7]
low, high = 0, len(items) - 1
assert binary_search(items, low, high, 2) == 1
assert binary_search(items, low, high, 2) == 1
assert binary_search(items, low, high, 7) == 5
assert binary_search(items, low, high, -1) == None
