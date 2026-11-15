def suffix_sum(arr):
    total = 0
    i = len(arr) - 1
    while i >= 0:
        current = arr[i]
        arr[i] = total
        total = total + current
        i = i - 1
    return arr


def main():
    arr = [10, 4, 8, 3]
    print(suffix_sum(arr))

    arr = [5]
    print(suffix_sum(arr))

    arr = []
    print(suffix_sum(arr))

    arr = [-2, 5, -1]
    print(suffix_sum(arr))

    arr = [1, 2, 3, 4]
    print(suffix_sum(arr))


main()