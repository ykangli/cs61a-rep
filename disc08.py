import math


# 2.1
# Write a function that takes in a a linked list and returns the sum of all its elements.
# You may assume all elements in lnk are integers.
def sum_nums(lnk):
    if lnk == Link.empty:
        return 0
    else:
        return lnk.first + sum_nums(lnk.rest)


class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest


# 2.2
# Write a function that takes in a Python list of linked lists and multiplies them
# element-wise. It should return a new linked list.
# If not all of the Link objects are of equal length, return a linked list whose length is
# that of the shortest linked list given. You may assume the Link objects are shallow
# linked lists, and that lst of lnks contains at least one linked list.
def multiply_lnks(lst_of_lnks):
    result_link = Link.empty
    product = 1
    for lnk in lst_of_lnks:
        if lnk is Link.empty:
            return Link.empty
        product *= lnk.first
    lst_of_lnk_rest = [lnk.rest for lnk in lst_of_lnks]
    return Link(product, multiply_lnks(lst_of_lnk_rest))


# 2.3 递归算法是直接操作原链表lnk
# Write a recursive function flip two that takes as input a linked list lnk
# and mutates lnk so that every pair is flipped.
def flip_two(lnk):
    if lnk is Link.empty or lnk.rest is Link.empty:
        return lnk
    else:
        lnk.first, lnk.rest.first = lnk.rest.first, lnk.first
        flip_two()


# 利用迭代
def flip_two_iter(lnk):
    while lnk is not Link.empty and lnk.rest is not Link.empty:
        lnk.first, lnk.rest.first = lnk.rest.first, lnk.first
        lnk = lnk.rest.rest


# 2.4
# Implement filter link, which takes in a linked list link and a function
# f and returns a generator which yields the values of link for which f returns True.
# Try to implement this both using a while loop and without using any form of
# iteration.
def filter_link(link, f):
    while link is not Link.empty:
        if f(link.first):
            yield link.first
        link = link.rest


class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches


# 3.1
# Define a function make even which takes in a tree t whose values are integers, and
# mutates the tree such that all the odd integers are increased by 1 and all the even
# integers remain the same.
def make_even(t):
    if t.label % 2 != 0:
        t.label += 1
    for branch in t.branches:
        make_even(branch)


# 3.2
# Define a function square tree(t) that squares every value in the non-empty tree
# t. You can assume that every value is a number.
def square_tree(t):
    t.label = t.label ** 2
    for branch in t.branches:
        square_tree(branch)


# 3.3 Define the procedure find paths that, given a Tree t and an entry,
# returns a list of lists containing the nodes along each path from the root of t to
# entry. You may return the paths in any order.
def find_paths(t, entry):
    paths = []
    if t.label == entry:
        return paths.append([t.label])
    for branch in t.branches:
        for path in find_paths(branch, entry):
            paths.append([t.label] + path)  # 分支路径+ t.label
    return paths


# 3.4 Write a function that combines the values of two trees t1 and t2 together with the
# combiner function. Assume that t1 and t2 have identical structure. This function
# should return a new tree
def combine_tree(t1, t2, combiner):
    combined = [combine_tree(b1, b2, combiner) for b1, b2
                in zip(t1.branches, t2.branches)]
    return Tree(combiner(t1.label, t2.label), combined)


# a = [1, 2, 3]
# b = [4, 5, 6]
#
# for b1, b2 in zip(a, b):
#     print(b1, b2)
#
# # 结果：
# # 1 4
# # 2 5
# # 3 6


# # 3.5 Implement the alt tree map function that, given a function and a Tree, applies the
# function to all of the data at every other level of the tree, starting at the root.
def alt_tree_map(t, map_fn):
    def helper(t, depth):
        if depth % 2 == 0:
            label = map_fn(t.label)
        else:
            label = t.label
            branches = [helper(b, depth + 1) for b in t.branches]
            return Tree(label, branches)

    return helper(t, 0)
