#Define variables with the strings "Hello!" and "Racecar"
test_string_1 = "Hello!"
test_string_2 = "Racecar"

#Defining the function reverse_string
def reverse_string(string):
    #Defining a variable that converts the string into a list
    character_list = list(string)

    #Defining an empty list that will contain the reversed list
    reversed_list = []

    #Defines n to be the last index
    n = (len(character_list) - 1)

    #Create a for loop in the range of items in character_list
    for char in range(len(character_list)):
        #Adding the last item in character_list to reversed_list
        reversed_list.append(character_list[n])

        #Decreasing the last index by 1 to ensure all characters are added
        n = n-1

    #Prints a string of joined characters
    print("".join(reversed_list))

#Calling the function
reverse_string(test_string_1)
reverse_string(test_string_2)

"""
#Explore More Efficient -v Later 

def reverse_string(string):
    reversed_list = []
    for i in range(len(string) - 1, -1, -1):
        reversed_list.append(string[i])
    print("".join(reversed_list))
"""