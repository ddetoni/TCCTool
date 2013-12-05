# -*- coding: utf-8 -*-

import string
import os
import sys
import pickle
from student import Student
from course import Course
from src.utils import remove_white_space


class DataLoader:

    def load_from_file(self, file_path, name_course):

        print "\nStarting to load \'" + file_path + "\' file.\n"

        data = open(file_path)

        data_size = os.path.getsize(file_path)
        data_processed = 0

        # Put the carret at the right place
        data_processed = data_processed + len(data.readline())
        data_processed = data_processed + len(data.readline())

        course = Course(name_course)
        count_interaction = 0

        for line in data:

            data_processed = data_processed + len(line)
            self.progress_load(data_size, data_processed)

            new_line = remove_white_space(line)
            split_line = string.split(new_line, "|")

            #split_line must have 3 position
            if len(split_line) != 3:
                continue

            #Verify if student exist
            complete_name = split_line[0]+" "+split_line[1]
            first_name = split_line[0]
            last_name = split_line[1]
            timestamp = split_line[2]
            
            conf_interaction = None
            if complete_name in course.students:
                student = course.students.get(complete_name)
                conf_interaction = student.set_interation(timestamp)
            else:
                student = Student(first_name, last_name)
                conf_interaction = student.set_interation(timestamp)
                course.students[complete_name] = student
            
            #Exclude the invalid dates
            if conf_interaction != 0:    
                course.add_to_average(timestamp, 1)
            
            count_interaction += 1

        data.close()

        print "\n"
        self.print_data_stats(count_interaction, course)

        return course

    def load_from_serial(self, srz_file_path):
        self.course = pickle.load(open(srz_file_path, 'r'))

        self.print_data_stats(self.count_interaction)

        return self.course

    def progress_load(self, data_size, data_processed):

        percentage_done = data_processed/float(data_size)

        teste = "\rProgress: " + str(int(percentage_done*100))+"% DONE."
        sys.stdout.write(teste)    # or print >> sys.stdout, "\r%d%%" %i,
        sys.stdout.flush()

    def print_data_stats(self, count_interaction, course):

        total_students = len(course.students.keys())
        interactions_per_student = count_interaction/total_students

        print "Total students: " + str(total_students)
        print "Total interactions: " + str(count_interaction)
        print "Interactions per student: " + str(interactions_per_student)
