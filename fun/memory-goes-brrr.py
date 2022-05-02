""" A short but effective way to allocate all your memory :) """

x = [42]

# simply append all values of x in each iteration over the next element of x
# x will grow exponentially and the for-loop will never end - beautiful
for i in x:
    x.extend(x)
