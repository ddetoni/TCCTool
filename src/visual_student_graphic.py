# -*- coding: utf-8 -*-

'''
Created on 26/11/2013

@author: douglas
'''

import matplotlib.pyplot as plt
#import matplotlib.dates as mdates
import datetime as dt
import time
from src.utils import *


class VisualStudentGraphic:

    student = None

    def __init__(self, student):

        self.student = student
        #52 weeks -> year
        ticks = range(0, 53, 4)

        week_interactions = week_interaction(self.student.interactions)
        
        weeks = week_interactions.keys()
        weeks.sort()
        
        x = weeks
        #Add week interactions
        y = [week_interactions[w] for w in weeks]

        #Set week points and interactions points
        plt.plot(x, y, 'o-', None, True)

        plt.xticks(ticks)

        plt.ylabel('Number of Interactions')
        plt.xlabel('Week')
        plt.title(self.student.name + ' ' + self.student.last_name +
                  ' - Interaction Graphic')

    #Plot the graphic
    def plot(self):
        plt.show()

    # Save the graphic with format PNG
    def save_fig(self, save_path, save_name):
        final_path = save_path+save_name+".png"
        plt.savefig(final_path, format='png')
        plt.close()
