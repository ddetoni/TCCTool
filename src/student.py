# -*- coding: utf-8 -*-

# This class implement a simple student object
import datetime
from utils import week_interaction

class Student:

    name = None
    last_name = None
    interactions = None
    total_interactions = 0
    average_by_week = 0
    result = 0

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        self.interactions = {}

    def set_interation(self, timestamp):

        date = datetime.datetime.fromtimestamp(float(timestamp))

        #Date formated
        date = date.strftime('%d/%m/%y')
        if date in self.interactions:
            count_int = self.interactions[date]
            self.interactions[date] = count_int + 1
            self.total_interactions = self.total_interactions + 1
            return count_int + 1
        else:
            self.interactions[date] = 1
            self.total_interactions = self.total_interactions + 1
            return 1
    
    def set_average_by_week(self):
        week_interactions = week_interaction(self.interactions)
        self.average_by_week = self.total_interactions/len(week_interactions)
