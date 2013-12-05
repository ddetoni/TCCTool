'''
Created on 04/12/2013

@author: douglas
'''


class Course:

    students = None
    name = None

    def __init__(self, name):

        self.students = {}
        self.name = name

    def del_student(self, student_name):
        try:
            del self.students[student_name]
        except KeyError:
            return None