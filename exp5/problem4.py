
# IV. Write a Python program to create two strings from a given string. Create the first string using 
# those characters which occurs only once and create the second string which consists of multi-time occurring 
# characters in the said string.


def check(str):
    str1 = ""
    str2 = ""
    for i in str:
        if str.count(i) > 1 and i not in str1:
            str1 = str1+i
        elif str.count(i) == 1:
            str2 = str2+i
    return str1, str2


str = input("Enter String: ")
str1, str2 = check(str)
print(str1, str2)
