def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def array_gcd(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        result = gcd(result, arr[i])
    return result


def main():
    print(array_gcd([24, 36, 48]))
    print(array_gcd([33, 44, 55, 66]))
    print(array_gcd([17]))
    print(array_gcd([12, 18, 24, 30]))
    print(array_gcd([1, 7, 14, 28]))


if __name__ == "__main__":
    main()
