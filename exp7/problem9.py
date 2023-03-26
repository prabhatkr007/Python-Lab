#     IX. Write a Python program to check if all dictionaries in a list are empty or not. 


def all_empty(list1):
    for dict1 in list1:
        if bool(dict1):
            return False
    return True

# Example usage:
list1 = [{},{},{}]
result = all_empty(list1)
print(result) # Output: True

list2 = [{1,2},{},{}]
result = all_empty(list2)
print(result) # Output: False
