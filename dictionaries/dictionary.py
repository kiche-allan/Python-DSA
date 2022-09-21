# Dictionaries
#
# my_dict = {
#     'hey' : 'hello guys',
#     'hey2' : 'hello guys',
#     'hey3' : 'hello guys',
#     'hey4' : 'hello guys'
# }
mydict = {'a': 1, 'b': 2, 'c': 3}
print(mydict)
# My_dic.get(<key>)
# searches the dictionary and returns a corresponding value it finds otherwise it returns a zero


print(mydict.get('a'))
# mydict.clear()

# mydict.items()
# Returns a list of values in key and value pairs
print(list(mydict.items()))

# Returns a list of dictionary keys
print(mydict.keys())

#returns a list of ditionary values
print(mydict.values())
#if a key is preset in a dictionary, this function will remove the key and return the associated value
print(mydict.pop('a'))
print(mydict)

print(mydict.popitem(2))
print(mydict)

