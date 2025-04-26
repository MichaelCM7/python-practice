num = 5

def compute_factorial(number):
    factorial_result = 1
    while number > 0:
        factorial_result *= number
        number -= 1

    print(factorial_result)

compute_factorial(num)

"""
#Lists Factors

def compute_factorial(number):
    factors = []
    factorial_result = 1
    while number > 0:
        result = number
        number -= 1
        factors.append(result)
        
    print(f"Factors : {factors}")

    for factor in factors:
        factorial_result *= factor

    print(factorial_result)
"""

