'''
Created on 05/12/2013

@author: douglas
'''
from utils import week_interaction
import matplotlib.pyplot as plt
import os
from student import Student

def build_graphic(person, average=None):

        #52 weeks -> year
        ticks = range(0, 53, 4)

        week_interactions = week_interaction(person.interactions)

        weeks = week_interactions.keys()
        weeks.sort()

        x = weeks
        #Add week interactions
        y = [week_interactions[w] for w in weeks]

        #Set week points and interactions points
        plt.plot(x, y, 'o-', None, True)

        if average is not None:
            week_interactions = week_interaction(average)

            weeks = week_interactions.keys()
            weeks.sort()

            xAv = weeks
            #Add week interactions
            yAv = [week_interactions[w] for w in weeks]

            plt.plot(xAv, yAv, 'o-', None, True)

        plt.xticks(ticks)
        
        if isinstance(person, Student):
            if person.result == 2:
                result = "Approved"
            elif person.result == 1:
                result = "Disapproved"
            else:
                result = "No info"

        plt.ylabel('Interaction Number')
        plt.xlabel('Week')
        
        if isinstance(person, Student):
            plt.title(person.name + ' ' + person.last_name +
                      ' - ' + result)
        else:
            plt.title(person.name + ' ' + person.last_name)

        return plt


def save_graphic_course(course, save_path):

    os.mkdir(save_path)
    os.mkdir(save_path + 'students/')
    os.mkdir(save_path + 'professors/')

    count_students = 0
    count_professors = 0
    g_name = 'graphic_'

    student_names = course.students.keys()

    for name in student_names:
        student = course.students[name]

        plt = build_graphic(student, course.get_average_each_week())
        save_graphic(plt, save_path+'students/', g_name+str(count_students))
        count_students += 1
        
    for professor in course.professors.itervalues():
        plt = build_graphic(professor, course.get_average_each_week())
        save_graphic(plt, save_path+'professors/', g_name+str(count_professors))
        count_professors += 1

def save_graphic_semester(semester, save_path):

    if not os.path.exists(save_path):
        os.mkdir(save_path)

    course_names = semester.courses.keys()

    for c_name in course_names:
        save_graphic_course(semester.courses[c_name],
                            save_path + c_name + '/')


def show_graphic(plt):
    plt.show()


def save_graphic(plt, save_path, save_name):
    final_path = save_path+save_name+".png"
    print 'Saving GRAPHIC: ' + final_path
    plt.savefig(final_path, format='png')
    plt.close()
