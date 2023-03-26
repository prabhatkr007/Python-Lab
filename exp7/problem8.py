#     VIII. Write a Python program to find a tuple, the smallest second index value from a list of tuples.

def smallest_second_index(list1):
    smallest = float('inf')
    result = None
    for tup in list1:
        if tup[1] < smallest:
            smallest = tup[1]
            result = tup
    return result


list1 = [('a', 3), ('b', 2), ('c', 1)]
result = smallest_second_index(list1)
print(result)