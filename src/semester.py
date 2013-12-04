'''
Created on 04/12/2013

@author: douglas
'''
import pickle

class Semester:

    courses = None
    name = None
    normalize_students = None

    def __init__(self, name):
        
        self.courses = {}
        self.name = name
    
    #This fuction remove the students that are not in all the courses.
    def normalize(self):
        
        #print "Normalizing semester..."
        course_names = self.courses.keys();
        
        for c_name in course_names:

            students = self.courses[c_name].students
            student_names = students.keys()
            
            if self.normalize_students == None:
                self.normalize_students = set(student_names)
            else:
                self.normalize_students = self.normalize_students.intersection(set(student_names))
        
        for c_name in course_names:
            
            students = self.courses[c_name].students
            student_names = students.keys()
            
            diff_students = set(student_names).difference(self.normalize_students)
            
            while diff_students:
                
                s_name = diff_students.pop()
                del self.courses[c_name].students[s_name]
        
        #print "Semester normalized.\n"

    #Save a serialization of semester
    def save(self, file_path):

        pickle.dump(self, open(file_path + self.name + ".srz", 'wb'))
    
    #Load a serializantion
    def load(self, srz_file_path):

        self = pickle.load(open(srz_file_path, 'r'))
        return self

    def print_all_student_names(self):
        
        student_names = list(self.normalize_students)
        student_names.sort()
        
        for name in student_names:
            print name
    
    def info(self):

        print "Info: " + self.name
        print "Number of courses: " + str(len(self.courses))
        
        if self.normalize_students == None:
            print "Semester don't normalized. Number of students unknown. \n"
        else:
            print "Total of students: " + str(len(self.normalize_students)) + "\n"

    def del_student(self, student_name):
        
        course_names = self.courses.keys()
        
        for  c_name in course_names:
            try:
                self.courses[c_name].del_student(student_name)
            except KeyError:
                continue
        
        if self.normalize_students != None:
            self.normalize_students.remove(student_name)