#!/usr/bin/python3
"""
Returning dictionary into a data structure
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def to_json(self):
        return self.__dict__
