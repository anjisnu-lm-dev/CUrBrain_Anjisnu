def reverse_and_double(n):
    rev=0
    if n>0:
        while n!=0:
            la=n%10
            n=n//10
            rev=rev*10+la
        return 2*rev
    elif n==0:
        return 0
    else:
        t=abs(n)
        while t!=0:
            la=t%10
            t=t//10
            rev=rev*10+la
        return -2*rev
def main():
    print(reverse_and_double(123))
    print(reverse_and_double(-45))
    print(reverse_and_double(0))
    print(reverse_and_double(1200))
    print(reverse_and_double(9))
if __name__ == "__main__":
    main()
