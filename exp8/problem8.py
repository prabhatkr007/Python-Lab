from collections import defaultdict

list1 = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
list2 = [1, 2, 2, 3]

my_dict = defaultdict(set)

for k, v in zip(list1, list2):
    my_dict[k].add(v)

print(my_dict)