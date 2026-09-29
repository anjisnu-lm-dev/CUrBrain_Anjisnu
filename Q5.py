def replace_ev_dig(n):
    if n <= 0:
        return "Invalid Input"

    r = []
    while n != 0:
        a = n % 10
        n = n // 10
        if a % 2 == 0:
            r.append(0)
        else:
            r.append(a)

    r.reverse()  
    return r
def main():
    print(replace_ev_dig(258))
    print(replace_ev_dig(12345))
    print(replace_ev_dig(2468))
    print(replace_ev_dig(13579))
    print(replace_ev_dig(1002))
if __name__ == "__main__":
    main()
 
