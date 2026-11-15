def delete_by_value(arr, target):
    n = len(arr)
    index = -1

    i = 0
    while i < n:
        if arr[i] == target:
            index = i
            break
        i = i + 1

    if index == -1:
        return arr

    i = index
    while i < n - 1:
        arr[i] = arr[i + 1]
        i = i + 1

    arr.pop()
    return arr


def main():
    arr = [10, 20, 30, 20, 40]
    print(delete_by_value(arr, 20))

    arr = [5, 15]
    print(delete_by_value(arr, 99))

    arr = [7]
    print(delete_by_value(arr, 7))

    arr = []
    print(delete_by_value(arr, 3))

    arr = [4, 4, 4]
    print(delete_by_value(arr, 4))


main()