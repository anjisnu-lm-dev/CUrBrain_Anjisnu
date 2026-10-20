def min_absolute_value(arr):
    best = arr[0]
    for x in arr:
        if abs(x) < abs(best):
            best = x
    return best
if __name__ == "__main__":
    print(min_absolute_value([10, -5, -2, 4, 2]))   
    print(min_absolute_value([-3, 3]))              
    print(min_absolute_value([0, -1, 1]))           
    print(min_absolute_value([7, -7, 4]))           
    print(min_absolute_value([5, -2, 2, -1]))       