# -*- coding: utf-8 -*-

'''
Created on 26/11/2013

@author: douglas
'''

from dataloader import DataLoader
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

if __name__ == '__main__':
    
    #data = DataLoader().load_from_file('../data/logs_course_37.in')
    #data = DataLoader().load_from_file('../data/name.in')
    data = DataLoader()
    data.load_from_file('../data/name.in')
    #data = DataLoader().load_from_serial('../data/logs_course_37.in.srz')
    
    student_names = data.students.keys()
    
    student = data.students[student_names[1]]
    
    dates = student.interactions.keys()
    x = [dt.datetime.strptime(d,'%m/%d').date() for d in dates]
    y = [student.interactions[d] for d in dates]
    
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    
    plt.plot_date(x, y,'-', None, True)
    plt.ylabel('Interaction number')
    plt.xlabel('Day')
    plt.title(student.name + ' - Interaction Graphic')
    plt.show()