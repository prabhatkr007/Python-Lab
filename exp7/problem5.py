
#     V. Write a python program to check whether two lists are circularly identical.

def are_circularly_identical(list1, list2):
    if len(list1) != len(list2):
        return False
    list1 *= 2
    for i in range(len(list1)):
        if list1[i:i+len(list2)] == list2:
            return True
    return False

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 1, 2]
if are_circularly_identical(list1, list2):
    print("The two lists are circularly identical")
else:
    print("The two lists are not circularly identical")
