import unittest
import sys,os

sys.path.append(os.getcwd()) #current working directory
from main import *



class TestGenRandom(unittest.TestCase):
    def test_gen_random1(self):
        self.assertEqual(list(set(gen_random(20,2,4))),[2,3,4])

class TestSquaredCont(unittest.TestCase):
    def test_squared_cont(self):
        self.assertEqual(squared_cont(2,4),[6,12,20])


class TestSort(unittest.TestCase):
    def test_sort(self):
        self.assertEqual(sort([1,2,56,-20]),[1,2,-20,56])



if __name__=='__main__':
    unittest.main()