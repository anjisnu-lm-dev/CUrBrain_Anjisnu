def threshold(sales,t):
    l=[]
    for i in sales:
        if i>=t:
            l.append(i)
    return l
def main():
    print(threshold(sales=[150,80,200,90,300],t=100))
    print(threshold(sales=[100,50,100], t=100 ))
    print(threshold(sales=[],t=50 ))
    print(threshold(sales=[10,20,30],t=40 ))
    print(threshold(sales=[75,75,75],t=75 ))
 

if __name__ == "__main__":
    main()