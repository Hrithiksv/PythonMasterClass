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
