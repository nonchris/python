# a dict (short for dictionary) is a data structure that stores key-value pairs
# so we give a value a name (the key) and can access the value by its name
# example:
my_dict = {
    "key1": "value1",
    "key2": "value2"
}

# print the whole dict
print(my_dict)

# extract the value of 'key1'
value = my_dict["key1"]
print(value)

# we can add values to a dict, by writing the name of the key in square brackets
# and assigning a value to it using the = operator
my_dict["key3"] = "value3"

# let's check the new dict
print(my_dict)

# we can also change the value of a key
my_dict["key3"] = "new value"

# now let's see if the value has changed
value3 = my_dict["key3"]
print(value3)

# TODO: print the value of 'key2'


# TODO: add a new key-value pair to the dict
#  the key should be 'my_key' and the value 'my_value' and print it


# TODO: print the length of the dict
#  hint: use the len() function


# TODO: change the value of 'key1' to 3


# TODO: add one to the value of 'key1'


# TODO: print the new value of 'key1'
