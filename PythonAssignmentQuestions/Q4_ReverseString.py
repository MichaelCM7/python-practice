test_string_1 = "Hello!"
test_string_2 = "Racecar"

def reverse_string(string):
    character_list = list(string)
    reversed_list = []
    #print(character_list)
    n = (len(character_list) - 1)

    for char in range(len(character_list)):
        reversed_list.append(character_list[n])
        n = n-1

    print("".join(reversed_list))

reverse_string(test_string_1)
reverse_string(test_string_2)

"""
#Efficient 

def reverse_string(string):
    reversed_list = []
    for i in range(len(string) - 1, -1, -1):
        reversed_list.append(string[i])
    print("".join(reversed_list))
"""