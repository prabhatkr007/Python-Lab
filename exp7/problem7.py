#VII. Write a Python program to convert list to list of dictionaries. 

def list_to_dict(list1, list2):
    result = []
    for i in range(len(list1)):
        dict1 = {}
        dict1['color_name'] = list1[i]
        dict1['color_code'] = list2[i]
        result.append(dict1)
    return result

# Example usage:
list1 = ["Black", "Red", "Maroon", "Yellow"]
list2 = ["#000000", "#FF0000", "#800000", "#FFFF00"]
result = list_to_dict(list1, list2)
print(result) 