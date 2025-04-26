#Defining the variables of num 1 and num 2
num1 = 14
num2 = 15

#Creating the function even_or_odd_checker
def even_or_odd_checker(number):
    #Checks the number variable to ensure that it is not a float
    if isinstance(number,float):
        print("Invalid Entry! Even and Odd only applies to Integers")
    else:
        #Defining remainder which is the modulus of the number passed and 2
        remainder = number % 2
        #Checks if the remainder is not 0 to assign odd or even
        if remainder != 0:
            print(f"The number {number} is odd")
        else:
            print(f"The number {number} is even")

#Calling the function
even_or_odd_checker(num1)
even_or_odd_checker(num2)