# -*- coding: utf-8 -*-

'''
Created on 26/11/2013

@author: douglas
'''

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
from Tkinter import *

class VisualStudentGraphic:
    
    student = None
    
    def __init__(self, student):
        
        self.student = student

    def plot(self):
        
        dates = self.student.interactions.keys()
        x = [dt.datetime.strptime(d,'%m/%d').date() for d in dates]
        y = [self.student.interactions[d] for d in dates]
    
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    
        plt.plot_date(x, y,'-', None, True)
        plt.ylabel('Interaction number')
        plt.xlabel('Day')
        plt.title(self.student.name + ' ' + self.student.last_name + ' - Interaction Graphic')
        plt.show()
