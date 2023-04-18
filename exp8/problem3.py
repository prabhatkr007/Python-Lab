list_of_tuples = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
new_list = [t for t in list_of_tuples if t]
print("New list:", new_list)