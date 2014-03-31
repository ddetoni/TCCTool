# -*- coding: utf-8 -*-

'''
Created on 26/11/2013

@author: douglas
'''

from dataloader import DataLoader
from semester import Semester
from visual_graphic import save_graphic_semester
#from src.utils import approved

if __name__ == '__main__':
    
    semester_1 = Semester("Semester_1")
    
    course0 = DataLoader().load_from_file('../data/semester_1/logs_course_35.in',
                                          '../data/semester_1/logs_course_35_professors.in',
                                          '../data/semester_1/exclude_student_35',
                                           'APE_I')
    course1 = DataLoader().load_from_file('../data/semester_1/logs_course_36.in',
                                          '../data/semester_1/logs_course_36_professors.in',
                                          '../data/semester_1/exclude_student_36',
                                          'PEI_I')
    course2 = DataLoader().load_from_file('../data/semester_1/logs_course_37.in',
                                          '../data/semester_1/logs_course_37_professors.in',
                                          '../data/semester_1/exclude_student_37',
                                          'EPP_I')
    course3 = DataLoader().load_from_file('../data/semester_1/logs_course_38.in',
                                          '../data/semester_1/logs_course_38_professors.in',
                                          '../data/semester_1/exclude_student_38',
                                          'EC_I')
    course4 = DataLoader().load_from_file('../data/semester_1/logs_course_39.in',
                                          '../data/semester_1/logs_course_39_professors.in',
                                          '../data/semester_1/exclude_student_39',
                                          'EAD_I')
    
    semester_1.courses[course0.name] = course0
    semester_1.courses[course1.name] = course1
    semester_1.courses[course2.name] = course2
    semester_1.courses[course3.name] = course3
    semester_1.courses[course4.name] = course4

    #semester_1.normalize()
    #semester_1.save("../data/semester_1/")    

    
    semester_2 = Semester("Semester_2")
    
    course5 = DataLoader().load_from_file('../data/semester_2/logs_course_61.in',
                                          '../data/semester_2/logs_course_61_professors.in',
                                          '../data/semester_2/exclude_student_61',
                                           'EAD_II')
    course6 = DataLoader().load_from_file('../data/semester_2/logs_course_62.in',
                                          '../data/semester_2/logs_course_62_professors.in',
                                          '../data/semester_2/exclude_student_62',
                                          'EPP_II')
    course7 = DataLoader().load_from_file('../data/semester_2/logs_course_63.in',
                                          '../data/semester_2/logs_course_63_professors.in',
                                          '../data/semester_2/exclude_student_63',
                                          'EC_II')
    course8 = DataLoader().load_from_file('../data/semester_2/logs_course_64.in',
                                          '../data/semester_2/logs_course_64_professors.in',
                                          '../data/semester_2/exclude_student_64',
                                          'AP_II')
    course9 = DataLoader().load_from_file('../data/semester_2/logs_course_65.in',
                                          '../data/semester_2/logs_course_65_professors.in',
                                          '../data/semester_2/exclude_student_65',
                                          'PE_II')
    
    semester_2.courses[course5.name] = course5
    semester_2.courses[course6.name] = course6
    semester_2.courses[course7.name] = course7
    semester_2.courses[course8.name] = course8
    semester_2.courses[course9.name] = course9
    
    semester_1.verify_approved(semester_2)
    #save_graphic_semester(semester_1, '../graphics/semester_1/')
    semester_1.print_all_student_names()