'''
Created on 04/12/2013

@author: douglas
'''
import datetime


class Course:

    students = None
    professors = None
    name = None
    total_interactions_each_week = None

    def __init__(self, name):

        self.students = {}
        self.professors = {}
        self.name = name
        self.total_interactions_each_week = {}

    def del_student(self, student_name):
        try:
            dates = self.students[student_name].interactions.keys()

            for date in dates:

                if date in self.total_interactions_each_week:
                    self.total_interactions_each_week[date] -= \
                        self.students[student_name].interactions[date]

            del self.students[student_name]
        except KeyError:
            return None

    def add_to_week_average(self, timestamp, n_interaction):

        date = datetime.datetime.fromtimestamp(float(timestamp))

        #Date formated
        date = date.strftime('%d/%m/%y')
        if date in self.total_interactions_each_week:
            self.total_interactions_each_week[date] += n_interaction
        else:
            self.total_interactions_each_week[date] = n_interaction

    def get_average_each_week(self):

        average = {}
        total_students = len(self.students)
        keys = self.total_interactions_each_week.keys()

        for date in keys:
            interactions = self.total_interactions_each_week[date]
            average[date] = interactions/total_students

        return average
