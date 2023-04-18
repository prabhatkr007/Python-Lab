list_of_tuples = [(1, 2), (3, 4), (5, 6)]
unzipped = list(zip(*list_of_tuples))
list1 = list(unzipped[0])
list2 = list(unzipped[1])
print("List 1:", list1)
print("List 2:", list2)