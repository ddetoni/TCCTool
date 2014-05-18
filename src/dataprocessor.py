# -*- coding: utf-8 -*-

'''
Created on 06/05/2014

@author: douglas
'''

import csv
from utils import week_interaction
import math


def extract_semester_data(semester, course_weeks, num_weeks, save_path='../'):
    file_name = semester.name + '.csv'
    file_path = save_path + file_name
    data_file = open(file_path, 'wb')
    csv_file = csv.writer(data_file, delimiter=',')

    info_header = ['NomeAluno', 'Situacao', 'Disciplina', 'TotalTutores']

    week_header = ['S'+str(i) for i in range(num_weeks)]

    stats_header = ['Media', 'MediaDif', 'ZeroSem', 'Mediana']

    header = info_header + week_header + stats_header
    table = []
    table.append(header)

    for name, course in semester.courses.iteritems():
        course_table = _extract_course_data(course, course_weeks[name])
        table.extend(course_table)

    csv_file.writerows(table)


def _extract_course_data(course, selected_weeks):

    course_table = []
    for s_name, student in course.students.iteritems():
        row = [
            s_name.encode('utf8'),
            'aprovado' if student.result == 2 else 'reprovado',
            course.name,
            len(course.tutors)
            ]

        week_row = _get_week_interaction(student)

        if selected_weeks:
            n_week_row = _normalize_weeks(week_row, selected_weeks)
            row.extend(n_week_row)
        else:
            row.extend(week_row)

        mean_w = _mean_week_row(n_week_row)
        row.append(mean_w)

        mean_diff = _mean_diff(n_week_row)
        row.append(mean_diff)

        zero_w = _count_zero_weeks(n_week_row)
        row.append(zero_w)

        median_w = _median_week_row(n_week_row)
        row.append(median_w)

        course_table.append(row)

    return course_table


def _get_week_interaction(student):
    week_interactions = week_interaction(student.interactions)
    week_row = range(52)

    for week in week_row:
        if week in week_interactions:
            week_row[week] = week_interactions[week]
        else:
            week_row[week] = 0

    return week_row


def _normalize_weeks(week_row, selected_weeks):

    normalized_week_row = []
    for i in range(len(week_row)):
        if i in selected_weeks:
            normalized_week_row.append(week_row[i])

    return normalized_week_row


def _mean_week_row(week_row):

    count = 0
    sum_interactions = 0

    for num in week_row:
        sum_interactions += int(num)
        count += 1

    return round(sum_interactions / float(count), 2)


def _mean_diff(week_row):

    sum_diff = 0
    for i in range(len(week_row)-1):
        diff = week_row[i] - week_row[i+1]
        sum_diff += math.fabs(diff)

    return round(sum_diff/len(week_row), 2)


def _AD_factor(week_row):

    ad = 0
    previous = 0

    for num in week_row:
        if num > previous:
            ad += 1
        elif num < previous:
            ad += -1
        else:
            pass

        previous = num

    return ad


def _count_zero_weeks(week_row):

    count = 0
    for week in week_row:
        if week == 0:
            count += 1

    return count


def _median_week_row(week_row):

    week_row.sort()
    mid_point = len(week_row)/2

    return week_row[mid_point]
