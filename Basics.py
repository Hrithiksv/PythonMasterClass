# for loop

import operator

for i in range(10):
    # By default print() func ends with new line. end=' ' specify that it ends with whitespace
    print(i, end=' ')
    if i == 6:
        break
print()
a2 = 9
b2 = 7
res = a2 if a2 < b2 else b2  # Ternary if statement
print(res)

# print() function with sep= & end=

print('G', 'F', sep='', end='')
print('G')
# \n provides new line after printing the year
print('09', '12', '2016', sep='-', end='\n')

print('Red', 'Green', 'Blue', sep=',', end='@')
print('geeksforgeeks')


# while look
i = 0
while i < 10:
    if i == 6:
        i += 1
        continue
    else:
        print(i, end=' ')
    i += 1
print()
# ==============================================================
# Strings
# string Methods - .lower() .upper() .count('ltr') .replace('old','new')
# Print statement with f-string
first_name = "John"
last_name = "Doe"

print(f"Hello, {first_name} {last_name}!")

st1 = "I'm hrithik"
print(st1)
print(st1[0])
print(st1[-1])
del st1

# Python program to
# format a output using
# string() method

cstr = "I love geeksforgeeks"

# Printing the center aligned
# string with fillchr
print("Center aligned string with fillchr: ")
print(cstr.center(40, '#'))
"""Output:
Center aligned string with fillchr: 
##########I love geeksforgeeks##########"""

# Printing the left aligned
# string with "-" padding
print("The left aligned string is : ")
print(cstr.ljust(40, '-'))
"""The left aligned string is : 
I love geeksforgeeks--------------------"""

# Printing the right aligned string
# with "-" padding
print("The right aligned string is : ")
print(cstr.rjust(40, '-'))
"""The right aligned string is : 
--------------------I love geeksforgeeks"""

# String alignment
String1 = "|{:<10}|{:^10}|{:>10}|".format('Geeks',
                                          'for',
                                          'Geeks')
print("\nLeft, center and right alignment with Formatting: ")
print(String1)
# Left, center and right alignment with Formatting:
# |Geeks     |   for    |     Geeks|
# To demonstrate aligning of spaces
String1 = "\n{0:^16} was founded in {1:<4}!".format("GeeksforGeeks",
                                                    2009)
print(String1)
# GeeksforGeeks   was founded in 2009 !
# ==============================================================

# List
list1 = ['this', 'is', 'python', 'programing', 100]
lis2 = ['art', 'education', 'sports']
print(list1[2])
print(list1[-4])
print(type(list1[-1]))
print(list1[1:3])
print(list1[::-1])  # reverse the list
print(list1.extend(lis2))  # adds items of lis2 to list1
print(list1.append('world'))  # adds item at last
print(list1.insert(2, 'hello'))  # inserts item at a specific position
list1.remove('this')
list1.pop()  # removes last item
list1.sort()  # sorts aplhabetical order
list1.sort(reverse=True)  # sorts in reverse order
list1.reverse()  # reverse it

list1_srt = ','.join(list1)


# Tuple
Tuple4 = tuple('geeks')
# tuple() - splits the characters OP: ('g','e','e','k','s')
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'geek')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)
print(Tuple4)

# Sets
set1 = set("geeksforgeeks")
# OP {'r', 's', 'o', 'f', 'e', 'k', 'g'}
# st= set("geeks","for","geeks")
# This is not allowed, insted pass list to a set: set(list[])
x = {1+2+2+3+4+5}  # this is a set
for i in set1:
    print(i)

set4 = {1, 2, 3, 4}
set5 = {3, 4, 5, 5, 6}
print(set4.intersection(set5))
print(set4.difference(set5))
print(set4.union(set5))

print(set1)
print(sorted(set1))  # sorted didnt work for string argument
set2 = set(["geeks", "for", "geeks"])
print(sorted(set2))

lst = [1, 2, 2, 8, 7, 9, 0, 6, 3, 4, 1, 4, 5]
print("printing set of list ", set(lst))

# Dictionarys
'''clear() – Remove all the elements from the dictionary
copy() – Returns a copy of the dictionary
get() – Returns the value of specified key
items() – Returns a list containing a tuple for each key value pair
keys() – Returns a list containing dictionary’s keys
pop() – Remove the element with specified key
popitem() – Removes the last inserted key-value pair
update() – Updates dictionary with specified key-value pairs
values() – Returns a list of all the values of dictionary'''
#               1           2            3
Dict1 = {1: "hrithik", 2: "welcome", 3: [1, 2, .4]}
print(Dict1)
print(Dict1.get(2))  # Index starts from 1 not 0
print(Dict1[1])
Dict1[4] = "to"      # adding elements to dictionary
Dict1[5] = "Hassan"
# Creating a Dictionary
Dict = {'Dict1': {1: 'Geeks'},
        'Dict2': {'Name': 'For'}}

# Accessing element using key
print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2']['Name'])

# Operators
a1 = 8
b1 = 3

print(operator.mul(a1, b1))

print(a1/b1)  # GIves decimal values
print(a1//b1)  # Gives floor values (rounded))

# is , is not
a = 10
b = 20
c = a
print(a is not b)  # is and is not O/P is Ture if thery are equal, False if not equal
print(a is c)

# not 'in' operator
x = 24
y = 20
list2 = [10, 20, 30, 40, 50]

if (x not in list2):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list2):
    print("y is present in given list")
else:
    print("y is NOT present in given list")

# Range(start, stop, setp) funcftion
lst3 = list(range(1, 50, 10))
print(lst3)

# print smallest
smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15, 1]:
    if smallest is None or itervar < smallest:
        smallest = itervar

    print("Loop:", itervar, smallest)
print("Smallest:", smallest)
