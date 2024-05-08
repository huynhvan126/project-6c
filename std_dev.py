# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 05/08/2024
# Description: defining the Person class, get_age method, and the std_dev function.
class Person:
    """represent a person with name and age"""
    def __init__(self, name, age):
        """initialize a person with name and age"""
        self.__name = name
        self.__age = age
    def get_age(self):
        return self.__age
def std_dev(people):
    if not people:
        return None
    # Calculate the mean of age
    total_age = sum(person.get_age() for person in people)
    mean_age = total_age / len(people)
    # Calculate the sum of squares of differences from the mean
    sum_squares_diff = sum((person.get_age() - mean_age) ** 2 for person in people)
    # Calculate the population of standard deviation
    std_dev = (sum_squares_diff / len(people)) ** 0.5
    return std_dev