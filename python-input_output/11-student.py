#!/usr/bin/python3
"""
Returning dictionary into a data structure
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dictionary represantation of instance"""
        if isinstance(attrs, list):
            for name in attrs:
                if isinstance(name, str) and name in self.__dict__:
                    my_dict[name] = self.__dict__[name]
            return my_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Sets replaces attributes of the instances"""
        for key in json:
            setattr(self, key, json[key])
