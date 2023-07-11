my_list = [1, "a string", 3, 4, 5]

# write a for loop that sums up all numbers in the list, print the result at the end
#  hint: you can use the type() function to check if the element is a number
# example:
x = 5
if type(x) == int:
    print("x is an integer")

my_sum = 0
for element in my_list:
    if type(element) == int:
        my_sum = my_sum + element


number_list = [1, 2, 3, 4, 5]
# sum all the numbers in the list print if the number is even or odd
# hint: you can use the modulo operator % to check if a number is even or odd
# the modulo operator returns the rest of a division
x = 5 % 2
print(x)

my_sum_2 = 0
for number in number_list:
    my_sum_2 = my_sum_2 + number

if my_sum_2 % 2 == 0:
    print(str(my_sum_2) + " is even")
else:
    print(str(my_sum_2) + " is odd")