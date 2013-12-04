'''
Created on 04/12/2013

@author: douglas
'''

class Semester:

    courses = None
    name = None

    def __init__(self, name):
        
        self.courses = {}
        name = name