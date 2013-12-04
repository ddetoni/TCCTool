# -*- coding: utf-8 -*-

'''
Created on 26/11/2013

@author: douglas
'''

from dataloader import DataLoader
from visual_student_graphic import VisualStudentGraphic

if __name__ == '__main__':

    
    course2 = DataLoader().load_from_file('../data/semester_2/logs_course_62.in')
    
    course = DataLoader().load_from_serial('../data/semester_2/logs_course_62.in.srz')
    
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
    
    if course != course2:
        print "igual"
    
    student = course.students[u"Eolita Pozzebon"]
    
    student2 = course2.students[u"Eolita Pozzebon"]
    
    vsg = VisualStudentGraphic(student)
    vsg.plot()
    
    vsg = VisualStudentGraphic(student2)
    vsg.plot()
    #vsg.save_fig('./','teste')
