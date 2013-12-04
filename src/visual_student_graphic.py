# -*- coding: utf-8 -*-

'''
Created on 26/11/2013

@author: douglas
'''

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import time


class VisualStudentGraphic:

    student = None

    def __init__(self, student):

        self.student = student

        ticks = ['01/01/13', '01/02/13', '01/03/13', '01/04/13', '01/05/13',
                 '01/06/13', '01/07/13', '01/08/13', '01/09/13', '01/10/13',
                 '01/11/13', '01/12/13']
        xticks = [dt.datetime.strptime(d, '%d/%m/%y').date() for d in ticks]

        dates = self.student.interactions.keys()
        dates.sort(key=lambda x: time.mktime(time.strptime(x,"%d/%m/%y")))
        
        #Convert date format and add to list
        x = [dt.datetime.strptime(d, '%d/%m/%y').date() for d in dates]
        #Add interactions
        y = [self.student.interactions[d] for d in dates]

        #Format x axis
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%y'))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator())

        #Set date points and interactions points
        plt.plot_date(x, y, 'o-', None, True)

        plt.xticks(xticks, rotation=30)

        plt.ylabel('Number of Interactions')
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
