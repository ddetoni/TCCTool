# -*- coding: utf-8 -*-

import string
from student import Student

class DataLoader:
    
    def __init__(self):
        self.students = {}
    
    #Remove all the invalids white spaces from a line.
    #Return a string with the words separated by "| " 
    def remove_invalid_space(self, file_line):
        
        line_without_space = ""
        
        previous_c = " "
        actual_c = " "
        next_c = " "
        
        line = unicode(file_line, encoding="utf-8")
        
        for c in line:
            next_c = c
            
            #Case test for the variable actual_c
            if previous_c != " " and actual_c == " " and next_c != " ":
                line_without_space = line_without_space + actual_c
            elif previous_c == " " and actual_c != " ":
                line_without_space = line_without_space + actual_c
            elif actual_c != " ":
                line_without_space = line_without_space + actual_c
                
            previous_c = actual_c
            actual_c = next_c
        
        if next_c != "\n":
            line_without_space = line_without_space + next_c
        
        return line_without_space
    
    def loader(self, folder_name):
        data = open(folder_name)
            
        for line in data:
            new_line = self.remove_invalid_space(line)
            split_line = string.split(new_line,"| ")
            
            if self.students.has_key(split_line[0]+" "+split_line[1]):
                student = self.students.get(split_line[0]+" "+split_line[1])
                student.set_interation(split_line[2])
            else:
                student = Student(split_line[0], split_line[1])
                student.set_interation(split_line[2])
                self.students[split_line[0]+" "+split_line[1]] = student
        
        print self.students
        
        
        