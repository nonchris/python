my_string = "abc"

# TODO: write an if statement that checks if the string is equal to "abc"
if my_string == "abc":
    print("The string is equal to 'abc'")

# TODO: you can check if two strings are not equal with !=
#  write an if statement that checks if the string is not equal to "abc"
if my_string != "abc":
    print("The string is not equal to 'abc'")

# TODO: check if the string has the length of 3
if len(my_string) == 3:
    print("The string has a length of 3")

my_string_2 = "Hello World"
my_string_2_split = my_string_2.split(" ")  # split on space
# now my_string_2_split is a list with two elements: ["Hello", "World"]
print(my_string_2_split)

# TODO: write a for loop that prints the elements in my_string_2_split
for word in my_string_2_split:
    print(word)

my_new_string = "Hello, how are you?"
# TODO: split that string into a list of words and print the list
word_list = my_new_string.split(" ")
print(word_list)

# You can check if a string contains a partial string with the in operator
if "a" in "abc":
    print("a is in abc")

# TODO: write an if statement that checks if "you" is in my_new_string
if "you" in my_new_string:
    print("'you' is in my_new_string")

# you can negate a statement with the not operator
if "a" not in "abc":
    print("a is not in abc")

# TODO: write a for loop that prints all elements in my_string_2_split that do not contain "o"
for word in my_string_2_split:
    if "o" not in word:
        print(word)
