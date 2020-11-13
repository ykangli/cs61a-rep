# 1.1
def memory(n):
    def f(g):
        nonlocal n
        return g(n)
    return f

# 2.2
def mystery(p, q):
    p[1].extend(q)
    q.append(p[1:])
    
p = [2, 3]
q = [4, [p]]
mystery(q, p)

# 2.3
def group_by(s, fn):
    grouped = {}
    for i in s:
        key = fn(i)
        if key in grouped:
            grouped[key].append(i)
        else:
            grouped[key] = i
    return grouped

# 2.4
def add_this_many(x, el, s):
    num = 0
    for i in s:
        if i == x:
            num += 1
    while(num > 0):
        s.append(el)
        num -= 1
    return s

# 3.1

'''
凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象

>>> s = [[1, 2]]
>>> i = iter(s)
>>> j = iter(next(i))
>>> next(j)
    1
>>> s.append(3)
>>> next(i)   第三行j = iter(next(i))中的next(i)已经将[1, 2]迭代出去
    3    
>>> next(j)
    2
>>> next(i)
    StopIteration

'''
# 4.1
def fiter(iterable, fn):
    for elem in iterable:
        if fn(elem):
            yield elem
