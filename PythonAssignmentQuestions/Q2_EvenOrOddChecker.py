num1 = 14
num2 = 15

def even_or_odd_checker(number):
    if isinstance(number,float):
        print("Invalid Entry! Even and Odd only applies to Integers")
    else:
        remainder = number % 2
        if remainder != 0:
            print(f"The number {number} is odd")
        else:
            print(f"The number {number} is even")

even_or_odd_checker(num1)
even_or_odd_checker(num2)