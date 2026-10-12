def power_modulo(base, power, mod): 
        if mod <= 0 or power < 0:
            raise ValueError("mod must be positive and power non-negative") 
        result = 1 % mod     
        base %= mod       
        for i in range(power): 
                    result = (result * base) % mod 
        return result 
if __name__ == "__main__":
    print(power_modulo(2, 10, 1000)) 
    print(power_modulo(2, 5, 10))     
    print(power_modulo(5, 0, 7))     
    print(power_modulo(7, 3, 1))     