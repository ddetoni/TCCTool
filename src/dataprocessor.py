# -*- coding: utf-8 -*-

'''
Created on 06/05/2014

@author: douglas
'''

import csv
from utils import week_interaction
import math


def extract_semester_data(semester, course_weeks,
                          num_weeks, group_1, group_2,
                          name, save_path='../'):
    file_name_g1 = name + '_t1.csv'
    file_name_g2 = name + '_t2.csv'

    file_path_g1 = save_path + file_name_g1
    file_path_g2 = save_path + file_name_g2

    data_file_g1 = open(file_path_g1, 'wb')
    csv_file_g1 = csv.writer(data_file_g1, delimiter=',')

    data_file_g2 = open(file_path_g2, 'wb')
    csv_file_g2 = csv.writer(data_file_g2, delimiter=',')

    info_header = ['NomeAluno', 'Disciplina', 'Situacao']

    week_header = ['S'+str(i) for i in range(1, num_weeks+1)]

    stats_header = ['Media', 'MediaDif', 'ZeroSem', 'Mediana', 'RazaoProf',
                    'RazaoTut']

    week_ef_header = ['EF-S'+str(i) for i in range(1, num_weeks+1)]

    header = info_header + week_header + stats_header + week_ef_header
    table_1 = []
    table_2 = []

    table_1.append(header)
    table_2.append(header)

    for name, course in semester.courses.iteritems():

        course_table_1, course_table_2 = _extract_course_data(course,
                                                              course_weeks[name],
                                                              num_weeks,
                                                              group_1,
                                                              group_2)

        table_1.extend(course_table_1)
        table_2.extend(course_table_2)

    csv_file_g1.writerows(table_1)
    data_file_g1.close()
    print 'File: ' + file_name_g1 + ' generated.'

    csv_file_g2.writerows(table_2)
    data_file_g2.close()
    print 'File: ' + file_name_g2 + ' generated.'


def _extract_course_data(course, selected_weeks, num_weeks, group_1, group_2):

    course_table_1 = []
    course_table_2 = []

    total_prof_interactions = _total_educator_interactions(course.professors,
                                                           selected_weeks,
                                                           num_weeks)

    total_tut_interactions = _total_educator_interactions(course.tutors,
                                                          selected_weeks,
                                                          num_weeks)

    for s_name, student in course.students.iteritems():
        row = [
            s_name.encode('utf8'),
            course.name,
            'aprovado' if student.result == 2 else 'reprovado'
            ]

        week_row = _get_week_interaction(student)

        n_week_row = _normalize_weeks(week_row,
                                      selected_weeks,
                                      num_weeks,
                                      0)

        row.extend(n_week_row)

        mean_w = _mean_week_row(n_week_row)
        row.append(mean_w)

        mean_diff = _mean_diff(n_week_row)
        row.append(mean_diff)

        zero_w = _count_zero_weeks(n_week_row)
        row.append(zero_w)

        median_w = _median_week_row(n_week_row)
        row.append(median_w)

        ratio_professor = _ratio_educator(total_prof_interactions, n_week_row)
        row.append(ratio_professor)

        ratio_tutor = _ratio_educator(total_tut_interactions, n_week_row)
        row.append(ratio_tutor)

        if s_name in group_1:
            course_table_1.append(row)
        elif s_name in group_2:
            course_table_2.append(row)

    course_table_1 = _effort_factor(course_table_1, 3, num_weeks)
    course_table_2 = _effort_factor(course_table_2, 3, num_weeks)

    return course_table_1, course_table_2


def _get_week_interaction(student):
    week_interactions = week_interaction(student.interactions)
    week_row = range(52)

    for week in week_row:
        if week in week_interactions:
            week_row[week] = week_interactions[week]
        else:
            week_row[week] = 0

    return week_row


def _normalize_weeks(week_row, selected_weeks, num_weeks, educator_flag):

    count = 0
    index_first_week = 0
    normalized_week_row = []
    for i in range(len(week_row)):
        if i in selected_weeks:
            normalized_week_row.append(week_row[i])

            if count == 0:
                index_first_week = i

            count += 1

        if count == num_weeks:
            break

    if not educator_flag:
        total_before = 0
        for i in range(index_first_week):
            total_before += week_row[i]

        normalized_week_row[0] += total_before

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


def _effort_factor(course_table, index_first_week, num_weeks):
    '''
    This fucntion calculate the Effor Factor, which is the sum of all
    student interactions in a week and divided by the total of students.
    '''

    total = 0
    count = 0
    for week in range(num_weeks):
        for row in course_table:
            total += row[index_first_week+week]
            count += 1

        mean = total/float(count)
        for row in course_table:
            e_factor = round(row[index_first_week+week]/float(mean), 2)
            row.append(e_factor)

        total = 0
        count = 0

    return course_table


def _total_educator_interactions(educators, selected_weeks, num_weeks):

    total_edu_interactions = 0
    for edu in educators.values():
        weeks = _get_week_interaction(edu)
        n_weeks = _normalize_weeks(weeks, selected_weeks, num_weeks, 1)

        for num in n_weeks:
            total_edu_interactions += num

    return total_edu_interactions


def _ratio_educator(total_edu_interaction, n_weeks):

    total = 0
    for week in n_weeks:
        total += week

    return round(total/float(total_edu_interaction), 2)
