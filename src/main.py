# -*- coding: utf-8 -*-

'''
Created on 26/11/2013

@author: douglas
'''

from dataloader import DataLoader
from visual_student_graphic import VisualStudentGraphic

if __name__ == '__main__':

    course = DataLoader().load_from_file('../data/semester_1/logs_course_39.in')
    

    count = 0
    fig_name = 'fig_'

    student_names = course.students.keys()

    for name in student_names:
        student = course.students[name]

        vsg = VisualStudentGraphic(student)
        vsg.save_fig('../graphics/semester_1/39/', fig_name+str(count))
        print "Save FIG: "+fig_name+str(count)
        count += 1

    '''
    student = course.students[u"Eolita Pozzebon"]
    
    vsg = VisualStudentGraphic(student)
    vsg.plot()
    #vsg.save_fig('./','teste')
    '''