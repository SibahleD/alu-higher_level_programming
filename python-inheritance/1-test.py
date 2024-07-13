#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

new_list = MyList()
new_list.append(5)
new_list.append(3)
new_list.append(8)


print("ID of new_list:", id(new_list))
print("ID of sorted_list:", id(sorted_list))
print(id(new_list) != id(new_list.print_sorted()))
