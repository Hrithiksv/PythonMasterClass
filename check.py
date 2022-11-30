def myFun(lst):
    lst = [10, 20, 30]
    print("Inside myfun", id(lst))


x = [1, 2, 3]
print(id(x))
myFun(x)

print(x)
