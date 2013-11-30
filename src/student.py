# -*- coding: utf-8 -*-

# This class implement a simple student object
import datetime

class Student:
    
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        self.interations = {}
        
    def set_interation(self, timestamp):
        
        date = datetime.datetime.fromtimestamp(float(timestamp))
        
        if self.interations.has_key(date.strftime('%m-%d')):
            count_int = self.interations[date.strftime('%m-%d')]
            self.interations[date.strftime('%m-%d')] = count_int + 1
        else:
            self.interations[date.strftime('%m-%d')] = 1
            