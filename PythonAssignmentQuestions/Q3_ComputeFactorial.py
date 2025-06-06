#Defining the variable num to be 5
num = 5

#Creating the function compute_factorial
def compute_factorial(number):
    #Defining factorial_result to be 1 to allow for multiplication
    factorial_result = 1

    #Creating a while loop
    while number > 0:
        #Multiplies factorial_result by the number variable
        factorial_result *= number

        #Decreases number variable by 1 to ensure that
        #it follows the correct factorial formula
        number -= 1

    #Prints the factorial
    print(factorial_result)

#Calls the function
compute_factorial(num)
