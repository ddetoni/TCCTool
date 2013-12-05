'''
Created on 05/12/2013

@author: douglas
'''
import unittest
from src.course import Course
from src.student import Student

class Test(unittest.TestCase):


    def setUp(self):
        self.stu = Student('João', 'Silva')
        self.course = Course('JS_I')
        self.course.students['João Silva'] = self.stu
        

    def testDelStudent(self):
        self.course.del_student('João Silva')
        with self.assertRaises(KeyError):
            self.course.students['João Silva']
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()