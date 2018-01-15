import unittest

from sorted_set import SortedSet
from collections.abc import (Container, Sized, Iterable, Sequence, Set)


class TestConstruction(unittest.TestCase):

    def test_empty(self):
        s = SortedSet([])

    def test_from_sequence(self):
        s = SortedSet([7, 8, 3, 1])

    def test_with_duplicates(self):
        s = SortedSet([8, 8, 8])

    def test_from_iterable(self):
        def gen6823():
            yield 6
            yield 8
            yield 2
            yield 3
        g = gen6823()
        s = sorted(g)

    def test_default_empty(self):
        s = SortedSet()


class TestContainerProtocol(unittest.TestCase):

    def setUp(self):
        self.s = SortedSet([6, 7, 3, 9])

    def test_positive_contained(self):
        self.assertTrue(6 in self.s)

    def test_negative_contained(self):
        self.assertFalse(2 in self.s)

    def test_positive_not_contained(self):
        self.assertTrue(5 not in self.s)

    def test_negative_not_contained(self):
        self.assertFalse(9 not in self.s)

    def test_protocol(self):
        self.assertTrue(issubclass(SortedSet, Container))


class TestSizedProtocol(unittest.TestCase):

    def test_empty(self):
        s = SortedSet()
        self.assertEqual(len(s), 0)

    def test_one(self):
        s = SortedSet([8])
        self.assertEqual(len(s), 1)

    def test_ten(self):
        s = SortedSet(range(10))
        self.assertEqual(len(s), 10)

    def test_with_duplicates(self):
        s = SortedSet([8, 8, 8])
        self.assertEqual(len(s), 1)

    def test_protocol(self):
        self.assertTrue(issubclass(SortedSet, Sized))


class TestIterableProtocol(unittest.TestCase):

    def setUp(self):
        self.s = SortedSet([6, 3, 3, 7, 9])

    def test_iter(self):
        i = iter(self.s)
        self.assertEqual(next(i), 3)
        self.assertEqual(next(i), 6)
        self.assertEqual(next(i), 7)
        self.assertEqual(next(i), 9)
        self.assertRaises(StopIteration, lambda: next(i))

    def test_loop(self):
        index = 0
        expected = [3, 6, 7, 9]
        for item in self.s:
            self.assertEqual(item, expected[index])
            index += 1

    def test_protocol(self):
        self.assertTrue(issubclass(SortedSet, Iterable))


class TestSequenceProtocol(unittest.TestCase):

    def setUp(self):
        self.s = SortedSet([1, 3, 6, 9, 12])

    def test_index_zero(self):
        self.assertEqual(self.s[0], 1)

    def test_index_end(self):
        self.assertEqual(self.s[3], 9)

    def test_index_beyond_end(self):
        self.assertRaises(IndexError, lambda: self.s[5])

    def test_index_minus_one(self):
        self.assertEqual(self.s[-1], 12)

    def test_index_minus_five(self):
        self.assertEqual(self.s[-5], 1)

    def test_index_before_beginning(self):
        self.assertRaises(IndexError, lambda: self.s[-6])

    def test_slice_from_start(self):
        self.assertEqual(self.s[:3], SortedSet([1, 3, 6]))

    def test_slice_to_end(self):
        self.assertEqual(self.s[3:], SortedSet([9, 12]))

    def test_slice_empty(self):
        self.assertEqual(self.s[10:], SortedSet())

    def test_slice_arbitary(self):
        self.assertEqual(self.s[2:4], SortedSet([6, 9]))

    def test_slice_full(self):
        self.assertEqual(self.s[:], self.s)

    def test_reversed(self):
        s = SortedSet([1, 3, 5, 7])
        r = reversed(s)
        self.assertEqual(next(r), 7)
        self.assertEqual(next(r), 5)
        self.assertEqual(next(r), 3)
        self.assertEqual(next(r), 1)
        with self.assertRaises(StopIteration):
            next(r)

    def test_index_positive(self):
        s = SortedSet([1, 3, 5, 7])
        self.assertEqual(s.index(5), 2)

    def test_index_negative(self):
        s = SortedSet([1, 3, 5, 7])
        with self.assertRaises(ValueError):
            s.index(9)

    def test_count_zero(self):
        s = SortedSet([1, 3, 5])
        self.assertEqual(s.count(11), 0)

    def test_count_one(self):
        s = SortedSet([1, 3, 5])
        self.assertEqual(s.count(1), 1)

    def test_protocol(self):
        self.assertTrue(issubclass(SortedSet, Sequence))

    def test_concatenate_disjoint(self):
        s = SortedSet([1, 2, 3])
        t = SortedSet([7, 8, 9])
        self.assertEqual(s + t, SortedSet([1, 2, 3, 7, 8, 9]))

    def test_concatenate_equal(self):
        s = SortedSet([1, 2, 3])
        self.assertEqual(s + s, s)

    def test_concatenate_intersecting(self):
        s = SortedSet([5, 6, 7])
        t = SortedSet([7, 8, 9])
        self.assertEqual(s + t, SortedSet([5, 6, 7, 8, 9]))

    def test_repetition_zero(self):
        s = SortedSet([1, 2, 3])
        self.assertEqual(0 * s, SortedSet())

    def test_repetition_non_zero(self):
        s = SortedSet([1, 2, 3])
        self.assertEqual(s * 3, s)


class TestReprProtocol(unittest.TestCase):

    def test_equal_empty(self):
        s = SortedSet()
        self.assertEqual(repr(s), 'SortedSet()')

    def test_sorted_some(self):
        s = SortedSet([25, 10])
        self.assertEqual(repr(s), 'SortedSet([10, 25])')


class TestEqualityProtocol(unittest.TestCase):

    def test_positive_equal(self):
        self.assertTrue(SortedSet([3, 6, 9]) == SortedSet([9, 6, 3]))

    def test_negative_equal(self):
        self.assertFalse(SortedSet([3, 6, 9]) == SortedSet([1, 2, 3]))

    def test_type_mismatch(self):
        self.assertFalse(SortedSet([3, 6, 9]) == [3, 6, 9])

    def test_identical(self):
        s = SortedSet([3, 6, 9])
        self.assertTrue(s == s)


class TestInequalityProtocol(unittest.TestCase):

    def test_negative_unequal(self):
        self.assertFalse(SortedSet([3, 6, 9]) != SortedSet([9, 6, 3]))

    def test_positive_unequal(self):
        self.assertTrue(SortedSet([3, 6, 9]) != SortedSet([1, 2, 3]))

    def test_type_mismatch(self):
        self.assertTrue(SortedSet([3, 6, 9]) != [3, 6, 9])

    def test_identical(self):
        s = SortedSet([3, 6, 9])
        self.assertFalse(s != s)


class TestRelationalSetProtocol(unittest.TestCase):

    def test_lt_positive(self):
        s = SortedSet({1, 2})
        t = SortedSet({1, 2, 3})
        self.assertTrue(s < t)

    def test_lt_negative(self):
        s = SortedSet({1, 2, 3})
        t = SortedSet({1, 2, 3})
        self.assertFalse(s < t)

    def test_le_lt_positive(self):
        s = SortedSet({1, 2})
        t = SortedSet({1, 2, 3})
        self.assertTrue(s <= t)

    def test_le_eq_positive(self):
        s = SortedSet({1, 2, 3})
        t = SortedSet({1, 2, 3})
        self.assertTrue(s <= t)

    def test_le_negative(self):
        s = SortedSet({1, 2, 3})
        t = SortedSet({1, 2})
        self.assertFalse(s <= t)

    def test_gt_positive(self):
        s = SortedSet({1, 2, 3})
        t = SortedSet({1, 2})
        self.assertTrue(s > t)

    def test_gt_negative(self):
        s = SortedSet({1, 2})
        t = SortedSet({1, 2, 3})
        self.assertFalse(s > t)

    def test_ge_gt_positive(self):
        s = SortedSet({1, 2, 3})
        t = SortedSet({1, 2})
        self.assertTrue(s > t)

    def test_ge_eq_positive(self):
        s = SortedSet({1, 2, 3})
        t = SortedSet({1, 2, 3})
        self.assertTrue(s >= t)

    def test_ge_negative(self):
        s = SortedSet({1, 2})
        t = SortedSet({1, 2, 3})
        self.assertFalse(s >= t)


class TestSetRelationalMethods(unittest.TestCase):

    def test_issubset_proper_positive(self):
        s = SortedSet({1, 2})
        t = [1, 2, 3]
        self.assertTrue(s.issubset(t))

    def test_issubset_positive(self):
        s = SortedSet({1, 2, 3})
        t = [1, 2, 3]
        self.assertTrue(s.issubset(t))

    def test_issubset_negative(self):
        s = SortedSet({1, 2, 3})
        t = [1, 2]
        self.assertFalse(s.issubset(t))

    def test_issuperset_proper_positive(self):
        s = SortedSet({1, 2, 3})
        t = [1, 2]
        self.assertTrue(s.issuperset(t))

    def test_issuperset_positive(self):
        s = SortedSet({1, 2, 3})
        t = [1, 2, 3]
        self.assertTrue(s.issuperset(t))

    def test_issuperset_negative(self):
        s = SortedSet({1, 2})
        t = [1, 2, 3]
        self.assertFalse(s.issuperset(t))


class TestOperationsSetProtocol(unittest.TestCase):

    def test_intersection(self):
        s = SortedSet({1, 2, 3})
        t = SortedSet({2, 3, 5})
        self.assertEqual(s & t, SortedSet({2, 3}))

    def test_union(self):
        s = SortedSet({1, 2, 3})
        t = SortedSet({2, 3, 5})
        self.assertEqual(s | t, SortedSet({1, 2, 3, 5}))

    def test_symmetric_difference(self):
        s = SortedSet({1, 2, 3})
        t = SortedSet({2, 3, 5})
        self.assertEqual(s ^ t, SortedSet({1, 5}))

    def test_difference(self):
        s = SortedSet({1, 2, 3})
        t = SortedSet({2, 3, 5})
        self.assertEqual(s - t, SortedSet({1}))


class TestSetOperationsMethods(unittest.TestCase):

    def test_intersection(self):
        s = SortedSet({1, 2, 3})
        t = [2, 3, 5]
        self.assertEqual(s.intersection(t), SortedSet({2, 3}))

    def test_union(self):
        s = SortedSet({1, 2, 3})
        t = [2, 3, 5]
        self.assertEqual(s.union(t), SortedSet({1, 2, 3, 5}))

    def test_symmetric_difference(self):
        s = SortedSet({1, 2, 3})
        t = [2, 3, 5]
        self.assertEqual(s.symmetric_difference(t), SortedSet({1, 5}))

    def test_difference(self):
        s = SortedSet({1, 2, 3})
        t = [2, 3, 5]
        self.assertEqual(s.difference(t), SortedSet({1}))

    def test_isdisjoint_positive(self):
        s = SortedSet({1, 2, 3})
        t = [5, 6, 7]
        self.assertTrue(s.isdisjoint(t))

    def test_isdisjoint_negative(self):
        s = SortedSet({1, 2, 3})
        t = [3, 5, 7]
        self.assertFalse(s.isdisjoint(t))


class TestSetProtocol(unittest.TestCase):

    def test_protocol(self):
        self.assertTrue(issubclass(SortedSet, Set))


if __name__ == '__main__':
    unittest.main()
