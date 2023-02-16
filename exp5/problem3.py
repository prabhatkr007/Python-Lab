
    # III. Write a Python program to find all the common characters in lexicographical order from 
    # two given lower case strings. If there are no common letters print "No common characters".


str1 = "jogender singh"
str2 = "shally lohia"


def check(str1, str2):
    str = ""
    str1 = sorted(set(str1))
    str2 = sorted(set(str2))
    for i in str1:
        for j in str2:
            if i == j:
                str = str+i
    if str == "":
        return "No common characters"
    return str


print(check(str1, str2))
