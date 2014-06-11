import os
import csv
import operator

def get_all_file_paths(rootDir):

    file_paths = []
    for dir_, _, files in os.walk(rootDir):
        for fileName in files:
            relDir = os.path.relpath(dir_, rootDir)
            relFile = os.path.join(rootDir, relDir, fileName)
            file_paths.append(relFile)

    return file_paths


def extract_name(file_path):
    return file_path.split('/')[-1]


def extract_week(file_path):

    if 'se1' in file_path or 'se_1' in file_path:
        return 'se1'
    elif 'se2' in file_path or 'se_2' in file_path:
        return 'se2'
    elif 'se3' in file_path or 'se_3' in file_path:
        return 'se3'
    elif 'se4' in file_path or 'se_4' in file_path:
        return 'se4'
    elif 'se5' in file_path or 'se_5' in file_path:
        return 'se5'
    elif 'se6' in file_path or 'se_6' in file_path:
        return 'se6'
    elif 'se7' in file_path or 'se_7' in file_path:
        return 'se7'


def extract_classifier(file_path):

    if 'bayesnet' in file_path:
        return 'bayesnet'
    elif 'mlp' in file_path:
        return 'mlp'
    elif 'j48' in file_path or 'J48' in file_path:
        return 'j48'
    elif 'randforest' in file_path:
        return 'randforest'

def parse_file(file_path):

    if file_path.split('.')[2] != 'info':
        return None

    file = open(file_path, 'rb')

    splited_file = []
    for line in file:
        split_line = line.split(' ')
        splited_file.append(split_line)

    just_valid_tokens = []
    for line in splited_file:
        for token in line:
            if token != '' and token != '\n' and token != '===' \
                    and token != '%\n':
                just_valid_tokens.append(token)

    file_info = [extract_name(file_path),
                 extract_week(file_path),
                 extract_classifier(file_path),
                 just_valid_tokens[44],
                 just_valid_tokens[13],
                 just_valid_tokens[18],
                 just_valid_tokens[21].replace('\n', ''),
                 just_valid_tokens[25].replace('\n', ''),
                 just_valid_tokens[60],
                 just_valid_tokens[61],
                 just_valid_tokens[67],
                 just_valid_tokens[68]
                 ]

    return file_info


def generate_csv_info(file_paths, save_path):

    file_name = 'results.csv'
    data_file = open(save_path + file_name, 'wb')
    csv_file = csv.writer(data_file, delimiter=',')

    header = ['NomeArq', 'Sem', 'Classif', 'TotalInst', 'CCI', 'ICI', 'Kappa',
              'MAE', 'A-TP-Rate', 'A-FP-Rate', 'R-TP-Rate', 'R-FP-Rate']

    csv_file.writerow(header)
    all_info = []
    for file_path in file_paths:
        file_info = parse_file(file_path)
        if file_info:
            all_info.append(file_info)

    all_info = sorted(all_info, key=operator.itemgetter(1, 2))
    csv_file.writerows(all_info)

    data_file.close()



if __name__ == "__main__":
    file_paths = get_all_file_paths('./entre_semestres/CLEC/')
    generate_csv_info(file_paths, './entre_semestres/CLEC/')

    file_paths = get_all_file_paths('./entre_semestres/CLPD/')
    generate_csv_info(file_paths, './entre_semestres/CLPD/')

    file_paths = get_all_file_paths('./entre_turmas/CLEC/semestre_1/')
    generate_csv_info(file_paths, './entre_turmas/CLEC/semestre_1/')

    file_paths = get_all_file_paths('./entre_turmas/CLEC/semestre_2/')
    generate_csv_info(file_paths, './entre_turmas/CLEC/semestre_2/')

    file_paths = get_all_file_paths('./entre_turmas/CLPD/semestre_1/')
    generate_csv_info(file_paths, './entre_turmas/CLPD/semestre_1/')

    file_paths = get_all_file_paths('./entre_turmas/CLPD/semestre_2/')
    generate_csv_info(file_paths, './entre_turmas/CLPD/semestre_2/')

    file_paths = get_all_file_paths('./sem_atributos/entre_semestres/CLEC/')
    generate_csv_info(file_paths, './sem_atributos/entre_semestres/CLEC/')

    file_paths = get_all_file_paths('./sem_atributos/entre_semestres/CLPD/')
    generate_csv_info(file_paths, './sem_atributos/entre_semestres/CLPD/')

    file_paths = get_all_file_paths('./sem_atributos/entre_turmas/CLEC/semestre_1/')
    generate_csv_info(file_paths, './sem_atributos/entre_turmas/CLEC/semestre_1/')

    file_paths = get_all_file_paths('./sem_atributos/entre_turmas/CLEC/semestre_2/')
    generate_csv_info(file_paths, './sem_atributos/entre_turmas/CLEC/semestre_2/')

    file_paths = get_all_file_paths('./sem_atributos/entre_turmas/CLPD/semestre_1/')
    generate_csv_info(file_paths, './sem_atributos/entre_turmas/CLPD/semestre_1/')

    file_paths = get_all_file_paths('./sem_atributos/entre_turmas/CLPD/semestre_2/')
    generate_csv_info(file_paths, './sem_atributos/entre_turmas/CLPD/semestre_2/')
