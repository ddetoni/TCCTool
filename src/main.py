'''
Created on 26/11/2013

@author: douglas
'''
from student import Student

if __name__ == '__main__':
    a = open('../data/name.in')
    print a.readline()
    
    s = Student('Douglas', 'Detoni')
    print s.lastname
    
    s.interations['teste'] = 1555
    print s.interations['teste']