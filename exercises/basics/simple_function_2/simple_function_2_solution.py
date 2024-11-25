x_1 = 2
y_1 = 3

x_2 = 4
y_2 = 5

x_3 = 6
y_3 = 7

# x and y are parameters of the function
# these variables are only available inside the function
# their values are given when the function is called
def add_numbers(x, y):
    res = x + y
    # return is used to return a value from a function
    return res


res1 = add_numbers(x_1, y_1)
print(res1)
res2 = add_numbers(x_2, y_2)
print(res2)
res3 = add_numbers(x_3, y_3)
print(res3)
