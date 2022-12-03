# Input() always returns string

import io

inpt1 = input("give input")
print(inpt1)

# Python program showing how to
# multiple input using split

# taking two inputs at a time
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
print()

# taking three inputs at a time
x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)
print()

# taking two inputs at a time
a, b = input("Enter two values: ").split()
print(f"First number is {a} and second number is {b}")
print()

# taking multiple inputs at a time
# and type casting using list() function
x = list(map(int, input("Enter multiple values: ").split()))
"""Here map(, ) maps intiger to the input values"""
print("List of students: ", x)

# another way of using list to take inputs
x = [int(x) for x in input("Enter multiple values: ").split()]
print("Number of list is: ", x)


# declare a dummy file
dummy_file = io.StringIO()

# add message to the dummy file
print('Hello Geeks!!', file=dummy_file)

# get the value from dummy file
dummy_file.getvalue()

# rounding of to two decimsl places
nm = 2.345
x1 = "{:.2f}".format(nm)
print(x1)

# some string formats
fname = 'hrithik'
lname = 'V'
fullname = f"{fname} {lname}"
print(fullname)

# some functions with parameters


def myfun(**kwargs):
    for key, value in kwargs.items():
        # this is treated as dict so must use .items() to iterate through values
        print(f"{key} == {value}")


myfun(first='hello', second='welcome', third='Python')
