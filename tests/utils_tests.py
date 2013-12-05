'''
Created on 05/12/2013

@author: douglas
'''
import unittest
from src.utils import convert_day_week, week_interaction, remove_white_space

class Test(unittest.TestCase):


    def testConvertDayWeek(self):
        self.assertEqual(convert_day_week("01/01/2013"), 0)
        self.assertEqual(convert_day_week("07/01/2013"), 1)
        self.assertEqual(convert_day_week("01/05/2013"), 17)
        self.assertEqual(convert_day_week("25/12/2013"), 51)
        self.assertEqual(convert_day_week("31/12/2013"), 52)
    
    def testWeekInteraction(self):
        day_int = {'01/01/2013':51, '06/01/2013':9, '25/12/2013':25,
                   '31/12/2013':300}
        self.assertEqual(week_interaction(day_int), {0:60, 51:25, 52:300})

    def testRemoveWhiteSpaces(self):
        self.assertEqual(remove_white_space(
            '    Douglas       |     Detoni '), u'Douglas|Detoni')
        self.assertEqual(remove_white_space(
            'Douglas|Detoni'), u'Douglas|Detoni')
        self.assertEqual(remove_white_space(
            '    Douglas|     Detoni '), u'Douglas|Detoni')
        self.assertEqual(remove_white_space(
            'Douglas       |Detoni   '), u'Douglas|Detoni')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testConvertDayWeek']
    unittest.main()