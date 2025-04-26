#Defining the array of numbers to be summed
numberList = [1,2,3,4,5,6,7,8,9,10]

#Creating the function list_summation
def list_summation(list_of_numbers):
    #Defining the variable sum and equating it to 0
    sum = 0

    #Using a for loop that goes through each item in the list
    for number in numberList:
        #Sums each item in the list
        sum += number

    #Print the output of the sum obtained
    print(f"Sum : {sum}")

#Calling the function
list_summation(numberList)