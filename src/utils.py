'''
Created on 04/12/2013

@author: douglas
'''

import time
import datetime


# This method apply an intersection between two semester
# and return a list of approved students.
def approved(semester1, semester2):

    approved = list(semester1.normalize_students.intersection(
        semester2.normalize_students))
    return approved


# This method return the disapproved students
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


# Calculate the interactions by week
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


# Remove all the invalids white spaces from a line.
# Return a string with the words separated by "| "
def remove_white_space(file_line):

    line_without_space = ""

    previous_c = " "
    actual_c = " "
    next_c = " "

    line = unicode(file_line, encoding="utf-8")

    for c in line:
        next_c = c

        # Case test for the variable actual_c
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


def generate_semester_csv(semester, class_name, num_weeks, save_path):

    csv_file = open(save_path+semester.name+".csv", 'w')

    weeks = range(num_weeks)
    weeks_string = ['S'+str(i) for i in weeks]

    header = 'NomeAluno,Situacao,Curso,Disciplina,Semestre,SomaInteracoes'

    for w in weeks_string:
        header += ',' + w

    header += '\n'
    csv_file.write(header)

    for course_name, course in semester.courses.iteritems():
        for stu_name, student in course.students.iteritems():
            line = stu_name
            if student.result == 1:
                line += ',reprovado'
            elif student.result == 2:
                line += ',aprovado'

            line += ','+class_name

            line += ','+course_name

            line += ','+semester.name

            line += ','+str(student.total_interactions)

            week_interactions = week_interaction(student.interactions)
            for week in weeks:
                if week in week_interactions:
                    line += ','+str(week_interactions[week])
                else:
                    line += ',0'

            line += '\n'
            csv_file.write(line.encode('utf8'))

    csv_file.close()


def normalize_week_interactions(week_interactions, first_week):

    last_week = first_week + 6  # 7 weeks in total
    normalized_week_interactions = [0]*7

    for week, n_interactions in week_interactions.iteritems():
        if first_week <= week <= last_week:
            normalized_week_interactions[week - first_week] += n_interactions
        elif week < first_week:
            normalized_week_interactions[0] += n_interactions
        elif week > last_week:
            normalized_week_interactions[6] += n_interactions

    return normalized_week_interactions


def generate_semester_csv_normalized(semester, class_name,
                                     first_weeks, save_path):

    csv_file = open(save_path+semester.name+"_norm.csv", 'w')

    weeks = range(1, 8)
    weeks_string = ['S'+str(i) for i in weeks]

    header = 'NomeAluno,Situacao,Curso,Disciplina,Semestre,SomaInteracoes'

    for w in weeks_string:
        header += ',' + w

    header += '\n'
    csv_file.write(header)

    for course_name, course in semester.courses.iteritems():
        for stu_name, student in course.students.iteritems():
            line = stu_name
            if student.result == 1:
                line += ',reprovado'
            elif student.result == 2:
                line += ',aprovado'

            line += ','+class_name

            line += ','+course_name

            line += ','+semester.name

            line += ','+str(student.total_interactions)

            week_interactions = week_interaction(student.interactions)
            normalized_week_interactions = normalize_week_interactions(
                week_interactions,
                first_weeks[course_name])

            for num in normalized_week_interactions:
                line += ','+str(num)

            line += '\n'
            csv_file.write(line.encode('utf8'))

    csv_file.close()


def convert_datekeys_to_timestampkeys(date_dict):

    date_keys = date_dict.keys()
    new_dict = {}

    for date in date_keys:
        timestamp = int(time.mktime(
            datetime.datetime.strptime(date, "%d/%m/%Y").timetuple()))
        new_dict[timestamp] = date_dict[date]

    return new_dict


def select_weeks(semester):

    selected_weeks = {}
    for name, course in semester.courses.iteritems():

        sum_weeks = [0]*53
        for s_name, student in course.students.iteritems():

            week_interactions = week_interaction(student.interactions)
            for i_week, value in week_interactions.iteritems():
                sum_weeks[i_week] += 1

        best_first_week = 0
        highest_sum = 0
        total = 0
        for i in range(53-7):
            total = sum_weeks[i] + sum_weeks[i+1] + sum_weeks[i+2] + \
                sum_weeks[i+3] + sum_weeks[i+4] + sum_weeks[i+5] + \
                sum_weeks[i+6]

            if total > highest_sum:
                highest_sum = total
                best_first_week = i

            total = 0

        selected_weeks[name] = range(best_first_week, best_first_week+7)

    return selected_weeks
