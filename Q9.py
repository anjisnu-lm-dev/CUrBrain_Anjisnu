def is_prime(x):
    if x < 2:
        return False
    for d in range(2, int(x**0.5)+1):
        if x % d == 0:
            return False
    return True


def next_prime(n):
    if n < 2:
        return 2
    x = n + 1
    while not is_prime(x):
        x = x + 1
    return x


def main():
    print(next_prime(14))
    print(next_prime(0))
    print(next_prime(1))
    print(next_prime(2))
    print(next_prime(17))


if __name__ == "__main__":
    main()