ip = list(map(int, input("enter list :").split(' ')))

print(ip)
nw_lst = []

for num in ip:
    sum = 0
    for ch in str(num):
        sum += int(ch)
    nw_lst.append(sum)

print(nw_lst)

#dig = 0
# for i in ip:
#   dig = dig+int(i)
# print(dig)


def fun1(a: list, b: list) -> int:
    # if len(a) > len(b):
    #    diff = set(a)-set(b)
    # else:
    #diff = set(b)-set(a)
    diff = set(a)-set(b) if len(a) > len(b) else set(b)-set(a)
    print(diff.pop())


s1 = [14, 27, 1, 4, 2, 50, 3, 1]
s2 = [2, 4, -4, 3, 1, 1, 14, 27, 50]
fun1(s1, s2)
