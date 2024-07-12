#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

new_list = MyList()
new_list.append(5)
new_list.append(3)
new_list.append(8)
id(new_list) is not id(new_list.print_sorted())
