
def reverse_subsegment(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr


def main():
    arr = [10, 20, 30, 40, 50, 60]
    print(reverse_subsegment(arr, 1, 4))

    arr = [1, 2, 3, 4]
    print(reverse_subsegment(arr, 0, 3))

    arr = [7]
    print(reverse_subsegment(arr, 0, 0))

    arr = [1, 2, 3, 4, 5]
    print(reverse_subsegment(arr, 2, 4))

    arr = [1, 2, 3, 4, 5]
    print(reverse_subsegment(arr, 0, 2))


if __name__ == "__main__":
    main()
