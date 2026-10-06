def factor(n,k):
    fac=[]
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            fac.append(i)
            if i!=n//i:
                fac.append(n//i)
    fac.sort()
    if len(fac)<k:
        return -1
    else:
        return fac[k-1]
def main():
    print(factor(12,3))
    print(factor(1,1))
    print(factor(12,6))
    print(factor(12,7))
    print(factor(36,5))


if __name__ == "__main__":
    main()
