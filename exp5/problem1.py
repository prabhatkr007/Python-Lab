# I. Write a Python program to convert a string in a list.

def Convert(string):
    li = list(string.split(" "))
    return li
  
  

str1 = "I am iron man"
print(Convert(str1))
