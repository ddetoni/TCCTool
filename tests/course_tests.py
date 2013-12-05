'''
Created on 05/12/2013

@author: douglas
'''
import unittest
from src.course import Course
from src.student import Student

class Test(unittest.TestCase):


    def setUp(self):
        self.stu = Student('Carlos', u'Silva')
        self.course = Course('JS_I')
        self.course.students['Carlos Silva'] = self.stu
        

    def testDelStudent(self):
        self.course.del_student('Carlos Silva')
        with self.assertRaises(KeyError):
            self.course.students['Carlos Silva']
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()