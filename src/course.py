'''
Created on 04/12/2013

@author: douglas
'''


class Course:

    students = None
    name = None
    overall_average = None

    def __init__(self, name):

        self.students = {}
        self.name = name
        self.overall_average = {}

    def del_student(self, student_name):
        try:
            del self.students[student_name]
        except KeyError:
            return None
    
    def add_to_average(self, date, n_interaction):
        
        if date in self.overall_average:
            self.overall_average[date] += n_interaction
        else:
            self.overall_average[date] = n_interaction
    
    def get_average(self):
        
        average = {}
        total_students = len(self.students)
        keys = self.overall_average.keys()
        
        for date in keys:
            interactions = self.overall_average[date]
            average[date] = interactions/total_students
        
        return average