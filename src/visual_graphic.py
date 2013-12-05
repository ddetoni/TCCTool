'''
Created on 05/12/2013

@author: douglas
'''
from src.utils import week_interaction
import matplotlib.pyplot as plt


def build_graphic(student, average = None):
    
        #52 weeks -> year
        ticks = range(0, 53, 4)

        week_interactions = week_interaction(student.interactions)

        weeks = week_interactions.keys()
        weeks.sort()

        x = weeks
        #Add week interactions
        y = [week_interactions[w] for w in weeks]

        #Set week points and interactions points
        plt.plot(x, y, 'o-', None, True)
        
        if average != None:
            week_interactions = week_interaction(average)

            weeks = week_interactions.keys()
            weeks.sort()

            xAv = weeks
            #Add week interactions
            yAv = [week_interactions[w] for w in weeks]
            
            plt.plot(xAv, yAv, 'o-', None, True)
        
        
        plt.xticks(ticks)

        plt.ylabel('Number of Interactions')
        plt.xlabel('Week')
        plt.title(student.name + ' ' + student.last_name +
                  ' - Interaction Graphic')
        
        return plt

def save_graphic_course(course, save_path):
    count = 0
    g_name = 'graphic_'

    student_names = course.students.keys()

    for name in student_names:
        student = course.students[name]

        plt = build_graphic(student, course.get_average())
        save_graphic(plt, save_path, g_name+str(count))
        print "Save GRAPHIC: "+g_name+str(count)
        count += 1

def save_graphic_semester():
    pass

def show_graphic(plt):
    plt.show()

def save_graphic(plt, save_path, save_name):
    final_path = save_path+save_name+".png"
    plt.savefig(final_path, format='png')
    plt.close()
    
