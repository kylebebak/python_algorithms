class ComparableMixin:
    """
    Author: Alex Martelli

    Mixin which allows for rich comparison via the implementation
    of only one method, __lt__(). All other rich comparison methods
    are defined in this mixin in terms of __lt__(). If objects are
    to be compared by reference, the `is` operator must be used,
    i.e. a is b. Objects implementing rich comparison can be sorted!
    """

    def __eq__(self, other):
        return not self < other and not other < self

    def __ne__(self, other):
        return self < other or other < self

    def __gt__(self, other):
        return other < self

    def __ge__(self, other):
        return not self < other

    def __le__(self, other):
        return not other < self


class ComparableHashableMixin:
    """
    Mixin which allows for rich comparison via the implementation
    of only one method, __lt__(). __eq__() and __ne__() are not
    defined, which ensures that instances of a class that inherits
    from this mixin are not only sortable, but also hashable!
    """

    def __gt__(self, other):
        return other < self

    def __ge__(self, other):
        return not self < other

    def __le__(self, other):
        return not other < self
