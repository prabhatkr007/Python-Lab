# V. Write a Python program to find the index of a given string at which a given substring starts.
# If the substring is not found in the given string return 'Not found'.


def test(str1, str2):
    res = str1.find(str2)
    return format("index = %d" % res) if res != -1 else 'Not found'


str1 = input("Enter string: ")
str2 = input("Enter substring: ")
print(test(str1, str2))
