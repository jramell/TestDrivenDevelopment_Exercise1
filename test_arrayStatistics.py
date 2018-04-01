from unittest import TestCase
from ArrayStatistics import ArrayStatistics

class TestArrayStatistics(TestCase):
    def test_numElems_empty(self):
        self.assertEqual(ArrayStatistics().numElems(""), 0)

    def test_numElems_oneElem(self):
        self.assertEqual(ArrayStatistics().numElems("1"), 1)