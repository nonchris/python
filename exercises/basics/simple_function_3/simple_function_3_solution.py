my_dict = {}

# write a function that takes two arguments and adds them to the dict
# the first argument is the key, the second the value

def add_to_dict(key, value):
    my_dict[key] = value


# call the function twice with different arguments
# print the dict after each function call and inspect the result
add_to_dict("x", 1)
print(my_dict)
add_to_dict("y", 2)
print(my_dict)


# write a function that takes the name of a key and prints its value
def print_value(key):
    val = my_dict[key]
    print(val)

# we can check if a key exists in a dict with the 'in' keyword
# example:
d = {"x": 1}
if "x" in d:
    print("x is in d!")

# TODO: fstring syntax
# write a function that takes the name of a key and prints if it is in the dict
# also print that the key is not in the dict if it isn't
def print_if_in_dict(key):
    if key in my_dict:
        print(f"{key} is in my_dict")
    else:
        print(f"{key} is not in my_dict")
