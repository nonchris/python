my_str = "Hello World"

# You can combine multiple conditions with 'and' and 'or'
# example:
if "Hello" in my_str and len(my_str) > 5:
    print("The string contains 'Hello' and has a length greater than 5")


# TODO: write an if statement that checks if the string contains "Hello" and "World"
if "Hello" in my_str and "World" in my_str:
    print("The string contains both 'Hello' and 'World'")

# TODO: check if the string is longer than three letters and smaller than 15
if len(my_str) > 3 and len(my_str) < 15:
    print("The string is longer than three letters and smaller than 15")

# TODO: check that the string contains "Hello" or is shorter than three characters
if "Hello" in my_str or len(my_str) < 3:
    print("The string contains 'Hello' or is shorter than three characters")

# TODO: replace 'my_str_' with a string that contains only three characters
#  and check if the statement above still works
my_str_ = "Hi"
if "Hello" in my_str_ or len(my_str_) < 3:
    print("The string contains 'Hello' or is shorter than three characters")

my_str_2 = "An other string"

# TODO: check if my_str or my_str_2 is longer than five letters
if len(my_str) > 5 or len(my_str_2) > 5:
    print("Either my_str or my_str_2 is longer than five letters")
