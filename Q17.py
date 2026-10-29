
def most_popular_item(sales):
    freq = {}

    for item in sales:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    max_freq = max(freq.values())
    result = []

    for item in freq:
        if freq[item] == max_freq:
            result.append(item)

    return min(result)


def main():
    sales = [101, 103, 101, 102, 103, 105, 101, 103]
    print(most_popular_item(sales))

    sales = [5, 5, 5, 2, 2, 2, 2]
    print(most_popular_item(sales))

    sales = [99]
    print(most_popular_item(sales))

    sales = [-2, -2, 3, 3, 0]
    print(most_popular_item(sales))

    sales = [4, 1, 4, 1, 7]
    print(most_popular_item(sales))


if __name__ == "__main__":
    main()
