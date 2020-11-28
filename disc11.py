class Pair:
"""Represents the built-in pair data structure in Scheme."""
    def __init__(self, first, rest):
        self.first = first
        if not scheme_valid_cdrp(rest):
        raise SchemeError("cdr can only be a pair, nil, or a promise but was {}".format(rest))
        self.rest = rest

    def map(self, fn):
        """Maps fn to every element in a list, returning a new
        Pair.
        >>> Pair(1, Pair(2, Pair(3, nil))).map(lambda x: x * x)
        Pair(1, Pair(4, Pair(9, nil)))
        """
        assert isinstance(self.rest, Pair) or self.rest is nil, \
        "rest element in pair must be another pair or nil"
        return Pair(fn(self.first), self.rest.map(fn))

    def __repr__(self):
        return 'Pair({}, {})'.format(self.first, self.rest)

class nil:
    """Represents the special empty pair nil in Scheme."""
    def map(self, fn):
        return nil
    def __getitem__(self, i):
        raise IndexError('Index out of range')
    def __repr__(self):
        return 'nil'
        nil = nil() # this hides the nil class *forever*

1.1 Write out the Calculator expression with proper syntax that corresponds to the
following Pair constructor calls. Also, draw out a box and pointer diagram corresponding to each input.

>>> Pair('+', Pair(1, Pair(2, Pair(3, Pair(4, nil)))))
(+ 1 2 3 4)

>>> Pair('+', Pair(1, Pair(Pair('*', Pair(2, Pair(3, nil))), nil)))
(+ 1 (* 2 3))

1.2 Answer the following questions about a Pair instance representing the Calculator
expression (+ (- 2 4) 6 8).

i. Write out the Python expression that returns a Pair representing the given
expression, and draw a box and pointer diagram corresponding to it.

Pair('+', Pair(Pair('-', Pair(2, Pair(4, nil))), Pair(6, Pair(8, nil))))

ii. What is the operator of the call expression? If the Pair you constructed in the
previous part was bound to the name p, how would you retrieve the operator?

p.first

iii. What are the operands of the call expression? If the Pair you constructed in
Part (i) was bound to the name p, how would you retrieve a list containing all
of the operands? How would you retrieve only the first operand?

p.rest to get a list containing all the operands. p.rest.first to get the first
operand by itself.

def calc_eval(exp):
    """Evaluates a Calculator expression represented as a Pair."""
    if isinstance(exp, Pair): # Call expressions
        fn = calc_eval(exp.first)
        # 对Pair()的实例p.rest进行递归调用，判断p.rest是哪一种类型，call expression、names还是numbers
        args = list(exp.rest.map(calc_eval)) 
        return calc_apply(fn, args)
    elif exp in OPERATORS: # Names
        return OPERATORS[exp]
    else: # Numbers
        return exp

def calc_apply(fn, args):
    """Applies a Calculator operation to a list of numbers."""
    # args为列表，可计算在fn函数作用下的列表的值
    return fn(args)

example：
>>> import math
>>> sum([1,2,3])
6

2.1 Suppose we want to add handling for comparison operators >, <, and = as well as
and expressions to our Calculator interpreter. These should work the same way
they do in Scheme.

calc> (and (= 1 1) 3)
3
calc> (and (+ 1 0) (< 1 0) (/ 1 0))
#f

i. Are we able to handle expressions containing the comparison operators (such
as <, >, or =) with the existing implementation of calc eval? Why or why not?

将'>','<','='添加到operator字典中就可以了

ii. Are we able to handle and expressions with the existing implementation of
calc eval? Why or why not?

and 操作符有'短路'效应，后面的operands可能不会去处理，因此不能简单的将 and 操作符按照添加到
operator词典

def calc_eval(exp):
    if isinstance(exp, Pair):
        if exp.first == 'and': # and expressions
            return eval_and(exp.rest)
    else: # Call expressions
        return calc_apply(calc_eval(exp.first), list(exp.rest.map(calc_eval)))
    elif exp in OPERATORS: # Names
        return OPERATORS[exp]
    else: # Numbers
        return exp

def eval_and(operands):
    curr, val = operands, True
    while curr is not nil:
        val = calc_eval(curr.first)
        # 一直往后走，当遇到Flase时就返回，后面就不会再判断，这样就能达到 add 短路的效果
        if val is False:
            return False
        curr = curr.first
    return val
    


