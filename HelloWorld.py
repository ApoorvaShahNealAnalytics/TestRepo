import pandas as pd

print("Hello World")

for i in range(10):
    print(i)


def long_function(param1, param2, param3=34, param4=[]):
    # This function is a function
    return "This is a function"


MESSAGE = long_function(1, 2, 4, [1, 2, 3])
print(MESSAGE)
