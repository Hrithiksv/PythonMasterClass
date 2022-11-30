import math as M
import time


def is_prime(n):
    if n <= 1:
        return False
    if n % 2 == 0:
        return n == 2

    max_div = M.floor(M.sqrt(n))
    for i in range(3, 1+max_div, 2):
        if n % i == 0:
            return False
    return True


t0 = time.time()
count = 0
nw_lst = []
for n in range(1, 100):
    x = is_prime(n)
    if x:
        nw_lst.append(n)
    count += x

print("total trime numbers are: ", count)
t1 = time.time()
print(nw_lst)
print(f"total time taken: {t1-t0}")
