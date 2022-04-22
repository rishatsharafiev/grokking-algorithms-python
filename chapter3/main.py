def look_for_key(box):
    for item in box:
        if item.is_box():
            return look_for_key(item)
        elif item.is_key():
            return item


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


assert factorial(10) == 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10
assert factorial(5) == 1 * 2 * 3 * 4 * 5
