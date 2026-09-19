# Task: Write a function is_even(n) that returns True if n is even,
# False otherwise.
#
# Then, in a loop, test it for every number from 1 to 10 and print
# each number alongside the result (e.g. "1 False", "2 True", ...).
#
# Notes coming from C:
# - No braces, no semicolons — blocks are defined by indentation.
# - Booleans are True/False (capitalized), not 1/0.
# - range() is the usual way to loop over a sequence of numbers.


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

for i in range(1,11):
    print(i ,is_even(i))