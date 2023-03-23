#     I. Write a Python program to multiplies all the items in a list.


#     V. Write a python program to check whether two lists are circularly identical.

#     VI. Write a Python program to convert a pair of values into a sorted unique array.

#     VII. Write a Python program to convert list to list of dictionaries. 
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]

#     VIII. Write a Python program to find a tuple, the smallest second index value from a list of tuples.

#     IX. Write a Python program to check if all dictionaries in a list are empty or not. 
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False

# Python program to multiply all values in the
# list using traversal


def multiplyList(myList):

	result = 1
	for x in myList:
		result = result * x
	return result


list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))
