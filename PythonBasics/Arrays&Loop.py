import array as arr

# .insert() .apprnd() .remove() .pop(position)
# .index() - gets the index of an array item

a = arr.array('i', [2, 3, 4, 6, 7])
a.insert(0, 1)
a.insert(3, 5)
a.append(9)
for e in (a):
    print(e, end=" ")
print()

b = a.pop()
c = a.pop(2)
print(b, c, end="\n")

# Function to convert decimal number
# to binary using recursion


def DecimalToBinary(num):

    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end='')


# Driver Code
if __name__ == '__main__':

    # decimal value
    dec_val = 24

    # Calling function
    DecimalToBinary(dec_val)
print()
# Using built in function
n1 = 23
print(bin(n1).replace("0b", ""))
