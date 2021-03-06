from unittest import TestCase
from ArrayStatistics import ArrayStatistics

class TestArrayStatistics(TestCase):
    def test_numElems_empty(self):
        self.assertEqual(ArrayStatistics().numElems(""), 0)

    def test_numElems_oneElem(self):
        self.assertEqual(ArrayStatistics().numElems("1"), 1)

    def test_numElems_twoElems(self):
        self.assertEqual(ArrayStatistics().numElems("1,2"), 2)

    def test_numElems_nElems(self):
        self.assertEqual(ArrayStatistics().numElems("1,2,3,4,10,14"), 6)

    def test_numElemsIter2_empty(self):
        self.assertEqual(ArrayStatistics().numElemsIter2(""), [0, -1])

    def test_numElemsIter2_oneElem(self):
        self.assertEqual(ArrayStatistics().numElemsIter2("1"), [1, 1])

    def test_numElemsIter2_twoElems(self):
        self.assertEqual(ArrayStatistics().numElemsIter2("0,2"), [2, 0])

    def test_numElemsIter2_nElems(self):
        self.assertEqual(ArrayStatistics().numElemsIter2("1,2,3,4,10,14"), [6, 1]);

    def test_numElemsIter3_empty(self):
        self.assertEqual(ArrayStatistics().numElemsIter3(""), [0, -1, -1])

    def test_numElemsIter3_oneElem(self):
        self.assertEqual(ArrayStatistics().numElemsIter3("1"), [1, 1, 1])

    def test_numElemsIter3_twoElem(self):
        self.assertEqual(ArrayStatistics().numElemsIter3("1,2"), [2, 1, 2])

    def test_numElemsIter3_nElems(self):
        self.assertEqual(ArrayStatistics().numElemsIter3("1,2,3,4,10,14"), [6, 1, 14]);

    def test_numElemsIter4_empty(self):
        self.assertEqual(ArrayStatistics().numElemsIter4(""), [0, -1, -1, -1])

    def test_numElemsIter4_oneElem(self):
        self.assertEqual(ArrayStatistics().numElemsIter4("1"), [1, 1, 1, 1])

    def test_numElemsIter4_twoElems(self):
        self.assertEqual(ArrayStatistics().numElemsIter4("1,2"), [2, 1, 2, 1.5])

    def test_numElemsIter4_nElems(self):
        self.assertEqual(ArrayStatistics().numElemsIter4("1,2,3,4,10,16"), [6, 1, 16, 6.0])