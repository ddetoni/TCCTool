'''
Created on 04/12/2013

@author: douglas
'''

#This method apply an intersection between two semester 
#and return a list of approved students.
def approved(semester1, semester2):
    
    approved = list(semester1.normalize_students.intersection \
                    (semester2.normalize_students))
    return approved

def dispproved(semester1, semester2):

    dispproved = list(semester1.normalize_students.difference \
                    (semester2.normalize_students))
    return dispproved