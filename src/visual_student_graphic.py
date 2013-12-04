# -*- coding: utf-8 -*-

'''
Created on 26/11/2013

@author: douglas
'''

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt


class VisualStudentGraphic:

    student = None

    def __init__(self, student):

        self.student = student

        ticks = ['01/01', '02/01', '03/01', '04/01', '05/01', '06/01',
                 '07/01', '08/01', '09/01', '10/01', '11/01', '12/01']
        xticks = [dt.datetime.strptime(d, '%m/%d').date() for d in ticks]

        dates = self.student.interactions.keys()
        dates.sort()
        
        #Convert date format and add to list
        x = [dt.datetime.strptime(d, '%m/%d').date() for d in dates]
        #x.sort()
        y = [self.student.interactions[d] for d in dates]

        #Format x axis
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator())

        #Set date points and interactions points
        plt.plot_date(x, y, '-', None, True)

        plt.xticks(xticks, rotation=80)

        plt.ylabel('Interaction number')
        plt.xlabel('Day')
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
