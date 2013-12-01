# -*- coding: utf-8 -*-

'''
Created on 26/11/2013

@author: douglas
'''

from dataloader import DataLoader
from visual_student_graphic import VisualStudentGraphic

if __name__ == '__main__':
    
    data = DataLoader().load_from_file('../data/logs_course_37.in')
    #data = DataLoader().load_from_file('../data/name.in')
    #data = DataLoader().load_from_serial('../data/name.in.srz')
    #data = DataLoader().load_from_serial('../data/logs_course_37.in.srz')
    '''
    count = 0
    fig_name = 'fig_'
    
    student_names = data.students.keys()
    
    for name in student_names:
        student = data.students[name]
        
        vsg = VisualStudentGraphic(student)
        vsg.save_fig('../graphics/', fig_name+str(count))
        count += 1
    '''
    student = data.students[u"Natália Moreira Viana"]
        
    vsg = VisualStudentGraphic(student)
    #vsg.plot()
    vsg.save_fig('./','teste')
    