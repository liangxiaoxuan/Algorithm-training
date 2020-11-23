

def quickort (arr):
    length = len(arr)
    if length <= 1:
        return arr

    else:
        pivot = arr.pop()

    items_greater = []
    items_lower = []

    for item in arr:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return quickort(items_lower) + [pivot] + quickort(items_greater)


if __name__ == '__main__':
    arr = [3, 4, 6, 1, 4]
    print(quickort(arr))