def findSmallest(items):
    smallest = items[0]
    smallest_index = 0
    for i in range(len(items)):
        if items[i] < smallest:
            smallest_index = i
            smallest = items[i]
    return smallest_index


assert findSmallest([1, 2, 3, 4]) == 0
assert findSmallest([2, 3, 1, 4]) == 2


def selectSort(items):
    newItems = []

    for i in range(len(items)):
        index = findSmallest(items)
        newItems.append(items.pop(index))

    return newItems


assert selectSort([1, 2, 3, 4]) == [1, 2, 3, 4]
assert selectSort([2, 3, 1, 4]) == [1, 2, 3, 4]
