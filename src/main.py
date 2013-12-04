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
    semester_2 = Semester("Semester_2")
    
    course0 = DataLoader().load_from_file('../data/semester_2/logs_course_61.in', 'EAD_II')
    course1 = DataLoader().load_from_file('../data/semester_2/logs_course_62.in', 'EPP_II')
    course2 = DataLoader().load_from_file('../data/semester_2/logs_course_63.in', 'EC_II')
    course3 = DataLoader().load_from_file('../data/semester_2/logs_course_64.in', 'AP_II')
    course4 = DataLoader().load_from_file('../data/semester_2/logs_course_65.in', 'PE_II')
    
    semester_2.courses[course0.name] = course0
    semester_2.courses[course1.name] = course1
    semester_2.courses[course2.name] = course2
    semester_2.courses[course3.name] = course3
    semester_2.courses[course4.name] = course4
    
    semester_2.normalize()
    semester_2.save("../data/semester_2/")
    '''
    
    semester_1 = Semester('load').load('../data/semester_1/Semester_1.srz')

    semester_2 = Semester('load').load('../data/semester_2/Semester_2.srz')
    
    semester_1.info()
    semester_2.info()
    
    teste = semester_1.normalize_students.difference(semester_2.normalize_students)
    
    
    print len(teste)
    
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