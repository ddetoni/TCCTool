# -*- coding: utf-8 -*-

import string
import os
import sys
import pickle
from student import Student
from course import Course


class DataLoader:

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
            elif (previous_c.isalpha() or previous_c.isdigit()) and \
                    (next_c.isalpha() or next_c.isdigit()):
                line_without_space = line_without_space + actual_c

            previous_c = actual_c
            actual_c = next_c

        if next_c != "\n":
            line_without_space = line_without_space + next_c

        return line_without_space

    def load_from_file(self, file_path, name_course):

        print "Starting to load \'" + file_path + "\' file.\n"
        
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

            new_line = self.remove_white_space(line)
            split_line = string.split(new_line, "|")

            if len(split_line) != 3:
                continue

            #Verify if student exist
            complete_name = split_line[0]+" "+split_line[1]
            first_name = split_line[0]
            last_name = split_line[1]
            timestamp = split_line[2]
            if complete_name in course.students:
                student = course.students.get(complete_name)
                student.set_interation(split_line[2])
            else:
                student = Student(first_name, last_name)
                student.set_interation(timestamp)
                course.students[complete_name] = student

            count_interaction += 1

        data.close()
        #Serialization
        #pickle.dump(course, open(file_path+".srz", 'wb'))

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
        print "Total interations: " + str(count_interaction)
        print "Interactions per student: " + str(interactions_per_student)
