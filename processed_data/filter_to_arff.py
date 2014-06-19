import os


def get_all_file_paths(rootDir):

    file_paths = []
    for dir_, _, files in os.walk(rootDir):
        for fileName in files:
            relDir = os.path.relpath(dir_, rootDir)
            relFile = os.path.join(rootDir, relDir, fileName)
            file_paths.append(relFile)

    return file_paths


def create_dir_skeleton(base_name):
    os.makedirs('{}/CLEC/semestre_1/se1'.format(base_name))
    os.makedirs('{}/CLEC/semestre_1/se2'.format(base_name))
    os.makedirs('{}/CLEC/semestre_1/se3'.format(base_name))
    os.makedirs('{}/CLEC/semestre_1/se4'.format(base_name))
    os.makedirs('{}/CLEC/semestre_1/se5'.format(base_name))
    os.makedirs('{}/CLEC/semestre_1/se6'.format(base_name))
    os.makedirs('{}/CLEC/semestre_1/se7'.format(base_name))

    os.makedirs('{}/CLEC/semestre_2/se1'.format(base_name))
    os.makedirs('{}/CLEC/semestre_2/se2'.format(base_name))
    os.makedirs('{}/CLEC/semestre_2/se3'.format(base_name))
    os.makedirs('{}/CLEC/semestre_2/se4'.format(base_name))
    os.makedirs('{}/CLEC/semestre_2/se5'.format(base_name))
    os.makedirs('{}/CLEC/semestre_2/se6'.format(base_name))
    os.makedirs('{}/CLEC/semestre_2/se7'.format(base_name))

    os.makedirs('{}/CLPD/semestre_1/se1'.format(base_name))
    os.makedirs('{}/CLPD/semestre_1/se2'.format(base_name))
    os.makedirs('{}/CLPD/semestre_1/se3'.format(base_name))
    os.makedirs('{}/CLPD/semestre_1/se4'.format(base_name))
    os.makedirs('{}/CLPD/semestre_1/se5'.format(base_name))
    os.makedirs('{}/CLPD/semestre_1/se6'.format(base_name))
    os.makedirs('{}/CLPD/semestre_1/se7'.format(base_name))

    os.makedirs('{}/CLPD/semestre_2/se1'.format(base_name))
    os.makedirs('{}/CLPD/semestre_2/se2'.format(base_name))
    os.makedirs('{}/CLPD/semestre_2/se3'.format(base_name))
    os.makedirs('{}/CLPD/semestre_2/se4'.format(base_name))
    os.makedirs('{}/CLPD/semestre_2/se5'.format(base_name))
    os.makedirs('{}/CLPD/semestre_2/se6'.format(base_name))
    os.makedirs('{}/CLPD/semestre_2/se7'.format(base_name))


def filter_weka_arff(file_paths, base_name):

    def arff_path(file_path):

        path_split = file_path.split('/')
        file_name_split = path_split[5].split('.')
        path_split.append(file_name_split[0])

        return './{}/{}/{}/{}/{}.arff'.format(base_name,
                                                path_split[2],
                                                path_split[3],
                                                path_split[4],
                                                path_split[6]), path_split[4]

    command = 'java -classpath ../weka.jar weka.filters.unsupervised.attribute.Remove -R 1,2 -i {} -o {}'
    for file_path in file_paths:
        out_path, se_number = arff_path(file_path)
        num_weeks = int(se_number[2])
        print num_weeks

        os.system(command.format(file_path, out_path))
        print "Converted: {}".format(out_path)


if __name__ == "__main__":

    file_paths = get_all_file_paths('./CSV_balanced/')
    create_dir_skeleton('ARFF_balanced')
    filter_weka_arff(file_paths, 'ARFF_balanced')
