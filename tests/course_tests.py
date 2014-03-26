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

        self.stu.interactions = {'01/01/13': 17, '31/12/13': 2,
                                 '05/05/13': 18}

        self.stu1 = Student('Carlos', 'Antonio')
        self.stu2 = Student('Carlos', 'Mario')
        self.course = Course('JS_I')
        self.course.students['Carlos Silva'] = self.stu
        self.course.students['Carlos Antonio'] = self.stu1
        self.course.students['Carlos Mario'] = self.stu2

    def testDelStudent(self):
        self.course.total_interactions_each_week = {'01/01/13': 27, '31/12/13': 5,
                                       '05/05/13': 22, '25/02/13': 20}
        self.course.del_student('Carlos Silva')
        with self.assertRaises(KeyError):
            self.course.students['Carlos Silva']
        self.assertEqual(self.course.total_interactions_each_week,
                         {'01/01/13': 10, '31/12/13': 3,
                          '05/05/13': 4, '25/02/13': 20})

    def testAddToWeekAverage(self):
        self.course.add_to_week_average('1357082141', 1)
        self.course.add_to_week_average('1357082141', 1)
        self.course.add_to_week_average('1388531741', 1)
        self.course.add_to_week_average('1367799341', 1)
        self.course.add_to_week_average('1367799341', 1)
        self.course.add_to_week_average('1357082141', 1)
        self.course.add_to_week_average('1388531741', 1)

        self.assertEqual(self.course.total_interactions_each_week,
                         {'01/01/13': 3, '31/12/13': 2,
                          '05/05/13': 2})

    def testGetAverage(self):
        self.course.add_to_week_average('1357082141', 8)
        self.course.add_to_week_average('1357082141', 32)
        self.course.add_to_week_average('1388531741', 15)
        self.course.add_to_week_average('1367799341', 7)
        self.course.add_to_week_average('1367799341', 60)
        self.course.add_to_week_average('1357082141', 41)
        self.course.add_to_week_average('1388531741', 1)

        self.assertEqual(self.course.get_average_each_week(),
                         {'01/01/13': 27, '31/12/13': 5,
                          '05/05/13': 22})

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
