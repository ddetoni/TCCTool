# -*- coding: utf-8 -*-

# This class implement a simple professor object
import datetime


class Professor:

    name = None
    last_name = None
    interactions = None

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        self.interactions = {}
        
    def set_interation(self, timestamp):

        date = datetime.datetime.fromtimestamp(float(timestamp))

        #Interactions limited at 2013 year.
        if date.year != 2013:
            return None

        #Date formated
        date = date.strftime('%d/%m/%y')
        if date in self.interactions:
            count_int = self.interactions[date]
            self.interactions[date] = count_int + 1
            return count_int + 1
        else:
            self.interactions[date] = 1
            return 1
