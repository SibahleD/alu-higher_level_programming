#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in my_list:
        if my_list[i] == search:
            new_row = list(map(lambda x: replace if x == search else x, my_list))        
            new_list.append(new_row)
        else:
            new_list.append(my_list[i])
        return new_list
