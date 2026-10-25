# write a python program to check that a string contains only a certain set of characters (in this case a-z,A-Z and 0-9)
import re

s = input("Enter a string: ")

if re.fullmatch(r'[a-zA-Z0-9]+', s):
    print("String contains only letters and digits")
else:
    print("String contains other characters")