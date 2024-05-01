import math
from math import factorial
from math import log2

month = str(input("Please enter your favorite month: "))
day = (input("Please enter your favorite day: "))
year = str(", 2024")

print(month, (day)+year)
print("Is the month alphanumberic?", month.isalnum())
print("How many 2's?", day.count("2"))
day = int(day)
print("Factorial:", factorial(day))
print("Log base 2:", log2(day))
