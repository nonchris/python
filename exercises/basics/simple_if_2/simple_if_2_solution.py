my_string = "abc"

# compare my_string to "abc" and print a message if they are equal
if my_string == "abc":
    print("my_string is equal to 'abc'")


# check if the length of my_string is smaller than 5 and print a message if it is
# remember you can use the len() function to get the length of a string
if len(my_string) < 5:
    print("my_string is smaller than 5")


# add an elif statement that checks if the length is greater than ten
elif len(my_string) > 10:
    print("my_string is greater than 10")

# change my_string above so that it doesn't fulfill any of the conditions above
# possible solution: "abcdefg"


# Check your assumption by creating and 'else'-case that prints the actual length of the string
else:
    str_len = len(my_string)
    print(str_len)

"""
Additional info:
Such a statement as above is always started with an 'if'.

After that it can be followed by a set of optional 'elif' statements,
those will be tested from top to bottom all conditions (including the 'if') above fail.

The block can end with an optional 'else' statement,
that triggers if none of the conditions above are fulfilled.

Note: After an 'else' there can't be any more 'elif' or 'else' statements!

If you want to test for multiple cases and execute all cases that are true,
you can use multiple 'if' statements instead of 'elif' statements.
"""
