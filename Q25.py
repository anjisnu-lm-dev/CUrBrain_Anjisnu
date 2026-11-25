def closest_pair(temps, target):
    left = 0
    right = len(temps) - 1
    best_pair = (temps[left], temps[right])
    best_diff = abs(temps[left] + temps[right] - target)
    while left < right:
        total = temps[left] + temps[right]
        diff = abs(total - target)
        if diff < best_diff:
            best_diff = diff
            best_pair = (temps[left], temps[right])
        if total < target:
            left = left + 1
        elif total > target:
            right = right - 1
        else:
            break
    return best_pair


def main():
    print("Test Case 1:", closest_pair([10, 22, 28, 29, 30, 40], 54)) 
    print("Test Case 2:", closest_pair([1, 3, 5, 9], 8))               
    print("Test Case 3:", closest_pair([1, 2], 100))                   
    print("Test Case 4:", closest_pair([-4, -1, 2, 6], 3))             
    print("Test Case 5:", closest_pair([10, 20, 30], 5))               


main()

