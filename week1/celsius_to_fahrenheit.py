# Task: Read a Celsius temperature from the user with input(),
# convert it to Fahrenheit, and print the result.
#
# Formula: F = C * 9/5 + 32
#
# Notes coming from C:
# - input() always returns a str, even if the user types a number.
#   You'll need to convert it yourself before doing math on it.



C = int(input("enter the nr"))

Celsius_To_Farenhite = C * 9/5 + 32

print(Celsius_To_Farenhite)