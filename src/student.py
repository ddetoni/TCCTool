# -*- coding: utf-8 -*-

# This class implement a simple student object
import datetime


class Student:

    name = None
    last_name = None
    interactions = None

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        self.interactions = {}

    def set_interation(self, timestamp):

        date = datetime.datetime.fromtimestamp(float(timestamp))
        
        #Date formated
        date = date.strftime('%m/%d')
        if date in self.interactions:
            count_int = self.interactions[date]
            self.interactions[date] = count_int + 1
        else:
            self.interactions[date] = 1
