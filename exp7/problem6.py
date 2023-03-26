
#     VI. Write a Python program to convert a pair of values into a sorted unique array.


def sorted_unique_array(a, b):
    arr = [a, b]
    arr = list(set(arr))
    arr.sort()
    return arr

# Example usage:
a = 3
b = 2
result = sorted_unique_array(a, b)
print(result) # Output: [2, 3]
