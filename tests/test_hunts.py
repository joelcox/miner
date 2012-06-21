import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import unittest

import miner.utils
import miner.classification


class TestHunts(unittest.TestCase):

    def test_records_in_single_class(self):
        records = [{'home_owner': True, 'employed': True, 'defaulted': False},
                   {'home_owner': True, 'employed': False, 'defaulted': False}]
        tree = miner.classification.Hunts('defaulted', records)
        self.assertEquals(tree.records_in_single_class(records), True)

        records = [{'home_owner': True, 'employed': True, 'defaulted': False},
                   {'home_owner': True, 'employed': False, 'defaulted': True}]
        tree = miner.classification.Hunts('defaulted', records)
        self.assertEquals(tree.records_in_single_class(records), False)
