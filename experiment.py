# a = 1
# b = 2
# print("----------------------")

# print(globals())
# glbs = dict(globals())

# for var in glbs:
#     print(var[0])
#     if var == "a":
#         print(var, a, var[0])

# print(glbs['a'])


# # locs = dict(locals())
# # for loc in locs:
# #     print(loc)

# dict = {'Name': 'Zara', 'Age': 7}
# print("Value : %s")
# print("Value : %s" % dict.keys())

print("----------------------")
thisdict = {'Name': 'Zara', 'Age': 7}
print(thisdict.keys())
print(thisdict.values())
for key in thisdict.keys():
    print(key, thisdict[key])
