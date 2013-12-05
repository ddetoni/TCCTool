'''
Created on 05/12/2013

@author: douglas
'''
import unittest
from src.course import Course
from src.student import Student

class Test(unittest.TestCase):


    def setUp(self):
        self.stu = Student('Carlos', 'Silva')
        self.stu1 = Student('Carlos', 'Antonio')
        self.stu2 = Student('Carlos', 'Mario')
        self.course = Course('JS_I')
        self.course.students['Carlos Silva'] = self.stu
        self.course.students['Carlos Antonio'] = self.stu1
        self.course.students['Carlos Mario'] = self.stu2
        

    def testDelStudent(self):
        self.course.del_student('Carlos Silva')
        with self.assertRaises(KeyError):
            self.course.students['Carlos Silva']
    
    def testAddToAverage(self):
        self.course.add_to_average('01/01/2013', 1)
        self.course.add_to_average('01/01/2013', 1)
        self.course.add_to_average('31/12/2013', 1)
        self.course.add_to_average('05/05/2013', 1)
        self.course.add_to_average('05/05/2013', 1)
        self.course.add_to_average('01/01/2013', 1)
        self.course.add_to_average('31/12/2013', 1)
        
        self.assertEqual(self.course.overall_average, 
                         {'01/01/2013':3, '31/12/2013':2,
                          '05/05/2013': 2})
        
    def testGetAverage(self):
        self.course.add_to_average('01/01/2013', 8)
        self.course.add_to_average('01/01/2013', 32)
        self.course.add_to_average('31/12/2013', 15)
        self.course.add_to_average('05/05/2013', 7)
        self.course.add_to_average('05/05/2013', 60)
        self.course.add_to_average('01/01/2013', 41)
        self.course.add_to_average('31/12/2013', 1)
        
        self.assertEqual(self.course.get_average(),
                         {'01/01/2013':27, '31/12/2013':5,
                          '05/05/2013': 22})

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()