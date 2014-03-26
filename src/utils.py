'''
Created on 04/12/2013

@author: douglas
'''


#This method apply an intersection between two semester
#and return a list of approved students.
def approved(semester1, semester2):

    approved = list(semester1.normalize_students.intersection(
        semester2.normalize_students))
    return approved


#This method return the disapproved students
def dispproved(semester1, semester2):

    dispproved = list(semester1.normalize_students.difference(
        semester2.normalize_students))
    return dispproved


# Convert a day(dd/mm/yy) in your corresponding week
def convert_day_week(date_interaction):

    total_month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    date = date_interaction.split('/')

    day = int(date[0])
    month = int(date[1])

    count_days = 0

    for i in range(0, month-1, 1):
        count_days += total_month_days[i]

    count_days += day

    return count_days/7


#Calculate the interactions by week
def week_interaction(day_interactions):

    inter_days = day_interactions.keys()
    week_interactions = {}

    for day in inter_days:

        week = convert_day_week(day)
        if week in week_interactions:
            count = week_interactions[week]
            count += day_interactions[day]
            week_interactions[week] = count
        else:
            week_interactions[week] = day_interactions[day]

    return week_interactions


#Remove all the invalids white spaces from a line.
#Return a string with the words separated by "| "
def remove_white_space(file_line):

    line_without_space = ""

    previous_c = " "
    actual_c = " "
    next_c = " "

    line = unicode(file_line, encoding="utf-8")

    for c in line:
        next_c = c

        #Case test for the variable actual_c
        if not actual_c.isspace():
            line_without_space = line_without_space + actual_c
        elif (previous_c.isalpha() or previous_c.isdigit()) and \
                (next_c.isalpha() or next_c.isdigit()):
            line_without_space = line_without_space + actual_c

        previous_c = actual_c
        actual_c = next_c

    if next_c != "\n" and next_c != " ":
        line_without_space = line_without_space + next_c

    return line_without_space
