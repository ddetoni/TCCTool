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
