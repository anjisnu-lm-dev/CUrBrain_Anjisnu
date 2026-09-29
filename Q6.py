def absolute_dif(n,a,b):
    if n < 0 or not (0 <= a <= 9) or not (0 <= b <= 9):
        return "Invalid Input"
    elif n == 0:
        ca = 0
        cb = 0
        if a == 0:
            ca = 1
        if b == 0:
            cb = 1
        return abs(ca - cb)
    else:
        ca=0
        cb=0
        while n!=0:
            x=n%10
            n=n//10
            if x==a:
                ca+=1
            if x==b:
                cb+=1
        return abs(ca-cb)
def main():
    print(absolute_dif(112231,1,2))
    print(absolute_dif(55555,5,2))
    print(absolute_dif(123456,3,6))
    print(absolute_dif(0,0,5))
    print(absolute_dif(1002001,0,1))
if __name__ == "__main__":
    main()

