'''
Created on 05/12/2013

@author: douglas
'''
import unittest
from src.course import Course
from src.student import Student

class Test(unittest.TestCase):


    def setUp(self):
        self.stu = Student('Douglas', 'Detoni')
        self.course = Course('DD_I')
        self.course.students['Douglas Detoni'] = self.stu
        

    def testDelStudent(self):
        self.course.del_student('Douglas Detoni')
        with self.assertRaises(KeyError):
            self.course.students['Douglas Detoni']
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()