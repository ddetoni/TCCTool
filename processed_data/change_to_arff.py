import os


def get_all_file_paths(rootDir):

    file_paths = []
    for dir_, _, files in os.walk(rootDir):
        for fileName in files:
            relDir = os.path.relpath(dir_, rootDir)
            relFile = os.path.join(rootDir, relDir, fileName)
            file_paths.append(relFile)

    return file_paths


def create_dir_skeleton():
    os.makedirs('ARFF/CLEC/semestre_1/se1')
    os.makedirs('ARFF/CLEC/semestre_1/se2')
    os.makedirs('ARFF/CLEC/semestre_1/se3')
    os.makedirs('ARFF/CLEC/semestre_1/se4')
    os.makedirs('ARFF/CLEC/semestre_1/se5')
    os.makedirs('ARFF/CLEC/semestre_1/se6')
    os.makedirs('ARFF/CLEC/semestre_1/se7')

    os.makedirs('ARFF/CLEC/semestre_2/se1')
    os.makedirs('ARFF/CLEC/semestre_2/se2')
    os.makedirs('ARFF/CLEC/semestre_2/se3')
    os.makedirs('ARFF/CLEC/semestre_2/se4')
    os.makedirs('ARFF/CLEC/semestre_2/se5')
    os.makedirs('ARFF/CLEC/semestre_2/se6')
    os.makedirs('ARFF/CLEC/semestre_2/se7')

    os.makedirs('ARFF/CLPD/semestre_1/se1')
    os.makedirs('ARFF/CLPD/semestre_1/se2')
    os.makedirs('ARFF/CLPD/semestre_1/se3')
    os.makedirs('ARFF/CLPD/semestre_1/se4')
    os.makedirs('ARFF/CLPD/semestre_1/se5')
    os.makedirs('ARFF/CLPD/semestre_1/se6')
    os.makedirs('ARFF/CLPD/semestre_1/se7')

    os.makedirs('ARFF/CLPD/semestre_2/se1')
    os.makedirs('ARFF/CLPD/semestre_2/se2')
    os.makedirs('ARFF/CLPD/semestre_2/se3')
    os.makedirs('ARFF/CLPD/semestre_2/se4')
    os.makedirs('ARFF/CLPD/semestre_2/se5')
    os.makedirs('ARFF/CLPD/semestre_2/se6')
    os.makedirs('ARFF/CLPD/semestre_2/se7')


def filter_weka_arff(file_paths):

    def arff_path(file_path):

        path_split = file_path.split('/')
        file_name_split = path_split[5].split('.')
        path_split.append(file_name_split[0])

        return './ARFF/{}/{}/{}/{}.arff'.format(path_split[2],
                                                path_split[3],
                                                path_split[4],
                                                path_split[6])

    command = 'java -classpath ../weka.jar weka.filters.unsupervised.attribute.Remove -R 1,2 -i {} -o {}'
    for file_path in file_paths:
        out_path = arff_path(file_path)
        os.system(command.format(file_path, out_path))
        print "Converted: {}".format(out_path)


if __name__ == "__main__":

    file_paths = get_all_file_paths('./CSV/')
    create_dir_skeleton()
    filter_weka_arff(file_paths)
