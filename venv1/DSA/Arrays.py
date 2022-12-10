import array as arr


def Method1():
    """Declare a string"""
    ary1 = arr.array("i", [1, 3, 4, 5, 5, 6])
    # ary1.byteswap()

    for i in ary1:
        print(i, end=' ')
    print()


# Method1()


def Method2():
    """Reverse a string by swapping elements """
    ary1 = arr.array("i", [1, 3, 4, 5, 5, 6])
    start = 0
    end = len(ary1)-1
    while start < end:
        ary1[start], ary1[end] = ary1[end], ary1[start]
        start += 1
        end -= 1
    print(ary1)


# Method2()


def Method3():
    """Reverse string by List slicing"""
    ary1 = arr.array("i", [1, 3, 4, 5, 5])
    print(type(ary1))
    A = list(ary1)
    print(A)
    print(A[::-1])

# Method3()


def LeftRotate(x):
    arr = [8, 22, 256, 53, 47, 4, 6, 98, 45]
    d = x
    # print(arr[:2])
    if d < len(arr):
        new_arr = arr[d:] + arr[0:d]
        arr = new_arr
    print(arr)


# LeftRotate(8)

def SecondLargest(ar: list):
    ar = set(ar)
    lst = list(ar)
    return lst[-3]


X = [2, 3, 14, 15, 16, 7, 8, 15, 16]
#res = SecondLargest(X)
# print(res)


def SecondLargest2():
    Y = [2, 3, 14, 15, 16, 7, 8, 15, 16]
    temp = Y[0]
    for i in range(1, len(Y)):
        if temp < Y[i]:
            temp = Y[i]
    print(temp)
    temp2 = 0
    for i in range(len(Y)):
        if temp2 < Y[i] and Y[i] != temp:  # IMP Y[i]!= temp
            temp2 = Y[i]
    print(temp2)


# SecondLargest2()
