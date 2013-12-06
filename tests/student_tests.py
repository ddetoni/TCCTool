'''
Created on 05/12/2013

@author: douglas
'''
import unittest
from src.student import Student


class Test(unittest.TestCase):

    def setUp(self):
        self.stud = Student('Douglas', 'Detoni')

    def testSetInteraction(self):
        self.assertEqual(self.stud.set_interation('1357042332'), 1)
        self.assertEqual(self.stud.set_interation('1357024805'), 2)

        self.assertEqual(self.stud.set_interation('1388484672'), 1)
        self.assertEqual(self.stud.set_interation('1388509872'), 2)

        self.assertEqual(self.stud.set_interation('1341162672'), None)
        self.assertEqual(self.stud.set_interation('1392484272'), None)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
