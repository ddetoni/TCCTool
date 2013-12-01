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
        
        ticks = ['01/01','02/01','03/01','04/01','05/01','06/01','07/01','08/01','09/01','10/01','11/01','12/01']
        xticks = [dt.datetime.strptime(d,'%m/%d').date() for d in ticks]
        
        dates = self.student.interactions.keys()
        x = [dt.datetime.strptime(d,'%m/%d').date() for d in dates]
        x.sort()
        y = [self.student.interactions[d] for d in dates]
    
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    
        plt.plot_date(x, y, '-', None, True)
        
        plt.xticks(xticks, rotation=80)
        
        plt.ylabel('Interaction number')
        plt.xlabel('Day')
        plt.title(self.student.name + ' ' + self.student.last_name + ' - Interaction Graphic')
        
        plt.show()
    
    def save_fig(self, save_path, save_name):
        
        ticks = ['01/01','02/01','03/01','04/01','05/01','06/01','07/01','08/01','09/01','10/01','11/01','12/01']
        xticks = [dt.datetime.strptime(d,'%m/%d').date() for d in ticks]
        
        dates = self.student.interactions.keys()
        x = [dt.datetime.strptime(d,'%m/%d').date() for d in dates]
        x.sort()
        y = [self.student.interactions[d] for d in dates]
    
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    
        plt.plot_date(x, y, '-', None, True)
        
        plt.xticks(xticks, rotation=80)
        
        plt.ylabel('Interaction number')
        plt.xlabel('Day')
        plt.title(self.student.name + ' ' + self.student.last_name + ' - Interaction Graphic')
        
        final_path = save_path+save_name+".png"
        plt.savefig(final_path, format='png')
        plt.close()
        