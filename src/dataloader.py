# -*- coding: utf-8 -*-

import string
import os, sys
from student import Student

class DataLoader:
    
    def __init__(self):
        self.students = {}
    
    #Remove all the invalids white spaces from a line.
    #Return a string with the words separated by "| " 
    def remove_white_space(self, file_line):
        
        line_without_space = ""
        
        previous_c = " "
        actual_c = " "
        next_c = " "
        
        line = unicode(file_line, encoding="utf-8")
        
        for c in line:
            next_c = c
            
            #Case test for the variable actual_c
            if not actual_c.isspace():
                line_without_space = line_without_space + actual_c
            elif (previous_c.isalpha() or previous_c.isdigit())  and (next_c.isalpha() or next_c.isdigit()):
                line_without_space = line_without_space + actual_c
                
            
            previous_c = actual_c
            actual_c = next_c
        
        if next_c != "\n":
            line_without_space = line_without_space + next_c
        
        return line_without_space
    
    def loader(self, folder_name):
        
        print "Starting to load \'" + folder_name + "\' file.\n" 
        
        data = open(folder_name)
        data_size = os.path.getsize(folder_name)
        data_processed = 0
        count_interaction = 0
        
        # Put the carret at the right place
        data_processed = data_processed + len(data.readline())
        data_processed = data_processed + len(data.readline())
            
        for line in data:
            
            data_processed = data_processed + len(line)
            self.progress_load(data_size, data_processed)
            
            new_line = self.remove_white_space(line)
            split_line = string.split(new_line,"|")
            
            #Verify if student exist
            if self.students.has_key(split_line[0]+" "+split_line[1]):
                student = self.students.get(split_line[0]+" "+split_line[1])
                student.set_interation(split_line[2])
            else:
                student = Student(split_line[0], split_line[1])
                student.set_interation(split_line[2])
                self.students[split_line[0]+" "+split_line[1]] = student
                
            count_interaction += 1
        
        data.close()
        
        print "\n"
        
        self.print_data_stats(count_interaction)
        
    def progress_load(self, data_size, data_processed):
        
        percentage_done =data_processed/float(data_size)
        
        teste = "\rProgress: " + str(int(percentage_done*100))+"% DONE."
        sys.stdout.write(teste)    # or print >> sys.stdout, "\r%d%%" %i,
        sys.stdout.flush()
        
    def print_data_stats(self, count_interaction):
        
        total_students = len(self.students.keys());
        interactions_per_student = count_interaction/total_students
        
        print "Total students: " + str(total_students)
        print "Total interations: " + str(count_interaction)
        print "Interactions per student: " + str(interactions_per_student)        
        