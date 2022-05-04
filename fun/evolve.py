# 10  # if this number is set to five replacements will go wrong
import os

with open("evolve.py", "r") as f:
    code = f.read()

# cut number from first line, increment it by five
number = int(code.split("\n")[0].split(" ")[1].strip())
# replace incremented number in read code
new_code = code.replace(f"{number}", f"{number+5}")
print(number)

# break condition
if number >= 499:
    print("We did it!")
    exit()

# write new code
with open("evolve.py", "w") as f:
    f.write(new_code)

print("---")
# call the program again :D
# recursion - but in shitty :P
os.system('python3 $(pwd)/evolve.py')
