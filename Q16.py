def second_highest_score(scores):
    highest = -1
    second = -1
    for x in scores:
        if x > highest:
            second = highest
            highest = x
        elif x < highest and x > second:
            second = x
    return second
if __name__ == "__main__":
    print(second_highest_score([50, 40, 50, 30]))   
    print(second_highest_score([100, 100, 100]))    
    print(second_highest_score([]))                 
    print(second_highest_score([10, 20, 30, 40]))   
    print(second_highest_score([5, 5, 4, 4, 3]))    