def has_divisible_prefix(arr, k):
         if k == 0:         
            raise ValueError("k must be non-zero")       
         k = abs(k)     
         remainder = 0       
         for value in arr:         
              remainder = (remainder + value) % k         
              if remainder == 0:             
                return True       
         return False 
if __name__ == "__main__":
    print(has_divisible_prefix([4, 2, 9], 3))   
    print(has_divisible_prefix([1, 1, 1], 5))   
    print(has_divisible_prefix([5, 1], 5))     
    print(has_divisible_prefix([], 3))          
    print(has_divisible_prefix([-3, 1], 3))     