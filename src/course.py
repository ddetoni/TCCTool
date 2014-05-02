'''
Created on 04/12/2013

@author: douglas
'''
import datetime
from math import sqrt
from utils import week_interaction


class Course:

    students = None
    professors = None
    tutors = None
    name = None
    total_interactions_each_week = None

    def __init__(self, name):

        self.students = {}
        self.professors = {}
        self.tutors = {}
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
    
    def general_statistics(self):
        
        total_students = len(self.students)
        
        all_interaction_numbers = []
        count_interactions = 0
        for student in self.students.itervalues():
            count_interactions = count_interactions + student.total_interactions
            all_interaction_numbers.append(student.total_interactions)
        
        average = count_interactions/total_students
        
        all_interaction_numbers.sort()
        median1 = -1;
        median2 = -1;
        if total_students%2 == 0:
            median1 = all_interaction_numbers[total_students/2]
            median2 = all_interaction_numbers[(total_students/2)-1]
        else:
            median1 = all_interaction_numbers[total_students/2]
        
        difference_with_average = []
        for number in all_interaction_numbers:
            difference_with_average.append(average-number)
        
        count_square_sum = 0
        for number in difference_with_average:
            count_square_sum = count_square_sum + (number*number)

        standard_deviation = sqrt(count_square_sum/total_students)
        
        print self.name + ' statistics:'
        print 'Student average: ' + str(average)

        if(median2 != -1):
            print 'Median: ' + str(median1) + ' and ' + str(median2)
        else:
            print 'Median: ' + str(median1)
            
        print 'Standard deviation: +/-%.2f' % standard_deviation
        print ''
        
        return [average, median1, median2, standard_deviation]
        
    def week_statistics(self):
            
        week_average_list = []
        total_students = len(self.students)
        
        for student in self.students.itervalues():
            week_interactions = week_interaction(student.interactions)
            week_average_list.append(student.total_interactions/len(week_interactions))
        
        week_average_list.sort()
        
        sum_average = 0
        for number in week_average_list:
            sum_average = sum_average + number;
            
        average = sum_average/total_students
        
        median1 = -1;
        median2 = -1;
        if total_students%2 == 0:
            median1 = week_average_list[total_students/2]
            median2 = week_average_list[(total_students/2)-1]
        else:
            median1 = week_average_list[total_students/2]
        
        difference_with_average = []
        for number in week_average_list:
            difference_with_average.append(average-number)
        
        count_square_sum = 0
        for number in difference_with_average:
            count_square_sum = count_square_sum + (number*number)

        standard_deviation = sqrt(count_square_sum/total_students)
        
        print self.name + ' statistics by week:'
        print 'Student average: ' + str(average)

        if(median2 != -1):
            print 'Median: ' + str(median1) + ' and ' + str(median2)
        else:
            print 'Median: ' + str(median1)
            
        print 'Standard deviation: +/-%.2f' % standard_deviation
        print ''
        
        return [average, median1, median2, standard_deviation]