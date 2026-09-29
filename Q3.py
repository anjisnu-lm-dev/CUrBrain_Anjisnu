def pallindrome_sumrev(n):
        rev=0
        t=abs(n)
        while t!=0:
            la=t%10
            t=t//10
            rev=rev*10+la
        
        if n < 0:
             return n - rev      
        if n == rev:
             return n            
        return n + rev

def main():
    print(pallindrome_sumrev(121))
    print(pallindrome_sumrev(123))
    print(pallindrome_sumrev(0))
    print(pallindrome_sumrev(-45))
    print(pallindrome_sumrev(120))
if __name__ == "__main__":
    main()

