class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest


class Tree:
    def __init__(self, lable, brances=[]):
        for b in brances:
            assert isinstance(b, Tree)
            self.lable = lable
            self.brances = list(brances)

    def is_leaf(self):
        return not self.brances
