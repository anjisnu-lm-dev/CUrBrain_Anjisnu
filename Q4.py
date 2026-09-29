def subtract(n):
    s=0
    prod=1
    if n>0:
        while n!=0:
            a=n%10
            n=n//10
            prod=prod*a
            s=s+a
        return prod-s
    else:
        return "Invalid Input"
def main():
    print(subtract(234))
    print(subtract(123))
    print(subtract(5))
    print(subtract(100))
    print(subtract(999))
if __name__ == "__main__":
    main()
