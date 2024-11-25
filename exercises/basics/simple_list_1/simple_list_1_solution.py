"""
Remember:
You can always run the code to try!
Don't worry if not everything is working yet :)
Always try to understand the error messages!
The code behind the # is a hint on how to start,
you can remove the # and space behind it and use it as a start!
"""

"""
A list is a collection of values.
It can be used to store multiple values in one variable.
The values can have different types.
Lists are indexed starting at 0.
So the first element of a list is at index 0.
"""

# recommended tasks to do before this:
# 1. simple_if_2.py

my_list = [1, "a string", 3.1415, 4, 5]

print(my_list)
print(type(my_list))

# extract the first element by using those square brackets with the index
first_element = my_list[0]
print(first_element)

# print the second element of the list
second_element = my_list[1]
print(second_element)

# print the length of the list
len_of_list = len(my_list)
print(len_of_list)


# write an if statement that checks if the list is longer than five
#  if it is, print a message that the list is longer
if len(my_list) > 5:
    print("The list is longer than five elements.")

# add an else that informs that the list is shorter than five
else:
    print("The list is shorter than five elements.")