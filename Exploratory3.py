# -*- coding: utf-8 -*-
import re

# first, the program opens a text file
# and converts the contents of the file into a single string
book = open("candide.txt", "r")
split = book.read()

# this function takes a string,
# puts every word in that string ending in 'at' in a new list of strings,
# identifies every element in that list that is more than 3 letters long,
# puts those elements into a second list of strings,
# and returns that second list of strings

# in other words, it returns a list of all words ending in 'at'
# that are more than 3 letters long
def find_ats(words_to_test):
    if type(words_to_test) != str:
        raise TypeError("The argument provided was not of type str")
    ats = []
    words = re.findall(r'[\w]*at\b', words_to_test)
    for word in words:
        if len(word) > 3:
            ats.append(word)
    return ats

print find_ats(split)
