# -*- coding: utf-8 -*-

'''
Created on 26/11/2013

@author: douglas
'''

from dataloader import DataLoader
from semester import Semester
from visual_graphic import save_graphic_semester, build_boxplot
#from src.utils import approved

def load_first_semester_clec():
    semester = Semester("Semester_1")
    begin_date = 1357005600   #Timestamp = 01/01/2013-00:00:00
    end_date = 1388455200     #Timestamp = 31/12/2013-00:00:00
    
    course0 = DataLoader().load_from_file('../data/CLEC/first_semester/APE-I/',
                                           'APE_I',
                                           begin_date, end_date)
    
    course1 = DataLoader().load_from_file('../data/CLEC/first_semester/EAD-I/',
                                           'EAD_I',
                                           begin_date, end_date)
    
    course2 = DataLoader().load_from_file('../data/CLEC/first_semester/EC-I/',
                                           'EC_I',
                                           begin_date, end_date)
    
    course3 = DataLoader().load_from_file('../data/CLEC/first_semester/EPP-I/',
                                           'EPP_I',
                                           begin_date, end_date)
    
    course4 = DataLoader().load_from_file('../data/CLEC/first_semester/PE-I/',
                                           'PE_I',
                                           begin_date, end_date)
    
    semester.courses[course0.name] = course0
    semester.courses[course1.name] = course1
    semester.courses[course2.name] = course2
    semester.courses[course3.name] = course3
    semester.courses[course4.name] = course4
    
    return semester

def load_second_semester_clec():
    semester = Semester("Semester_2")
    begin_date = 1357005600   #Timestamp = 01/01/2013-00:00:00
    end_date = 1388455200     #Timestamp = 31/12/2013-00:00:00
    
    course0 = DataLoader().load_from_file('../data/CLEC/second_semester/APE-II/',
                                           'APE_II',
                                           begin_date, end_date)

    course1 = DataLoader().load_from_file('../data/CLEC/second_semester/EAD-II/',
                                           'EAD_II',
                                           begin_date, end_date)

    course2 = DataLoader().load_from_file('../data/CLEC/second_semester/EC-II/',
                                           'EC_II',
                                           begin_date, end_date)

    course3 = DataLoader().load_from_file('../data/CLEC/second_semester/EPP-II/',
                                           'EPP_II',
                                           begin_date, end_date)
    
    course4 = DataLoader().load_from_file('../data/CLEC/second_semester/PE-II/',
                                           'PE_II',
                                           begin_date, end_date)
    
    semester.courses[course0.name] = course0
    semester.courses[course1.name] = course1
    semester.courses[course2.name] = course2
    semester.courses[course3.name] = course3
    semester.courses[course4.name] = course4
    
    return semester

def load_third_semester_clec():
    semester = Semester("Semester_3")
    begin_date = 1388541600   #Timestamp = 01/01/2014-00:00:00
    end_date = 1419991200     #Timestamp = 31/12/2014-00:00:00
    
    course0 = DataLoader().load_from_file('../data/CLEC/third_semester/APE-III/',
                                           'APE_III',
                                           begin_date, end_date)

    course1 = DataLoader().load_from_file('../data/CLEC/third_semester/EC-III/',
                                           'EC_III',
                                           begin_date, end_date)

    course2 = DataLoader().load_from_file('../data/CLEC/third_semester/ECo-I/',
                                           'ECo_I',
                                           begin_date, end_date)

    course3 = DataLoader().load_from_file('../data/CLEC/third_semester/EPP-III/',
                                           'EPP_III',
                                           begin_date, end_date)
    
    course4 = DataLoader().load_from_file('../data/CLEC/third_semester/Lib-I/',
                                           'Lib_I',
                                           begin_date, end_date)
    
    course5 = DataLoader().load_from_file('../data/CLEC/third_semester/PE-III/',
                                           'PE_III',
                                           begin_date, end_date)
    
    semester.courses[course0.name] = course0
    semester.courses[course1.name] = course1
    semester.courses[course2.name] = course2
    semester.courses[course3.name] = course3
    semester.courses[course4.name] = course4
    semester.courses[course5.name] = course5
    
    return semester

if __name__ == '__main__':

    #semester_1 = load_first_semester_clec()
    semester_2 = load_second_semester_clec()
    semester_3 = load_third_semester_clec()

    semester_2.verify_approved(semester_3)

    #semester_1.save("../data/semester_1/")
    #semester_2.save("../data/semester_2/")

    #semester_1 = Semester("Semester_1").load("../data/semester_1/Semester_1.srz")
    #semester_2 = Semester("Semester_2").load("../data/semester_2/Semester_2.srz")
    
    #save_graphic_semester(semester_1, '../graphics/semester_1/')
    semester_2.print_all_student_names()

    #build_boxplot(semester_1.courses['EAD_I'])
    
    '''
    semester_1.courses['EAD_I'].general_statistics()
    semester_1.courses['EAD_I'].week_statistics()
    
    semester_1.courses['EPP_I'].general_statistics()
    semester_1.courses['EPP_I'].week_statistics()
    
    semester_1.courses['APE_I'].general_statistics()
    semester_1.courses['APE_I'].week_statistics()
    
    semester_1.courses['PEI_I'].general_statistics()
    semester_1.courses['PEI_I'].week_statistics()
    
    semester_1.courses['EC_I'].general_statistics()
    semester_1.courses['EC_I'].week_statistics()
    '''