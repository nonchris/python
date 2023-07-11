"""
Remember:
You can always run the code to try!
Don't worry if not everything is working yet :)
Always try to understand the error messages!
The code behind the # is a hint on how to start,
you can remove the # and space behind it and use it as a start!
"""

"""
A for-loop is a method to go over a collection of values, like a list
and use each value in the collection to do something.
"""

# recommended tasks to do before this:
# simple_list_1.py

my_list = [1, "a string", 3.1415, 4, 5]

# TODO: write a for-loop that prints each element of the list
# for element in my_list:


# TODO: write a for-loop that prints the type of each element
# for

"""
We can define a variable above a for-loop and use it inside the for-loop
The cool thing is that the variable will keep the value in the next run of the loop.
"""
# example:
len_of_list = 0
for number in my_list:
    # in each step we just count one to the global variable
    len_of_list = len_of_list + 1
    print("Current number: " + len_of_list)

print(len_of_list)


my_number_list = [1, 2, 3, 4, 5]

# TODO: Write a for-loop that adds all numbers of the list together
my_sum = 0
# for
