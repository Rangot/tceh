import sys
import pprint

'''
import random


def random_int():
    s = 0
    while True:
        yield s
        s = random.randint(0, 100)


n = random_int()
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))



def ranging(lst1, lst2):
    lst3 = []
    lst3.append(lst1)
    while True:
        lst1 += 1
        lst3.append(lst1)
        if lst1 == lst2-1:
            break
    yield lst3


x = ranging(50, 100)
print(next(x))
print(sys.getsizeof(x))


def mapping(lst):
    lst_new = []
    for i in lst:
        x = i*i
        lst_new.append(x)
    yield lst_new


nums = [1, 2, 3, 5, 7, 9, 103]
y = mapping(nums)
print(next(y))
print(sys.getsizeof(y))


def enumerating(lst):
    idx = 0
    lst_new = []
    for i in lst:
        lst_new.append(idx)
        idx += 1
        lst_new.append(i)
    lst_ret = []
    while lst_new:
        lst_ret.append(lst_new[0:2])
        del lst_new[0:2]
    return printing(lst_ret)


def printing(lst_ret):
    for j in lst_ret:
        print(str(j).strip(',').strip('[').strip(']'))
    yield lst_ret


s = [1, 2, 7, 19]
z = enumerating(s)
print(next(z))
print(sys.getsizeof(z))
'''


def zipping(*args):
    num = len(args)  # 3
    lst = []
    for i in range(0, num):
        lst.append(tuple())
    print(lst)
    zipping_2(args, lst)


def zipping_2(*args, lst):
    for i in args:
        for j in i:
            k = 0
            lst[k] += (j, )
            k += 1

    yield z


w = 'abc'
t = (10, 20, 30)
u = (-5, -10, -15)

z = zipping(w, t, u)
print(next(z))
