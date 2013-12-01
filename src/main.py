# -*- coding: utf-8 -*-

'''
Created on 26/11/2013

@author: douglas
'''

from dataloader import DataLoader
from visual_student_graphic import VisualStudentGraphic

if __name__ == '__main__':
    
    #data = DataLoader().load_from_file('../data/logs_course_37.in')
    #data = DataLoader().load_from_file('../data/name.in')
    data = DataLoader().load_from_serial('../data/name.in.srz')
    #data = DataLoader().load_from_serial('../data/logs_course_37.in.srz')
    
    student = data.students[u'Mercedes Nelly Gardey de Sánchez']
    
    vsg = VisualStudentGraphic(student)
    vsg.plot()