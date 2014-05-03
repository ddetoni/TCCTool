# -*- coding: utf-8 -*-

'''
Created on 26/11/2013

@author: douglas
'''

from dataloader import DataLoader
from semester import Semester
from visual_graphic import save_graphic_semester, build_boxplot, save_graphic_group, save_graphics_reproveds
from utils import generate_semester_csv
from hgext.highlight import generate_css
'''
def load_first_semester_clec():
    semester = Semester("Semester_1")
    #begin_date = 1362884400   #Timestamp = 10/03/2013-00:00:00
    #end_date = 1373079600     #Timestamp = 06/07/2013-00:00:00
    
    course0 = DataLoader().load_from_file('../data/CLEC/first_semester/APE-I/',
                                           'APE_I',
                                           1365908400, #14/04/2013
                                           1369537140) #25/05/2013
    
    course1 = DataLoader().load_from_file('../data/CLEC/first_semester/EAD-I/',
                                           'EAD_I',
                                           1362884400, #10/03/2013
                                           1365822000) #13/04/2013
    
    course2 = DataLoader().load_from_file('../data/CLEC/first_semester/EC-I/',
                                           'EC_I',
                                           1369537200, #26/05/2013
                                           1373079600) #06/07/2013
    
    course3 = DataLoader().load_from_file('../data/CLEC/first_semester/EPP-I/',
                                           'EPP_I',
                                           1369537200, #26/05/2013
                                           1373079600) #06/07/2013
    
    course4 = DataLoader().load_from_file('../data/CLEC/first_semester/PE-I/',
                                           'PE_I',
                                           1365908400, #14/04/2013
                                           1369537140) #25/05/2013
    
    semester.courses[course0.name] = course0
    semester.courses[course1.name] = course1
    semester.courses[course2.name] = course2
    semester.courses[course3.name] = course3
    semester.courses[course4.name] = course4
    
    return semester
'''
def load_first_semester_clec():
    semester = Semester("Semester_1")
    begin_date = 1357005600   #Timestamp = 01/01/2013-00:00:00
    end_date = 1375326000    #Timestamp = 01/08/2013-00:00:00
    
    course0 = DataLoader().load_from_file('../data/CLEC/first_semester/APE-I/',
                                           'APE_I',
                                           begin_date, 
                                           end_date)
    
    course1 = DataLoader().load_from_file('../data/CLEC/first_semester/EAD-I/',
                                           'EAD_I',
                                           begin_date, #10/03/2013
                                           end_date) #13/04/2013
    
    course2 = DataLoader().load_from_file('../data/CLEC/first_semester/EC-I/',
                                           'EC_I',
                                           begin_date, 
                                           end_date)
    
    course3 = DataLoader().load_from_file('../data/CLEC/first_semester/EPP-I/',
                                           'EPP_I',
                                           begin_date, 
                                           end_date)
    
    course4 = DataLoader().load_from_file('../data/CLEC/first_semester/PE-I/',
                                           'PE_I',
                                           begin_date, 
                                           end_date)
    
    semester.courses[course0.name] = course0
    semester.courses[course1.name] = course1
    semester.courses[course2.name] = course2
    semester.courses[course3.name] = course3
    semester.courses[course4.name] = course4
    
    return semester

def load_second_semester_clec():
    semester = Semester("Semester_2")
    begin_date = 1375326000   #Timestamp = 01/08/2013-00:00:00
    end_date = 1388455200     #Timestamo = 31/12/2013
    
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

def load_first_semester_clpd():
    semester = Semester("Semester_1")
    begin_date = 1357005600   #Timestamp = 01/01/2013-00:00:00
    end_date = 1375326000    #Timestamp = 01/08/2013-00:00:00
    
    course0 = DataLoader().load_from_file('../data/CLPD/first_semester/APE_I/',
                                           'APE_I',
                                           begin_date, 
                                           end_date)
    
    course1 = DataLoader().load_from_file('../data/CLPD/first_semester/CESADE_I/',
                                           'CESADE_I',
                                           begin_date, #10/03/2013
                                           end_date) #13/04/2013
    
    course2 = DataLoader().load_from_file('../data/CLPD/first_semester/CESEB_I/',
                                           'CESEB_I',
                                           begin_date, 
                                           end_date)
    
    course3 = DataLoader().load_from_file('../data/CLPD/first_semester/CESEI_I/',
                                           'CESEI_I',
                                           begin_date, 
                                           end_date)
    
    course4 = DataLoader().load_from_file('../data/CLPD/first_semester/EAD-NB/',
                                           'EAD-NB',
                                           begin_date, 
                                           end_date)
    
    semester.courses[course0.name] = course0
    semester.courses[course1.name] = course1
    semester.courses[course2.name] = course2
    semester.courses[course3.name] = course3
    semester.courses[course4.name] = course4
    
    return semester

def load_second_semester_clpd():
    semester = Semester("Semester_2")
    begin_date = 1375326000   #Timestamp = 01/08/2013-00:00:00
    end_date = 1388455200     #Timestamp = 31/12/2013-00:00:00
    
    course0 = DataLoader().load_from_file('../data/CLPD/second_semester/APE_II/',
                                           'APE_II',
                                           begin_date, 
                                           end_date)
    
    course1 = DataLoader().load_from_file('../data/CLPD/second_semester/CESADE_II/',
                                           'CESADE_II',
                                           begin_date,
                                           end_date)
    
    course2 = DataLoader().load_from_file('../data/CLPD/second_semester/CESEB_II/',
                                           'CESEB_II',
                                           begin_date, 
                                           end_date)
    
    course3 = DataLoader().load_from_file('../data/CLPD/second_semester/CESEI_II/',
                                           'CESEI_II',
                                           begin_date, 
                                           end_date)
    
    course4 = DataLoader().load_from_file('../data/CLPD/second_semester/ECO_I/',
                                           'ECO_I',
                                           begin_date, 
                                           end_date)
    
    semester.courses[course0.name] = course0
    semester.courses[course1.name] = course1
    semester.courses[course2.name] = course2
    semester.courses[course3.name] = course3
    semester.courses[course4.name] = course4
    
    return semester

def load_third_semester_clpd():
    semester = Semester("Semester_3")
    begin_date = 1388541600   #Timestamp = 01/01/2014-00:00:00
    end_date = 1419991200     #Timestamp = 31/12/2014-00:00:00
    
    course0 = DataLoader().load_from_file('../data/CLPD/third_semester/APE_III/',
                                           'APE_III',
                                           begin_date, 
                                           end_date)
    
    course1 = DataLoader().load_from_file('../data/CLPD/third_semester/COEGDADE_I/',
                                           'COEGDADE_I',
                                           begin_date,
                                           end_date)
    
    course2 = DataLoader().load_from_file('../data/CLPD/third_semester/COEGDEB_I/',
                                           'COEGDEB_I',
                                           begin_date, 
                                           end_date)
    
    course3 = DataLoader().load_from_file('../data/CLPD/third_semester/COEGDEI_I/',
                                           'COEGDEI_I',
                                           begin_date, 
                                           end_date)
    
    course4 = DataLoader().load_from_file('../data/CLPD/third_semester/ECO_II/',
                                           'ECO_II',
                                           begin_date, 
                                           end_date)
    
    semester.courses[course0.name] = course0
    semester.courses[course1.name] = course1
    semester.courses[course2.name] = course2
    semester.courses[course3.name] = course3
    semester.courses[course4.name] = course4
    
    return semester

if __name__ == '__main__':

    #semester_1 = load_first_semester_clec()
    #semester_2 = load_second_semester_clec()
    #semester_3 = load_third_semester_clec()

    #semester_1.verify_approved(semester_2)
    #semester_2.verify_approved(semester_3)

    #semester_1.save("../data/CLEC/first_semester/")
    #semester_2.save("../data/CLEC/second_semester/")
    #semester_3.save("../data/CLEC/third_semester/")

    #semester_1 = Semester("Semester_1").load("../data/CLEC/first_semester/Semester_1.srz")
    #semester_2 = Semester("Semester_2").load("../data/CLEC/second_semester/Semester_2.srz")
    #semester_3 = Semester("Semester_3").load("../data/CLEC/third_semester/Semester_3.srz")
    
    #save_graphic_semester(semester_1, '../graphics/CLEC/semester_1/')
    #save_graphic_semester(semester_2, '../graphics/CLEC/semester_2/')
    
    #save_graphics_reproveds(semester_1, '../graphics/CLEC/semester_1/reproved/')
    #save_graphics_reproveds(semester_2, '../graphics/CLEC/semester_2/reproved/')
    
    #semester_1.print_all_student_names()
    #print '\n'
    #semester_2.print_all_student_names()
    
    #generate_semester_csv(semester_2,'CLEC', 52, '../csv/')
    
    #-------------------------------------------------------------------------------------#
    
    #semester_1 = load_first_semester_clpd()
    #semester_2 = load_second_semester_clpd()
    #semester_3 = load_third_semester_clpd()
    
    #semester_1.verify_approved(semester_2)
    #semester_2.verify_approved(semester_3)
    
    #semester_1.save("../data/CLPD/first_semester/")
    #semester_2.save("../data/CLPD/second_semester/")
    #semester_3.save("../data/CLPD/third_semester/")
    
    #semester_1 = Semester("Semester_1").load("../data/CLPD/first_semester/Semester_1.srz")
    semester_2 = Semester("Semester_2").load("../data/CLPD/second_semester/Semester_2.srz")
    #semester_3 = Semester("Semester_3").load("../data/CLPD/third_semester/Semester_3.srz")
    
    #save_graphic_semester(semester_1, '../graphics/CLPD/semester_1/')
    #save_graphic_semester(semester_2, '../graphics/CLPD/semester_2/')
    
    #save_graphics_reproveds(semester_1, '../graphics/CLPD/semester_1/reproved/')
    #save_graphics_reproveds(semester_2, '../graphics/CLPD/semester_2/reproved/')
    
    generate_semester_csv(semester_2,'CLPD', 52, '../csv/')
    
    #semester_1.print_all_student_names()
    #print '\n'
    #semester_2.print_all_student_names()
    '''
    reproved_group = semester_1.courses['EAD_I'].get_all_reproved()
    save_graphic_group(semester_1, 'EAD_I', reproved_group, '../graphics/semester_1/reproved/')
    
    reproved_group = semester_1.courses['EPP_I'].get_all_reproved()
    save_graphic_group(semester_1, 'EPP_I', reproved_group, '../graphics/semester_1/reproved/')
    
    reproved_group = semester_1.courses['APE_I'].get_all_reproved()
    save_graphic_group(semester_1, 'APE_I', reproved_group, '../graphics/semester_1/reproved/')
    
    reproved_group = semester_1.courses['PE_I'].get_all_reproved()
    save_graphic_group(semester_1, 'PE_I', reproved_group, '../graphics/semester_1/reproved/')
    
    reproved_group = semester_1.courses['EC_I'].get_all_reproved()
    save_graphic_group(semester_1, 'EC_I', reproved_group, '../graphics/semester_1/reproved/')
    '''
    '''
    reproved_group = semester_2.courses['EAD_II'].get_all_reproved()
    save_graphic_group(semester_2, 'EAD_II', reproved_group, '../graphics/semester_2/reproved/')
    
    reproved_group = semester_2.courses['EPP_II'].get_all_reproved()
    save_graphic_group(semester_2, 'EPP_II', reproved_group, '../graphics/semester_2/reproved/')
    
    reproved_group = semester_2.courses['APE_II'].get_all_reproved()
    save_graphic_group(semester_2, 'APE_II', reproved_group, '../graphics/semester_2/reproved/')
    
    reproved_group = semester_2.courses['PE_II'].get_all_reproved()
    save_graphic_group(semester_2, 'PE_II', reproved_group, '../graphics/semester_2/reproved/')
    
    reproved_group = semester_2.courses['EC_II'].get_all_reproved()
    save_graphic_group(semester_2, 'EC_II', reproved_group, '../graphics/semester_2/reproved/')
    '''
    
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