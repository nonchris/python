# We can define the expected type of a variable
# by writing ' : type' after the variable name
# example:
# we define that x and y shall be integers
# this is possible with every type
def do_add(x: int, y: int):
    result = x + y
    print(result)


#  add reasonable typehints to that function
def add_strings(str_1: str, str_2: str):
    result = str_1 + str_2
    print(result)

#  write a function that takes three ints, adds them together and prints the result
#  add typehints to the parameters
def add_three_ints(x: int, y: int, z: int):
    result = x + y + z
    print(result)
