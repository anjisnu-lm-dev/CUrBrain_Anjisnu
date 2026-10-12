def sum_modulo(arr):
    MOD = 1000000007
    result = 0
    for value in arr:
        result = (result + value) % MOD
    return result
if __name__ == "__main__":
    print(sum_modulo([1000000000, 1000000000, 1000000000])) 
    print(sum_modulo([1, 2, 3, 4]))                          
    print(sum_modulo([]))                                   
    print(sum_modulo([1000000007]))                          
    print(sum_modulo([0, 0, 0]))  