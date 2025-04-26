#Define variables num 1 and num 2
num1 = 2022
num2 = 9875

#Create function sum_of_digits
def sum_of_digits(number):
    #Define digit sum to be 0
    digit_sum = 0

    #Create list of the digits by converting them into a string
    #mapping int to each character in the string and converting it into a list
    number_list = list(map(int,str(number)))

    #For each loop that adds each digit to the digit_sum variable
    for digit in number_list:
        digit_sum += digit

    #Prints the output of the operations
    print(digit_sum)

#Calling the function
sum_of_digits(num1)
sum_of_digits(num2)