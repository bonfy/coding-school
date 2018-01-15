# coding: utf-8

from collections.abc import Sequence, Set
import itertools
import bisect


class SortedSet(Sequence, Set):

    def __init__(self, items=None):
        self._items = sorted(set(items)) if items else []

    def __contains__(self, item):
        try:
            self.index(item)
            return True
        except ValueError:
            return False

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        # for item in self._items:
        #     yield item
        return iter(self._items)

    def __getitem__(self, index):
        result = self._items[index]
        return SortedSet(result) if isinstance(index, slice) else result

    def __eq__(self, rhs):
        # 注意 这里必须是 NotImplemented
        if not isinstance(rhs, SortedSet):
            return NotImplemented

        return self._items == rhs._items

    # eq 和 ne 要一起指定，不然有时候会有意想不到的问题
    def __ne__(self, rhs):
        if not isinstance(rhs, SortedSet):
            return NotImplemented
        return self._items != rhs._items

    def __repr__(self):
        return 'SortedSet({})'.format(
            repr(self._items) if self._items else ''
        )

    # 重写 count 加快速度
    def count(self, item):
        return int(item in self)

    def index(self, item):
        index = bisect.bisect_left(self._items, item)
        if (index != len(self._items)) and (self._items[index] == item):
            return index
        raise ValueError('{} not found'.format(repr(item)))

    def __add__(self, rhs):
        return SortedSet(itertools.chain(self._items, rhs))

    def __mul__(self, rhs):
        return self if rhs > 0 else SortedSet()

    def __rmul__(self, lhs):
        return self * lhs

    def issubset(self, iterable):
        return self <= SortedSet(iterable)

    def issuperset(self, iterable):
        return self >= SortedSet(iterable)

    def intersection(self, iterable):
        return self & SortedSet(iterable)

    def union(self, iterable):
        return self | SortedSet(iterable)

    def symmetric_difference(self, iterable):
        return self ^ SortedSet(iterable)

    def difference(self, iterable):
        return self - SortedSet(iterable)
