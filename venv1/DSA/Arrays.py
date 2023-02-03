import array as arr


def Method1():
    """Declare a array"""
    ary1 = arr.array("i", [1, 3, 4, 5, 5, 6])
    # ary1.byteswap()

    for i in ary1:
        print(i, end=' ')
    print()


# Method1()


def Method2():
    """Reverse a array by swapping elements """
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
    """Reverse array by List slicing"""
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

def SecondLargest(arr: list):
    arr = set(arr)
    if len(arr) <= 1:
        return -1

    # print(ar)
    lst = list(arr)
    lst.sort()
    # print(lst)
    return lst[-2]


# X = [2, 3, 14, 15, 16, 7, 8, 15, 16]
# res = SecondLargest(X)
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
        if temp2 < Y[i] and Y[i] != temp:
            temp2 = Y[i]
    print(temp2)


# SecondLargest2()
def ValueEqualToIndex(arr):
    ary = []
    for index, item in enumerate(arr, 1):
        if index == item:
            ary.append(index)
    return ary


# X = [3, 2, 3, 9, 9, 9]
# val = ValueEqualToIndex(X)

def MoveNonZeros():
    ary = [2, 4, 0, 0, 1, 3, 5, 0]
    nonzero = [x for x in ary if x != 0]
    zero = [y for y in ary if y == 0]
    return nonzero+zero


# VAL = MoveNonZeros()
# print(VAL)
def Swapsubarrofksize(ary, N, K):
    i = 0
    while (i < N):
        if (i+K < N):
            ary[i:i+K] = reversed(ary[i:i+K])
            i += K
        else:
            # reversed function used to reverse any part of the array.
            ary[i:] = reversed(ary[i:])
        # updating index from i to i+k.
            i += K


# ary = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9]
# Swapsubarrofksize(ary, len(ary), 3)
# print(ary)
