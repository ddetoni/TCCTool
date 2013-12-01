# -*- coding: utf-8 -*-

'''
Created on 26/11/2013

@author: douglas
'''

from dataloader import DataLoader
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
from Tkinter import *

if __name__ == '__main__':
    

    data = DataLoader()
    data.load_from_file('../data/name.in')
        
    student_names = data.students.keys()
    
    vsg_frame = Tk()
    vsg_frame.minsize(300, 500)
    
    listbox = Listbox(vsg_frame)
    listbox.pack()
    
    for item in student_names:
        listbox.insert(END, item)

    mainloop()
    
    student = data.students[student_names[0]]
    
    dates = student.interactions.keys()
    x = [dt.datetime.strptime(d,'%m/%d').date() for d in dates]
    y = [student.interactions[d] for d in dates]
    
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    
    plt.plot_date(x, y,'-', None, True)
    plt.ylabel('Interaction number')
    plt.xlabel('Day')
    plt.title(student.name + ' ' + student.last_name + ' - Interaction Graphic')
    plt.show()