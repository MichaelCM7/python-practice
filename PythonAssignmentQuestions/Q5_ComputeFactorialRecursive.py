#Define the variable num to be 7
num = 7

#Create the function compute_factorial_recursive
def compute_factorial_recursive(number):
    #Checks if number is 0 and returns 1 up the stack
    if number == 0:
        return 1
    else:
        # Recursively call compute_factorial_recursive to continue building the stack
        factorial =  number * compute_factorial_recursive(number - 1)
        return factorial

#Calls the function
recursive_factorial = compute_factorial_recursive(num)
print(recursive_factorial)