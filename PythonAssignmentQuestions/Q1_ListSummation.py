numberList = [1,2,3,4,5,6,7,8,9,10]

def list_summation(list_of_numbers):
    sum = 0

    for number in numberList:
        sum += number

    print(f"Sum : {sum}")

list_summation(numberList)