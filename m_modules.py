### Modules ###

import module

module.sum(1, 2, 3)
module.printValue("Hello, this is a value from the module!")

from module import sum, printValue

sum(1, 2, 3)
printValue("Hello, this is a value from the module!")

import math

print(f"Square root of 16: {math.sqrt(16)}")
print(f"Pi: {math.pi}")
print(f"Factorial of 5: {math.factorial(5)}")
print(f"Cosine of 0: {math.cos(0)}")
print(f"Logarithm base 10 of 100: {math.log10(100)}")

from math import pi

print(f"Pi: {pi}")