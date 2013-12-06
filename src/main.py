# -*- coding: utf-8 -*-

'''
Created on 26/11/2013

@author: douglas
'''

from dataloader import DataLoader
from semester import Semester
from src.visual_graphic import save_graphic_semester
from src.utils import dispproved

if __name__ == '__main__':
    '''
    semester_1 = Semester("Semester_1")
    
    course0 = DataLoader().load_from_file('../data/semester_1/logs_course_35.in', 'APE_I')
    course1 = DataLoader().load_from_file('../data/semester_1/logs_course_36.in', 'PEI_I')
    course2 = DataLoader().load_from_file('../data/semester_1/logs_course_37.in', 'EPP_I')
    course3 = DataLoader().load_from_file('../data/semester_1/logs_course_38.in', 'EC_I')
    course4 = DataLoader().load_from_file('../data/semester_1/logs_course_39.in', 'EAD_I')
    
    semester_1.courses[course0.name] = course0
    semester_1.courses[course1.name] = course1
    semester_1.courses[course2.name] = course2
    semester_1.courses[course3.name] = course3
    semester_1.courses[course4.name] = course4
    
    semester_1.normalize()
    semester_1.save("../data/semester_1/")    
    
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
    
    dis_students = dispproved(semester_1, semester_2)
    
    semester_1.del_students(dis_students)
    
    semester_1.info()
    
    save_graphic_semester(semester_1, '../graphics/semester_1/')
    