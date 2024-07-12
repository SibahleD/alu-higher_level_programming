#!/usr/bin/python3
"""
inheriting from 'list'
"""
class MyList(list):
    """inherits from list"""
    def lookup(obj):
        """return the list"""
        return dir(obj)
    
    def print_sorted(self):
        """"print the list in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
        return sorted_list

