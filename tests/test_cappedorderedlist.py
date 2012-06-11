import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import unittest

import miner.utils


class TestCappedOrderedList(unittest.TestCase):

    def setUp(self):
        self.list = miner.utils.CappedOrderedList(3)
        self.list.add(2)
        self.list.add(1)
        self.list.add(3)

    def test_order(self):
        self.assertEqual(self.list[0], 1)
        self.assertEqual(self.list[1], 2)
        self.assertEqual(self.list[2], 3)

    def test_max_length(self):
        self.list.add(2)
        self.assertEqual(len(self.list), 3)
        self.assertEqual(self.list[0], 1)
        self.assertEqual(self.list[1], 2)
        self.assertEqual(self.list[2], 2)

    def test_order_tuples(self):
        self.list.add((1, 'Meta'))
        self.assertEqual(self.list[0], (1, 'Meta'))
