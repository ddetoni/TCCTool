# -*- coding: utf-8 -*-

'''
Created on 26/11/2013

@author: douglas
'''

from dataloader import DataLoader
from semester import Semester
from visual_student_graphic import VisualStudentGraphic

if __name__ == '__main__':
    
    '''
    semester = Semester("Semester_1")
    
    course0 = DataLoader().load_from_file('../data/semester_1/logs_course_35.in', 'APE_I')
    course1 = DataLoader().load_from_file('../data/semester_1/logs_course_36.in', 'PE_I')
    course2 = DataLoader().load_from_file('../data/semester_1/logs_course_37.in', 'EPP_I')
    course3 = DataLoader().load_from_file('../data/semester_1/logs_course_38.in', 'EC_I')
    course4 = DataLoader().load_from_file('../data/semester_1/logs_course_39.in', 'EAD_I')
    
    semester.courses[course0.name] = course0
    semester.courses[course1.name] = course1
    semester.courses[course2.name] = course2
    semester.courses[course3.name] = course3
    semester.courses[course4.name] = course4
    
    semester.save("../data/semester_1/")
    '''
    
    semester = Semester('load').load('../data/semester_1/Semester_1.srz')
    semester.normalize()
    
    semester.print_all_student_names()
    
    '''
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
    '''
    student = course.students[u"Eolita Pozzebon"]
    
    vsg = VisualStudentGraphic(student)
    vsg.plot()
    #vsg.save_fig('./','teste')
    '''