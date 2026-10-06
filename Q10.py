def count_primes(n):
    if n <= 2:
        return 0
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False
    for p in range(2, int(n**0.5)+1):
        if is_prime[p]:
            for j in range(p*p, n, p):
                is_prime[j] = False
    count = 0
    for i in range(n):
        if is_prime[i]:
            count = count + 1
    return count


def main():
    print(count_primes(10))
    print(count_primes(2))
    print(count_primes(0))
    print(count_primes(3))
    print(count_primes(30))


if __name__ == "__main__":
    main()