# -*- coding: utf-8 -*-
'''
Created on 04/12/2013

@author: douglas
'''
import pickle
import unicodecsv


class Semester:

    courses = None
    name = None
    normalize_students = None

    def __init__(self, name):

        self.courses = {}
        self.name = name

    # This fuction remove the students that are not in all the courses.
    def normalize(self):

        # print "Normalizing semester..."
        course_names = self.courses.keys()

        for c_name in course_names:

            students = self.courses[c_name].students
            student_names = students.keys()

            if self.normalize_students is None:
                self.normalize_students = set(student_names)
            else:
                self.normalize_students = self.normalize_students. \
                    intersection(set(student_names))

        for c_name in course_names:

            students = self.courses[c_name].students
            student_names = students.keys()

            diff_students = set(student_names).difference(
                self.normalize_students)

            while diff_students:

                s_name = diff_students.pop()
                del self.courses[c_name].students[s_name]

        # print "Semester normalized.\n"

    # Save a serialization of semester
    def save(self, file_path):

        pickle.dump(self, open(file_path + self.name + ".srz", 'wb'))

    # Load a serializantion
    def load(self, srz_file_path):

        self = pickle.load(open(srz_file_path, 'r'))
        return self

    # Bug: Situation is not correct
    def print_all_student_names(self):

        already_printed = []

        for course in self.courses.itervalues():
            for student in course.students.itervalues():
                complete_name = student.name + ' ' + student.last_name
                if complete_name not in already_printed:
                    already_printed.append(complete_name)
                    print complete_name + ' - ' + str(student.result)

    def info(self):

        print "Info: " + self.name
        print "Number of courses: " + str(len(self.courses))

        if self.normalize_students is None:
            print "Semester don't normalized. Number of students unknown. \n"
        else:
            print "Total of students: " + str(len(self.normalize_students)) \
                + "\n"

    def del_student(self, student_name):

        course_names = self.courses.keys()

        for c_name in course_names:
            try:
                self.courses[c_name].del_student(student_name)
            except KeyError:
                continue

        if self.normalize_students is not None:
            self.normalize_students.remove(student_name)

    def del_students(self, student_list):

        for s_name in student_list:
            self.del_student(s_name)

    def get_all_student_names(self):

        student_names = []

        for course in self.courses.itervalues():
            for student in course.students.itervalues():
                complete_name = student.name + ' ' + student.last_name
                if complete_name not in student_names:
                    student_names.append(complete_name)

        return student_names

    def verify_approved(self, following_semester):

        s_names = following_semester.get_all_student_names()

        for course in self.courses.itervalues():
            for student in course.students.itervalues():
                complete_name = student.name + ' ' + student.last_name
                if complete_name in s_names:
                    student.result = 2
                else:
                    student.result = 1

    def correct_situation(self, file_path):

        with open(file_path, 'rb') as csvfile:
            correct_situation = unicodecsv.reader(csvfile, delimiter=',',
                                                  encoding='utf-8')
            for row in correct_situation:
                if row[2] == 'excluir':
                    self.del_student(row[0])
                elif row[2] == 'aprovado':
                    student = self.courses[row[1]].students[row[0]]
                    student.result = 2
                    self.courses[row[1]].students[row[0]] = student
