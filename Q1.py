def has_even_digits(n):
    t = abs(n)
    if t == 0:
        return False

    count = 0
    while t != 0:
        t //= 10
        count += 1

    return count % 2 == 0
def main():
    print(has_even_digits(1234))
    print(has_even_digits(-567))
    print(has_even_digits(0))
    print(has_even_digits(-45))
if __name__ == "__main__":
    main()

