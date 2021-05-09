# https://towardsdatascience.com/https-towardsdatascience-com-python-basics-mutable-vs-immutable-objects-829a0cb1530a
# https://www.youtube.com/watch?v=5qQQ3yzbKp8
# Mutable objects: list, dict, set
# Immutable objects:int, float, complex, string, tuple
from inspect import currentframe as cf
import os
os.system('cls')

# Immutable objects:int, float, complex, string, tuple
print('      --- STRINGS are IMMUTABLE ---\n')
string1 = "john"
string2 = "john"

print(f"{cf().f_lineno} | string1 = '{string1}' at address {id(string1)}")
print(f"{cf().f_lineno} | string2 = '{string2}' at address {id(string2)}")
print(f"{cf().f_lineno} | string1 is string2 = {string1 is string2}\n")

# string1 = 'mary'
# print(f"{cf().f_lineno} | string1 = '{string1}' at address {id(string1)}")
# print(f"{cf().f_lineno} | string2 = '{string2}' at address {id(string2)}")
# print(f"{cf().f_lineno} | string1 is string2 = {string1 is string2}")

# # ======================================================================

# # Mutable objects: list, dict, set
# print('\n\n      --- LISTS are MUTABLE ---\n')
# values = [4, 5, 6]
# values2 = values

# print(f"{cf().f_lineno} | {id(values)} {values}")
# print(f"{cf().f_lineno} | {id(values2)} {values2}")
# print(f"{cf().f_lineno} | values is values2 = {values is values2}\n")

# values.append(7)
# print(f"{cf().f_lineno} | {id(values)} {values}")
# print(f"{cf().f_lineno} | {id(values2)} {values2}")
# print(f"{cf().f_lineno} | values is values2 = {values is values2}")
